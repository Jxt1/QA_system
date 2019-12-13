######################################################
# refer to https://github.com/phatpiglet/autocorrect #
######################################################

import re
from collections import Counter
import os
import json
from itertools import chain

PATH = os.path.abspath(os.path.dirname(__file__))

word_regexes = {
    'en': r'[A-Za-z]+', 
}

alphabets = {
    'en': 'abcdefghijklmnopqrstuvwxyz',
}

def concat(*args):
    """reversed('th'), 'e' => 'hte'"""
    try:
        return ''.join(args)
    except TypeError:
        # print(args)
        return ''.join(chain.from_iterable(args))

class Word(object):
    """container for word-based methods"""

    def __init__(self, word, lang='en'):
        """
        Generate slices to assist with typo
        definitions.
        'the' => (('', 'the'), ('t', 'he'),
                  ('th', 'e'), ('the', ''))
        """
        slice_range = range(len(word) + 1)
        self.slices = tuple((word[:i], word[i:])
                            for i in slice_range)
        self.word = word
        self.alphabet = alphabets[lang]

    def _deletes(self):
        """th"""
        for a, b in self.slices[:-1]:
            yield concat(a, b[1:])

    def _transposes(self):
        """teh"""
        for a, b in self.slices[:-2]:
            yield concat(a, reversed(b[:2]), b[2:])

    def _replaces(self):
        """tge"""
        for a, b in self.slices[:-1]:
            for c in self.alphabet:
                yield concat(a, c, b[1:])

    def _inserts(self):
        """thwe"""
        for a, b in self.slices:
            for c in self.alphabet:
                yield concat(a, c, b)

    def typos(self):
        """letter combinations one typo away from word"""
        for e in self._deletes():
            yield e
        for e in self._transposes():
            yield e
        for e in self._replaces():
            yield e
        for e in self._inserts():
            yield e

    def double_typos(self):
        """letter combinations two typos away from word"""
        for e1 in self.typos():
            for e2 in Word(e1).typos():
                yield e2

class Speller:
    def __init__(self, threshold=0, lang='en'):
        self.threshold = threshold
        words_file = os.path.join(PATH, 'data/word_count.json')
        fp = open(file=words_file)
        self.nlp_data = json.load(fp)
        fp.close()
        self.lang = lang

        if threshold > 0:
            print('Original number of words: {}'
                    .format(len(self.nlp_data)))
            self.nlp_data = {k: v for k, v in self.nlp_data.items() 
                            if v > threshold}
            print('After applying threshold: {}'
                    .format(len(self.nlp_data)))

    def existing(self, words):
        """{'the', 'teh'} => {'the'}"""
        return set(word for word in words
                   if word in self.nlp_data)

    def autocorrect_word(self, word):
        """most likely correction for everything up to a double typo"""
        w = Word(word, self.lang)
        candidates = (self.existing([word]) or 
                      self.existing(w.typos()) or 
                      self.existing(w.double_typos()) or 
                      [word])
        return max(candidates, key=self.nlp_data.get)


    def autocorrect_sentence(self, sentence):
        return re.sub(word_regexes[self.lang],
                      lambda match: self.autocorrect_word(match.group(0)),
                      sentence)

    __call__ = autocorrect_sentence

spell = Speller(lang='en')


def validate():
    with open('./data/missp.dat.txt') as f:
        lines = f.readlines()
        i = 0
        all_word = 0
        correct = 0
        unknown_word = 0
        while i < lines.__len__() - 1:
            a = lines[i].strip('\n')
            i = i + 1
            print(i, a)
            assert(a[0]=='$')
            if a[1:] not in spell.nlp_data:
                unknown_word = unknown_word + 1
                while i < lines.__len__():
                    b = lines[i]
                    if b[0] == '$':
                        break
                    i = i + 1
                continue

            while i < lines.__len__():
                b = lines[i].strip('\n')
                if b[0] == '$':
                    break
                if spell(b) == a[1:]:
                    correct = correct + 1
                i = i + 1
                all_word = all_word + 1
            print('all words: {}, correct: {}, unknown: {}.'.format(all_word, correct, unknown_word))

if __name__ == "__main__":
    # print(spell('how to implemetn matrx multple?'))
    validate()

