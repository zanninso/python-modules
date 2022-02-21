from time import time
import curses


def moment(s):
    d = int(s / (24 * 60 * 60))
    s %= (24 * 60 * 60)
    h = int(s / (60 * 60))
    s %= (60 * 60)
    m = int(s / 60)
    s %= 60
    s = s
    nd = min(1, d)
    nh = max(min(1, h), nd)
    nm = max(min(1, m), nh)
    return("{}d".format(d) * nd + " {}h".format(h) * nh + " \
{}m".format(m) * nm + " {:.2f}s".format(s))


def ft_progress(lst):
    curses.setupterm()
    idx = 1
    lst_len = len(lst)
    t = time()
    t0 = 0
    predicted_time = 0
    bar_size = 20
    output_format = 'ETA: {} [{}%][{}>{}] {}/{} | elapsed time {} '

    print('start ', lst_len)
    while idx <= lst_len:

        predicted_time = moment(((time() - t) / idx) * (lst_len - idx))
        percent = int(idx / lst_len * 100)
        prgs = int(idx / (lst_len / 20))

        print(curses.tigetstr('el').decode(), end='')
        params = [predicted_time, percent, '=' * prgs, ' ' * (bar_size - prgs)]
        params += [idx, lst_len, "%.2f" % (time() - t)]
        print(output_format.format(*params))
        print(curses.tigetstr('cuu1').decode(), end='')

        yield lst[idx-1]
        idx += 1
