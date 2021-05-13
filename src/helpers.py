import math

def w2t_mle(data, output_file):

    ### MLE computing
    #Computing of Maximum Likelihood Estimation with negative log probabilites.
    #Allows for more control of OOV instead of bigram modeling. Assign an uniform cost for every concept and unknown word pair.

    words = dict()
    concepts = dict()
    words_concepts = dict()

    for word, concept in data:
        words[word] = words.get(word, 0) + 1.0
        concepts[concept] = concepts.get(concept, 0) + 1.0
        words_concepts[word + " " +
                       concept] = words_concepts.get(word + " " + concept, 0) + 1.0

    with open(output_file, 'w') as file:
        for word_concept in words_concepts:
            word, concept = word_concept.split()
            cost = -1 * \
                math.log(words_concepts[word + " " +
                         concept] / concepts[concept])
            file.write("0 0 " + word + " " + concept + " " + str(cost) + "\n")
        for concept in concepts.keys():
            cost = 1 / len(concepts.keys())
            file.write("0 0 <UNK> " + concept + " " + str(cost) + "\n")
        file.write("0\n")

def w2t_unweighted(data, output_file):
    
    ### FST computing
    # #Computing of unweighted FST.

    words = set()
    concepts = set()
    words_concepts = set()

    for word, concept in data:
        words.add(word)
        concepts.add(concept)
        words_concepts.add(word + " " + concept)

    with open(output_file, 'w') as file:
        for word_concept in words_concepts:
            word, concept = word_concept.split()
            file.write("0 0 " + word + " " + concept + "\n")
        for concept in concepts:
            file.write("0 0 <UNK> " + concept + "\n")
        file.write("0\n")


def make_tag(corpus):
    ### Build tags corpus
    # Refactor corpus substituting words with relative tags
    return [[word[1] for word in sent] for sent in corpus]


def make_word_tag_conll(corpus):
    ### Build words and tags conll
    # Refactor conll substituting O tags with words
    return [[(word[0], word[0]) if word[-1] == 'O' else (word[0], word[-1]) for word in sent] for sent in corpus]


def make_word_plus_tag_conll(corpus):
    ### Build word plus tags conll
    # Refactor conll substituting tags with word+tag
    return [[(word[0], word[0] + '+' + word[1]) for word in sent] for sent in corpus]


def convert_to_tag(file):
    ### Convert output for evaluation
    # Replace words with O tags
    lines = [line.strip().split("\t") for line in open(file, 'r')]
    with open(file, 'w') as f:
        for line in lines:
            if len(line) >= 4:
                if not(line[3].startswith("B-") or line[3].startswith("I-")):
                    line[3] = 'O'
            f.write("\t".join(line) + "\n")


def get_words_tags_cutoff(corpus, cut_min=2):

    ### Cut off on words
    # Return word concepts pair with applied cutoff

    words = dict()
    sentences = []
    cutoff = []

    for s in corpus:
        for word, tag in s:
            words[word] = words.get(word, 0) + 1
            sentences.append([word, tag])

    for word, tag in sentences:
        if words[word] >= cut_min:
            cutoff.append([word, tag])
    return cutoff
