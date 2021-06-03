a=int(input())
res=[int(x) for x in str(a)] 
print(res)
t1=res[0]
t2=res[1]
t3=res[2]
t4=res[3]
t5=res[4]
l=[]
l.append(t4)
l.append(t5)
l.append(t3)
l.append(t2)
l.append(t1)
strings=[str(l) for l in l]
a_string="".join(strings)
an_integer=int(a_string)
num=an_integer
flag=False
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
a=int(input())
res=[int(x) for x in str(a)] 
print(res)
t1=res[0]
t2=res[1]
t3=res[2]
t4=res[3]
t5=res[4]
l=[]
l.append(t4)
l.append(t5)
l.append(t3)
l.append(t2)
l.append(t1)
strings=[str(l) for l in l]
a_string="".join(strings)
an_integer=int(a_string)
num=an_integer
flag=False
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number") 
