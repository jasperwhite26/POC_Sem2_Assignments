text = input('enter text: ')

result = text.find("the")

if result == -1:
    print("the word the is not in the string")
else:
    print("the word the is in the string")
    print(result)