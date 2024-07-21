#replace the elements in an array with the average of max and min elements
my_list=list(map(int,input().split()))
maxi=0
mini=0
for i in range(0,len(my_list)):
    if(my_list[i]>maxi):
      maxi=my_list[i]
    if(my_list[i]<mini):
      mini=my_list[i]
print(maxi)
print(mini)
for i in range(0,len(my_list)):
    avg=(maxi+mini)/2
    my_list[i]=avg
print(my_list)
      