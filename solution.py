import csv


class Solution:
    def __init__(self):
        self.words = []

    def read_file(self, filename):
        with open(filename) as data:
            csv_reader = csv.reader(data, delimiter=" ")
            next(csv_reader)
            for row in csv_reader:
                self.words.append(row[0])
        return self.words

    def longest_words_chain(self, words) -> int:
        words.sort(key=len)
        words_chains = {word: 1 for word in words}
        longest_chain = 1
        for word in words:
            for letter in range(len(word)):
                existing_word = word[:letter] + word[letter + 1:]
                if existing_word in words_chains:
                    words_chains[word] = words_chains[existing_word] + 1
                    longest_chain = max(longest_chain, words_chains[word])
        return longest_chain


