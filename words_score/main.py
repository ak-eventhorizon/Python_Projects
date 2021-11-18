"""
Function score_words takes a list of lowercase words as an argument
and returns a score as follows:

The score of a single word is 2 if the word contains an even number of vowels.
Otherwise, the score of this word is 1. The score for the whole list of words
is the sum of scores of all words in the list.

['programming', 'is', 'awesome']  --> 4 (1 + 1 + 2)

"""


def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0

        for letter in word:
            if is_vowel(letter):
                num_vowels += 1

        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


if __name__ == '__main__':

    words1 = ['hacker', 'book']  # 4 = 2 + 2
    print(score_words(words1))

    words2 = ['programming', 'is', 'awesome']  # 4 = 1 + 1 + 2
    print(score_words(words2))

    words3 = ['programming', 'is', 'awesome', 'rrr', 'tt']  # 4 = 1 + 1 + 2 + 0 + 0
    print(score_words(words3))

    words4 = ['london', 'is', 'capital', 'of', 'great', 'britain']  # 8 = 2 + 1 + 1 + 1 + 2 + 1
    print(score_words(words4))

    words5 = ['fbibepbwicbq',
              'vqpyywkbvkyjzsmhydvh',
              'gn',
              'axkzfhkyjcgyoaspzex',
              'mcrzwd',
              'cohtzztocconrmbzle',
              'znimrpssdsbkma']  # 13
    print(score_words(words5))
