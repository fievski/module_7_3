import string
from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                text = f.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word)
        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            results[file_name] = words.count(word)
        return results

finder2 = WordsFinder('text.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# name = 'text.txt'
# with open(name, encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')
#     print(file.tell())
