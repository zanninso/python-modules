from curses.ascii import islower, isupper
import string


def text_analyzer(*args):
    "counts the number of upper, lower, space characters \
    and punctuation in a given text."
    if (len(args) > 1 or (len(args) > 0 and type(args[0]) != str)):
        print("ERROR")
        return
    if (len(args) == 0):
        txt = input("What is the txt to analyse?: ")
    else:
        txt = args[0]
    txt = "Aa ," if (txt == "") else txt
    print("The txt contains " + str(len(txt)) + " characters:")
    print("- ", sum(isupper(c) for c in txt), " upper letters")
    print("- ", sum(islower(c) for c in txt), " lower letters")
    print("- ", sum(c in string.punctuation for c in txt), " punctuation mark")
    print("- ", sum(c == ' ' for c in txt), " spaces")
