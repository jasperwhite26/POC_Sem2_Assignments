try:
    value = int(input("Enter a number: "))
    value2 = int(input("Enter another number: "))
    print(value / value2)
except ZeroDivisionError:
    print("Division by zero is not possible, sorry.")
