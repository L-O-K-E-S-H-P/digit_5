"""An integer of 5digits will be provided as input. It has to be considered as three parts,
<First_part><middle_number><second_part>
The first_part must be replaced with second part and second part replaced by first part then have to check whether it's a prime number
Input - 12345
Explanation - after interchanging position, it will be 45321. Now 45321 has to be checked whether it is a prime number
Output – Number """
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
    print(" ")
else:
    print("Number") 
