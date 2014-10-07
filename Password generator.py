#Ryan Cox
#05/10/14
#Password creator

import string
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random

passwordLength = int(input("Hello, please enter the number of charcaters you would like to use for your password: "))

print("your password is: ")
for passwordLength in range(passwordLength):
    print(random.choice(string.ascii_letters)) 

