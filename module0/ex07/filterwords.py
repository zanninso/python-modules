import string
import sys
import re

patrn = '[' + re.escape(string.punctuation) + ']'
if (len(sys.argv) == 3 and sys.argv[2].isdigit() and int(sys.argv[2]) >= 0):
    words = sys.argv[1].split()
    min_len = int(sys.argv[2])
    words = [re.sub(patrn, '', word) for word in words]
    print([word for word in words if (len(word) > min_len)])
else:
    print("ERROR")
