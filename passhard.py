#making a password strength checker for my first cybersecurity program using python

import time
import string
print("create a password here")
time.sleep(1)
a=input("type your password:")
passw = a  # putting the value into it
if any(char.isupper() for char in passw) and any(char.isdigit() for char in passw) and any(char in string.punctuation  for char in passw) and  len(passw) >= 8:
     print("your password has been set") #learn to use the function ,methods and operators
else:
    print(" password doesnt meet the requirements")







