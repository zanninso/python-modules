from vector import Vector

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print("Column vector of shape n * 1: ", v1.__repr__())
output = v1 * 5
print("Vector * 5 = ", output)
print("shape:", output.shape)
print()

v1 = Vector([[0.0, 6.0, 2.0, 3.0]])
print("Row vector of shape 1 * n: ", v1.__repr__())
output = v1 + output
print("Vector + output = ", output)
print("shape:", output.shape)
print()

v1 = Vector(4)
print("Column vector of shape 1 * n: ", v1.__repr__())
output = v1 - output
print("Vector - output = ", output)
print("shape:", output.shape)
print()

print("{} . {}".format(v1.__repr__(), output.__repr__()))
output = v1.dot(output)
print("Output:", output)
print()

v1 = Vector(range(10, 15))
print("Column vector of shape 1 * n: ", v1.__repr__())
output = v1 / 2.0
print("Vector / 2.0 = ", output)
print("shape:", output.shape)
print()


try:
    2.0 / v1
except Exception as e:
    print(e)
