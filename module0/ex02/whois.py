import sys
try:
    if (len(sys.argv) != 2):
        raise Exception()
    n = int(sys.argv[1])
    if (n == 0):
        print("I'm Zero.")
    elif (n % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
except Exception:
    print("ERROR")
