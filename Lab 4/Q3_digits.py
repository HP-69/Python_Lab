s=input()
str(s)
length=len(s)
count=0
for i in s:
    if(i==' '):
        count=count + 1
print("number of the digits",length-count)