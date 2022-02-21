from generator import generator


print('test1:')
text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)
print('-------------------------------------------')

print('test2:')
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print('-------------------------------------------')

print('test3:')
for word in generator(text, sep=" ", option="ordered"):
    print(word)
print('-------------------------------------------')

print('test4:')
text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)
print('-------------------------------------------')

print('test5:')
text = 1.0
for word in generator(text, sep="."):
    print(word)
