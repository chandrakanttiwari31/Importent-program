# This Program   which Show The Number is Prime Or Not

int_a=int(input("Enter your Number"))

for i in range(2,int_a+1):
    if(int_a%i==0):
        break
if(int_a==i):
    print(f"The  Number {int_a} is a Prime Number ")
else:
    print(f"The Number {int_a} is not Prime Number")