import pandas as pd

results = pd.read_csv('results.csv')

words = results[results['type'] == 'w']
words_and_concepts = results[results['type'] == 'w_and_c']
words_plus_concepts = results[results['type'] == 'w_plus_c']

words_sorted = words.sort_values('f1', ascending=False)
words_and_concepts_sorted = words_and_concepts.sort_values('f1', ascending=False)
words_plus_concepts_sorted = words_plus_concepts.sort_values('f1', ascending=False)

print(words_sorted.head(15))
print(words_and_concepts_sorted.head(15))
print(words_plus_concepts_sorted.head(15))