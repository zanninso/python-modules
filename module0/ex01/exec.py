import sys

sys.argv.pop(0)
sys.argv = sys.argv[::-1]
sep = ''
for arg in sys.argv:
    print(sep, arg.swapcase()[::-1], end='', sep='')
    sep = ' '
print()
