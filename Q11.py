#print the particular element  present in k index
list=list(map(int,input().split(" ")))
k=int(input())
for i in range(0,len(list)):
    rem=k%(len(list))
print(list[rem])