import sys

MCD = {'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-',
            'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--',
            'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.',
            '0': '-----'}

sys.argv.pop(0)
args = []

for arg in sys.argv:
    args += arg.split()

for arg in args:
    if (arg.isalnum() is False):
        exit(print("ERROR"))

word_sep = ''
char_sep = ''
for arg in args:
    print(word_sep, *[MCD[c.upper()] for c in arg], sep=char_sep, end='')
    word_sep = ' /'
    char_sep = ' '
print()
