from time import sleep
import my_minipack.progressbar as progressbar

listy = range(100000)
ret = 0
for elem in progressbar.ft_progress(listy):
    ret += elem
    sleep(0.001)
print()
print(ret)

deleted:    ex00/ft_filter.py ex00/ft_map.py ex00/ft_reduce.py ex01/main.py ex02/logger.py ex03/csvreader.py ex03/test.py ex04/README.md ex04/build.sh ex04/setup.cfg ex04/setup.py ex04/src/my_minipack/__init__.py ex04/src/my_minipack/logger.py ex04/src/my_minipack/progressbar.py ex04/test.py