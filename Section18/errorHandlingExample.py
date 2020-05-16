def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        if b == 0:
            return f"Unfortunately you can't divide by {b}!"


print(divide(1,2))
print(divide(9,0))
print(divide(0, 5))
print(divide(88,0))


def divideMine(firstNumber, secondNumber):
    try:
        return firstNumber / secondNumber
    except ZeroDivisionError:
        if secondNumber == 0:
            return f"Again, unfortunately you can't divide by {secondNumber}!"


firstNumber = input("Enter first number: ")
secondNumber = input ("Enter second number: ")

print(divideMine(int(firstNumber), int(secondNumber)))
