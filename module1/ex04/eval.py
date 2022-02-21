import re


class Evaluator:
    @classmethod
    def zip_evaluate(self, coefs, words):
        if (len(coefs) != len(words)):
            return (-1)
        return (sum([c * len(w) for c, w in zip(coefs, words)]))

    @classmethod
    def enumerate_evaluate(self, coefs, words):
        if (len(coefs) != len(words)):
            return (-1)
        return (sum([coefs[c] * len(e) for c, e in enumerate(words)]))
