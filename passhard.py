#making a password strength checker for my first cybersecurity program using python

import time
print("create a password here")
time.sleep(1)
a=input("type your password:")

passw = "a"
has_capital = False
for passw in a:
         if passw.isupper():
              has_capital = True
              break
if has_capital:
             print("password is " , a)
else:
              print("entered password cant be created") # check whether the password contains capital letter


