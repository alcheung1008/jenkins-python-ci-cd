def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


if __name__ == "__main__":
    print("Addition of 6 and 7 is:", add(6, 7))
    print("Subtraction of 2 from 9 is:", subtract(9, 2))
    print("Multiplication of 9 and 3 is:", multiply(9, 3))
    print("Division of 90 by 15 is:", divide(90, 15))
