try:
    value = int(input("Enter a number: "))
    value2 = int(input("Enter another number: "))
except ValueError:
   print("An integer was not given, try again.")

try:
    print(value / value2)
except ZeroDivisionError:
    print("Division by zero is not possible, sorry")  
