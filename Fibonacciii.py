# This Program   which Calculate the Fibonacci Series

int_a=int(input("Enter your Number"))
prev=0
nextt=1
print(f"the fibonaci series From  is {prev}  {nextt}",end="")

for i in range(1,int_a-1):
    b=prev+nextt
    print(b,end=" ")
    prev=nextt
    nextt=b
