#making a password strength checker for my first cybersecurity program using python

import time
import string
print("create a password here")
time.sleep(.25)                  # added delay so the program output will look good
a = input("type your password:")
passw = a
hasuppercase = any(a.isupper() for a in passw)
haslowercase = any(a.islower() for a in passw)
hasdigit = any(a.isdigit() for a in passw)
hassymbols = any(a in string.punctuation for a in passw)
checklength = len(passw) >=8
if hasuppercase and haslowercase and hasdigit and hassymbols and checklength:
    print("password is has been created")
else:
    if not hasuppercase:
        print("capital letter is not included")
    if not haslowercase:
        print("lowercase letter is not included")
    if not hasdigit:
        print("digit is not included")
    if not hassymbols:
        print("symbols is not included")
    if not checklength:
        print("password length is short")








