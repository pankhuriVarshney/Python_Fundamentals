n=int(input("Enter a number: "))
n1=n
bnum=[]
while(n>0):
    bnum.insert(0,n%2)
    n//=2
print(bnum)

for x in range(len(bnum)):
    n+=(bnum[x]*(2**(len(bnum)-x-1)))
print (n)