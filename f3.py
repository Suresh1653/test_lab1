str1="abc bca cab cba"
str2=""
for i in str1:
    str2=i[::-1]+str2
print(str2.strip())

