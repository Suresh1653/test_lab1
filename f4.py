import re
str1="drive name is sda sdb"
pat=r"sd[a-z]"
out=re.findall(pat,str1)
print(out)
