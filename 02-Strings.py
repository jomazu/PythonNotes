# Variables allow you to manipulate the contents of the variable, from a user input etc.
message = 'Hello world'
print(message.lower())
print(message.upper())
print(message.swapcase())
# Collect name from user
name = input("What is your name? ")
country = input("What country do you live in? ")
country = country.upper()
print('\nHey, ' + name + ' lives in the ' + country)
message = 'Hello world'
# Finds the number of characters before "world", which is 6
print(message.find('world'))
# Counts the number of the character "o", which is 2
print(message.count('o'))
print(message.capitalize())
print(message.replace('Hello' , 'Hi'))