import sys

try:
    if (len(sys.argv) != 3):
        raise Exception("Invalid arguments number")
    a, b = int(sys.argv[1]), int(sys.argv[2])
    print("Sum:\t\t" + str(a + b))
    print("Difference:\t" + str(a - b))
    print("Product:\t" + str(a * b))
    print("Quotient:\t" + str(a / b if b != 0 else "ERROR (div by zero)"))
    print("Remainder:\t" + str(a / b if b != 0 else "ERROR (modulo by zero)"))

except ValueError as e:
    print("InputError: only numbers")
    print("\nUsage: python operations.py <number1> <number2>", "Example:", "\
        \tpython operations.py 1 1", sep='\n')
except Exception as e:
    print("InputError: ", e)
    print("\nUsage: python operations.py <number1> <number2>", "Example:", "\
        \tpython operations.py 1 1", sep='\n')
