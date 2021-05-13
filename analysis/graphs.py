from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

sentences = [line.strip().split() for line in open('../data/NL2SparQL4NLU.train.utterances.txt', 'r')]
s_length = [len(s) for s in sentences]

m = np.mean(s_length)
b = range(min(s_length), max(s_length))

fig, axes = plt.subplots()
axes.hist(s_length, bins=b, color='grey')
axes.axvline(x=np.mean(s_length), c='black')
axes.text(x=7, y=100, s='mean={:.2f}'.format(m), c='black')
axes.set_title('Train sentence length')
axes.set_xlabel('# Words')
axes.set_ylabel('# Number')
axes.xaxis.set_major_locator(ticker.MultipleLocator(1))
fig.savefig('words_length.png', dpi=300)

words_list = [w for s in sentences for w in s]
words_dict = dict()
for word in words_list:
    words_dict[word] = words_dict.get(word, 0) + 1
words = pd.DataFrame.from_dict(words_dict, orient='index', columns=['count'])
words.sort_values(by='count', inplace=True, ascending=False)

words['idx'] = range(1, len(words) + 1)
words['real'] = words['count'] / len(words_list)

s = 0.0
for n in range(1, len(words) + 1):
    s += 1/n

words['predicted'] = (1 / words['idx']) / s

print(words)

fig, axes = plt.subplots()
axes.scatter(np.log(words['idx']), np.log(words['real']), color='grey')
axes.plot(np.log(words['idx']), np.log(words['predicted']), color='black')
axes.text(x=0.4, y=-2.3, s='predicted', c='black')
axes.set_title('Zipf\'s law')
axes.set_xlabel('log(rank)')
axes.set_ylabel('log(frequency)')
fig.savefig('zipf.png', dpi=300)

def get_concept_dict(file):
    d = dict()
    for line in open(file, 'r'):
        l = line.strip().split('\t')
        if len(l) > 1:
            t = l[1].split('-')
            if len(t) > 1:
                c = t[1]
                d[c] = d.get(c, 0) + 1
    return d

train_dict = get_concept_dict('../data/NL2SparQL4NLU.train.conll.txt')
test_dict = get_concept_dict('../data/NL2SparQL4NLU.test.conll.txt')

concepts = list(set(list(train_dict.keys()) + list(test_dict.keys())))

train_size = sum(train_dict.values())
test_size = sum(test_dict.values())


data = [[c, 100*train_dict.get(c, 0)/train_size, 100*test_dict.get(c, 0)/test_size] for c in concepts]

df = pd.DataFrame(data=data, columns=['concept', 'train', 'test'])
df.sort_values(by='train' ,axis=0, inplace=True, ascending=True)

print(df)

train_ordered = sorted(train_dict, key=lambda item: item[1])
test_ordered = sorted(test_dict, key=lambda item: item[1])

fig, axes = plt.subplots()
df.plot(x='concept', y=['train', 'test'], kind='barh', color=['darkgrey', 'lightgrey'], ax=axes)
axes.text(x=2.5, y=5, s='<0.1%', c='black')
axes.set_title('Concepts distribution')
axes.set_xlabel('Percentage %')
axes.legend(loc='lower right')
axes.xaxis.set_minor_locator(ticker.MultipleLocator(5))
axes.grid(axis='x', linestyle='-', linewidth=0.5)
axes.grid(axis='x', linestyle='--', linewidth=0.3, which='minor')
plt.subplots_adjust(left=0.3)
plt.savefig('concepts.png', dpi=300)