# helper https://pyformat.info/

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

for language in languages:
    print('{} was created by {}'.format(language, languages[language]))
