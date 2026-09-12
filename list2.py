l1=[10,20,36,71,49,26]
#sorting
for i in range(len(l1)):
    for j in range(len(l1)-1-i):
        if l1[j]<l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)

#maxvalue,minvalue

max_v=l1[0]
min_v=l1[0]

for i in l1:
    if i>max_v:
        max_v=i
for i in l1:
    if i<max_v:
        min_v=i
print(f"max number {max_v}")
print(f"min number {min_v}")





