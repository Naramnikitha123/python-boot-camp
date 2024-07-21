#print the sum of the even numbers
'''''''
n=int(input())
sum=0
while n>0:
    r=n%10
    if(n%2==0):
     sum=sum+r
    n=n//10
print(sum)


#reverse of a number
n=1234
rev=""
while n>0:
   r=n%10 #extracting digit
   rev=rev+str(r)
   n=n//10
ans=int(rev) # changing rev into integer and storing ans
print(ans)
print(type(ans))