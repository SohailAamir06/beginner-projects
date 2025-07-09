import math

def calc(x, y):
    print("Addition         :", x + y)
    print("Subtraction      :", x - y)
    print("Multiplication   :", x * y)
    print("Division         :", x / y if y != 0 else "Undefined (division by 0)")
    print("Modulus          :", x % y if y != 0 else "Undefined (mod by 0)")
    print("Exponentiation   :", x ** y)
    print("Floor Division   :", x // y if y != 0 else "Undefined (division by 0)")
    print("Square Root of x :", math.sqrt(x) if x >= 0 else "Invalid (sqrt of negative)")
    print("Square Root of y :", math.sqrt(y) if y >= 0 else "Invalid (sqrt of negative)")
    print("Absolute x       :", abs(x))
    print("Absolute y       :", abs(y))
    print("Maximum          :", max(x, y))
    print("Minimum          :", min(x, y))

x, y = map(int, input("Enter two numbers (space-separated): ").split())
calc(x, y)
