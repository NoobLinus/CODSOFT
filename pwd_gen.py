#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("----Codsoft Task-2----")
print("PASSWORD GENERATOR")

# Importing libraries
import random
import string

def gen_pwd(len, use_punc=True, use_num=True):
    chars = string.ascii_letters
    if use_punc:
        chars += string.punctuation
    if use_num:
        chars += string.digits

    pwd = ''.join(random.choice(chars) for _ in range(len))
    return pwd

# Asking user for password length and character types
while True:
    len = input("Enter password length: ")

    if len.isdigit() and int(len) > 0:
        len = int(len)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

use_punc = input("Include punctuation? (yes/no): ").lower() == 'yes'
use_num = input("Include digits? (yes/no): ").lower() == 'yes'

# Generating and displaying the password
while True:
    pwd = gen_pwd(len, use_punc, use_num)
    print("Generated Password:", pwd)
    
    satisfied = input("Satisfied with the password? (yes/no): ").lower()
    
    if satisfied == 'yes':
        break


# In[ ]:




