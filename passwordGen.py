# password generator
# -*- coding: utf-8 -*-

import random
import string

# number list 
number_list = [x for x in range(0, 10)]

# alphabet list
lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

# punctuation lisst
punction_list = list(string.punctuation)

# code length
code_length = int(input("Set up the length of your code: "))

# code
code_list = []

# generate your code
print(" ")
print("Processing...")
while True:
    if len(code_list) < code_length:
        random_number = random.randint(1,4)
        # print(random_number)
        if random_number == 1:
            random_code = random.randint(0, len(number_list))
            code_list.append(number_list[random_code])
        elif random_number == 2:
            random_code = random.randint(0, len(lower_alphabet))
            code_list.append(lower_alphabet[random_code])
        elif random_number == 3:
            random_code = random.randint(0, len(upper_alphabet))
            code_list.append(upper_alphabet[random_code])
        else:
            random_code = random.randint(0, len(punction_list))
            code_list.append(punction_list[random_code])
    else:
        break

# your code
your_code =  "".join(map(str, code_list))
print("Your code is: ")
print(your_code)
