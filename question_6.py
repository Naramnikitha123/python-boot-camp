#Take a space separated input from a user and print alternate element
my_list=list(map(int,input().split()))#step count method
for i in range(0,len(my_list),2):
    print(my_list[i])
