# Data type = String

# use quotes inside string = \'
# string on multiple lines = """ text here multiple lines """ (3 quotations)
# message = 'Hello World'
# print(message[:6])
# first index is included, : til last index (not inclusive)
# empty last index = til end
# empty first index = begining til index declared

# message = 'Hello World'
# newmessage = message.replace('World', 'Universe')
# print(newmessage.upper())

# methods:
# .lower()/.upper()
# .count()
# replace()

# greeting = 'Hello'
# name = 'Tenzin'
# message = greeting + ', ' + name + '. Welcome.'
# message = '{}, {}. Welcome'.format(greeting, name.upper())
# message = f'{greeting}, {name.upper()}. Welcome!'
# print(message)

# see more
# name = 'Tenzin'
# print(help(str.lower)) # To get help by method_descriptor
# print(dir(name)) # To get all methods available to us to use

# Integers & Floats

# num = 3 # int
# num = 3.14 # float

# Arthmetic Operators:
# Addition: 3 + 2
# Subtraction: 3 - 2
# Multiplication: 3 * 2
# Division: 3 / 2
# Floor Division:3 // 2 (rounds down to int)
# Exponent: 3 ** 2 (3 squared)
# Modulus: 3 % 2

# print(3 // 2) # Math.floor()
# print(3 % 2) # mod 2 = 0 (EVEN) # mod 2 = 1 (ODD)

# PEMDAS In Python

# num = 1
# num += 10
# print(num) # 11 -> (num + 10)

# print(round(-3.25)) # Round to closest INT

# num_1 = 3
# num_2 = 2
# print(num_1 > num_2)

# Wrap string numbers in int() to get value
# num_1 = int('100')
# num_2 = int('200')
# print(num_1 + num_2)

# CONDITIONALS

# language = 'Java'
# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# elif language == 'JavaScript':
#     print('Language is JavaScript')
# else: 
#     print('No Match')

user = 'Admin'
logged_in = False

# if user == 'Admin' and logged_in:
#     print('Admin Page')
# else:
#     print('Bad Credentials')
