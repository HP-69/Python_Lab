n=int(input())
s=str(n)
sum=0
for i in s:
    sum=sum + pow(int(i),3)
if(sum==n):
    print("armstrong number")
else:
    print("not")