import re

password = input("enter password: ")

if(len(password)>=8 and
   re.search("[A-Z]", password) and
   re.search("[a-z]", password) and
   re.search("[0-9]", password) and
   re.search("[@#$%^&*]", password)):
   print("strong password")
else:
   print("weak password")