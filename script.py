import random

#Take input
n = int(input('Enter length of password: '))

# Maintaining list of alphabets, numbers and special characters
alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
number_list = list('0123456789')
special_char_list = list('!@#$%^&*()_+=-')

# Combining lists
collection = [alphabet_list,number_list,special_char_list]
collection = collection*(int(n/3))
random.shuffle(collection)

# Generating password
pass_string = ''
for item in range(len(collection)):
    pass_string += random.choice(collection[item])
    
if len(pass_string) != n:
    pass_string += random.choice(collection[0])

print(pass_string)
