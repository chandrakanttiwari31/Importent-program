# This Program   which Show The Number Is Palindrom Or Not

int_a=int(input("Enter your Number"))
sum=0
rem=int_a
while(rem!=0):
    sum=sum*10+(rem%10)
    rem=rem//10
if(sum==int_a):
    print(f"The  Number {int_a} is a Palindrom Number ")
else:
    print(f"The Number {int_a} is not Palindrom Number")