n=int(input())
s=str(n)
t=0
for i in range(1,len(s)+1):
    r=n%10
    t=t*10+r
    n=n/10
    if(r==0):
        break
if(t==n):
    print("palindrome")
else:
    print("not")