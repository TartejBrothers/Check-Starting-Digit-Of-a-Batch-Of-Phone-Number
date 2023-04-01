lst=[]
n=int(input("Enter Number Of Elements:"))
for i in range(0,n):
    a=int(input("Enter Phone Number:"))
    lst.append(a)
for i in range(0,n):
    c=str(lst[i])
    if c[0]=="9":
        print("Numbers Starting From 9 are: ",lst[i])
