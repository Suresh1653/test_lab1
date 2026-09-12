import re
str1="drive name is sda sdb sdc sdd sde"
pat=r"sd[a-z]"
out=re.findall(pat,str1)
print(out)
