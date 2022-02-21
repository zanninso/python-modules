from cgi import print_directory


class ObjectC(object):
    def __init__(self):
        pass


def what_are_the_vars(*args, **kargs):
    """
    print the given agrs
    """
    obj = ObjectC()
    for idx, elm in enumerate(args):
        key = 'var_' + str(idx)
        try:
            getattr(obj, key)
            return
        except Exception as e:
            setattr(obj, key, elm)
    for key in kargs:
        try:
            getattr(obj, key)
            return
        except Exception as e:
            setattr(obj, key, kargs[key])
    return obj


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
