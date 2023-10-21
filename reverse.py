n=input("Enter a number: ")
if(n[0]=='-'):
    n=n[1:]
    print('-',end="")
print(n[::-1])