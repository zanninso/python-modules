# helper https://pyformat.info/

t = (19, 42, 21, 55, 56)
output = 'The {} numbers are: {}'.format(len(t), t)
print(output.replace("(", '').replace(")", ''))
