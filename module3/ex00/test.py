from NumPyCreator import NumPyCreator
npc = NumPyCreator()

print(npc.from_list([[1, 2, 3], [6, 3, 4]]), '\n')

print(npc.from_list([[1, 2, 3], [6, 4]]), '\n')

print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]), '\n')

print(npc.from_list(((1, 2), (3, 4))), '\n')

print(npc.from_tuple(("a", "b", "c")), '\n')

print(npc.from_tuple([[1, 2, 3], [6, 3, 4]]), '\n')

print(npc.from_iterable(range(5)), '\n')

shape = (3, 5)
print(npc.from_shape(shape), '\n')

print(npc.random(shape), '\n')

print(npc.identity(4), '\n')
