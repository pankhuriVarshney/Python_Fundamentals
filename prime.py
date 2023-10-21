n=int(input("Enter a number: "))
for x in range(2,n):
    if(n%x==0):
        print("It is not a prime number")
        break
else:
    print("It is a prime number")