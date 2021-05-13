import sys
import os
sys.path.insert(0, os.path.abspath('../helpers/'))
import pandas as pd
import subprocess
from conll import evaluate
from helpers_labs import read_corpus_conll, read_fst4conll
from helpers import get_words_tags_cutoff, make_tag, make_word_plus_tag_conll, make_word_tag_conll, w2t_mle, w2t_unweighted, convert_to_tag


wdir = '../w_dir/'

# model type ['w', 'w_and_c', 'w_plus_c']
# n-gram order
# method ['witten_bell', 'absolute', 'katz', 'kneser_ney', 'presmoothed', 'unsmoothed']
# cutoff

mtypes = ['w', 'w_and_c', 'w_plus_c']
methods = ['witten_bell', 'absolute', 'katz',
           'kneser_ney', 'presmoothed', 'unsmoothed']

err_string = "Usage: \n - model type: ['w', 'w_and_c', 'w_plus_c']  (required)\n - n-gram order: [integer number] (required)\n - smoothing method: ['witten_bell' | 'absolute' | 'katz' | 'kneser_ney' | 'presmoothed' | 'unsmoothed'] (required)\n - cutoff: [integer number]  (optional, default: 2)"


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():

    ### Check arguments
    if(len(sys.argv) < 4):
        print(err_string)
        sys.exit()

    mtype = sys.argv[1]
    order = sys.argv[2]
    method = sys.argv[3]
    cutoff = 2
    
    if len(sys.argv) > 4:
        cutoff = sys.argv[4]

    if not (method in methods):
        print(err_string)
        sys.exit()

    if not isInt(order):
        print(err_string)
        sys.exit()

    if not (mtype in mtypes):
        print(err_string)
        sys.exit()

    if not isInt(cutoff):
        print(err_string)
        sys.exit()

    ### Copy datasets
    subprocess.call(['./copy_files.sh'])

    ### Create files for training corpus and symbols tapes
    train_conll = read_corpus_conll(wdir + 'train.conll')

    if mtype == 'w_and_c':
        custom_train = make_word_tag_conll(train_conll)
    elif mtype == 'w_plus_c':
        custom_train = make_word_plus_tag_conll(train_conll)
    else:
        custom_train = train_conll

    tags_corpus = make_tag(custom_train)
    words_tags_cutoff = get_words_tags_cutoff(custom_train, int(cutoff))
    words = [t[0] for t in words_tags_cutoff]
    tags = [t[1] for t in words_tags_cutoff]

    with open(wdir + 'words.txt', 'w') as f:
        f.write("\n".join(words) + "\n")

    with open(wdir + 'tags.txt', 'w') as f:
        f.write("\n".join(tags) + "\n")

    with open(wdir + 'train.tags.txt', 'w') as f:
        for s in tags_corpus:
            f.write(" ".join(s) + "\n")

    ### Create symbol tapes
    subprocess.call(['./generate_symbols.sh'])

    ### Create words-concepts transducer
    if mtype == 'w_plus_c':
        w2t_unweighted(words_tags_cutoff, wdir + 'w2t.txt')
    else:
        w2t_mle(words_tags_cutoff, wdir + 'w2t.txt')

    subprocess.call(['./compile_transducer.sh'])

    ### Create language model
    subprocess.call(['./compile_model.sh', order, method])

    ### Compile test sentences to far
    subprocess.call(['./compile_test.sh'])

    ### Test pipeline with test data
    subprocess.call(['./compose_pipeline.sh'])
    
    ### Print performance
    if mtype == 'w_and_c':
        convert_to_tag(wdir + 'w2t_m.out')

    refs = read_corpus_conll(wdir + 'test.conll')
    hyps = read_fst4conll(wdir + 'w2t_m.out', split=(mtype == 'w_plus_c'))

    results = evaluate(refs, hyps)

    pd_tbl = pd.DataFrame().from_dict(results, orient='index')
    print("F1 score: {:.4f}\nPrecision: {:.4f}\nRecall: {:.4f}". format(pd_tbl.loc['total', 'f'], pd_tbl.loc['total', 'p'], pd_tbl.loc['total', 'r']))

if __name__ == "__main__":
    main()