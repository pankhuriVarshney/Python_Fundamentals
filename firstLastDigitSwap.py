n=input("Enter a number:")
first=n[0]
last=n[len(n)-1]
num=last+n[1:len(n)-1]+first
print(int(num))
