l1=[11,10,5,3,8,17,14,1]
def prime_num(l1):
    for i in l1:
        if i==1:
            print(f"{i} is not prime")
            continue
        for j in range(2,i):
            if i%j==0:
                print(f"{i} is not prime")
                break
        else:
            print(f"{i} is prime")
l1=[11,10,5,3,8,17,14,1]

prime_num(l1)





