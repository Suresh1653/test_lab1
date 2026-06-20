d1={"a":15,"b":12}
d2={"c":25,"d":5}
d3={}
max_v=None
min_v=None
for key,value in d1.items():
    if max_v is None or value>max_v:
        max_v=value
        max_k=key
for key,value in d2.items():
    if value>max_v:
        max_v=value
        max_k=key

print(f"max key of dictionaries {max_k}")
print(f"max value of dictionaries {max_v}")

