a=int(input())
def compute(x):
    for i in range(x):
        v=x*(10**i)*(x-1)
        sum=sum+v
    print(sum)
compute(a)