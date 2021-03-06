def ft_reduce(fun, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    result = iterable.pop(0)
    for iter in iterable:
        result = fun(result, iter)
    return result
