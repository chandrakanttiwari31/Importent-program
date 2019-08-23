# This Program  Calculate The Armstrong which Values Given By User

int_a=int(input("Enter your Number"))
sum=0
rem=int_a
while(rem!=0):
    sum=sum+(rem%10)**3
    rem=rem//10
if(sum==int_a):
    print(f"The  Number {int_a} is a Armstrong ")
else:
    print(f"The Number {int_a} is not Armstrong Number")