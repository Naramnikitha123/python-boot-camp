#7.you are given with a comma separated natural numbers 1 to 10 print only the even numbers
'''
my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):# starting for loop from index 1
  count+=1#counting the even numbers
    #if(i%2==0):
print(count)
'''''
#you are given with a space separated integer list find number of even elements and number of odd elements in a given list
my_list=list(map(int,input().split(",")))
even=0 #initialize
odd=0
for i in range(0,len(my_list)):
  if(my_list[i]%2==0):
       even+=1
  else:
       odd+=1
print(even)
print(odd)




   

 
 