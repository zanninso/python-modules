
import random


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    try:
        if ((isinstance(text, str) and isinstance(sep, str)) is False):
            raise Exception()
        words = text.split(sep)
        if (option == 'shuffle'):
            random. shuffle(words)
        elif (option == 'unique'):
            words = list(set(words))
        elif (option == 'ordered'):
            words.sort()
        for word in words:
            yield word
    except Exception as e:
        print("ERROR ", e)
