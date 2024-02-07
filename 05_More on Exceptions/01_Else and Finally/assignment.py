number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    print(number1 / number2)
except ZeroDivisionError:
    print("Division by zero is not possible, sorry")
else:
    print("No value error detected")
finally:
    print("I always run")
