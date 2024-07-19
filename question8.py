#given an space separated integer list find the average of elements present in the even index
my_list=list(map(int,input().split()))
#even=0
sum=0
count=0
n=len(my_list)
for i in range(len(my_list)):
    #if(i%2==0): 
        sum+=my_list[i]
        count+=1
    #avg=sum//even
print(sum/count)
'''''
my_list=list(map(int,input().split()))
even=0
sum=0
for i in range(0,len(my_list)):
'''''''''