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
    print("Addition of 7 and 6 is:", add(7, 6))
    print("Subtraction of 6 from 9 is:", subtract(9, 6))
    print("Multiplication of 73 and 61 is:", multiply(73, 61))
    print("Division of 100 by 25 is:", divide(100, 25))
