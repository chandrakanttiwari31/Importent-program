# This Program Which Calculate The Factorial Of Given Number

int_a=int(input("Enter Your Number"))
fct=1
for i in range(2,int_a+1):
    fct=fct*i
print(f"Your Calculated FActorial is {fct}")
