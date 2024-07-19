#list is immutable,ordered
#my_list=[1,2,3,4,6,9,5]
#my_list.append(999)
#my_list.insert(8000,999) #999 insert in the 0 index,insert used to insert in specific position or else insert at the last index
#print(my_list)
#print(len(my_list)) #print length of numbers
#my_list.pop(2000) #if we pop the index out of bounds or range
#my_list_2=[5,6,7,8]
#new_list=my_list+my_list_2
#new_list=my_list.copy()
#new_list.pop()
#pop
#my_list.pop(4)it deletes the element from particular position
#cnt=my_list.count(2) #it count the number of repeated elements
#print(cnt)
#my_list=[98,75,63,55,43,29,11]
#my_list.sort() # ascending and descending order #complexity:nlogn
#print(*my_list) #print original list
#print(*new_list) #output as 1 2 3 4
#print(*my_list)
#my_list=list(map(int,input().split(","))) # it prints the output without , separated
#my_list=list(map(int,input().split("@"))) #it prints output with space seprated instead of @
#my_list=list(map(str,input().split("@"))) # it prints output with space seprated instead of @
#my_list=list(map(str,input().split("@"))
#print(*my_list)
#my_list()
''''
my_list=list(map(int,input().split()))
choice=int(input())
print("enter the choice:")
print("1.append 2.pop 3.insert 4.sort")#displaying in terminal
if(choice==1):
   my_list.append(int(input()))
   print(my_list)
elif(choice==2):
   my_list.pop(4)
   print(my_list)
elif(choice==3):
   my_list.insert()
   print(my_list)
else:
   my_list.sort()
   print(my_list)

'''
'''
my_list=list(map(int,input().split()))
print(my_list[i],end=" ")
print("\n----------------")
for i in my_list:
   print(i,end=" ")
   '''''

#s="hello world"
#for i in range(len(s)):
    #print(s[i],end=" ") 
#for i in range(len(s)):
    #print(s[i],end=" ")
    #print()

#1.using for loop print 1 to 100 num?
#2.using for loop append 1 to 100 num in an empty list? 
#3.find sum of all the numbers in a list?

#for i in range(1,100+1):
  #print(i)
''''
my_list=[]
for i in range(1,100+1):
   my_list.append(i)
print(my_list)
'''
my_list=[1,2,3,4,5]
for i in range(sum(5)):
    print(sum)





   
   




 