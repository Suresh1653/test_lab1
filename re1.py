import re
str1="suresh1653@gmail.com"
pat="^[a-zA-Z0-9_+&.-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}$"
out=re.match(pat,str1)
if out:
    print("valid email")
else:
    print("invalid email")

