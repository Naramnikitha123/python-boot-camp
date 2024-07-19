#Arithmetic operators
#a = int(input())
#b = int(input())
#a=13
#b=4  #it is not round figuring or it will remove values after decimal
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(a%b)
#print(a**b) #power
#print(a//b) 
#logical operators
'''
age=int(input())
if(age>=18 and age<24):
    print("Only two wheeler")
elif(age>24 and age<45):
    print("Two and four wheeler")
else:
    print("All")

'''
'''
x goes to market he will buy 10 apples,2 dozen bananas and he will buy 8 oranges the cost of each apple is?
1 apple=15
1 banana=4
1 orange=5
'''
'''
apple=int(input())
banana=int(input())
orange=int(input())
apple=apple*15
banana=banana*4
orange=orange*5
cost=apple+banana+orange
print(cost)
if(cost<700):
    print("x is not cheated")
else:
    '''
'''
    print("x is cheated")
    cost_apples=15
    cost_banana=4
    cost_orange=5
    #no of fruits
    print("enter on of apples")
    no_apples=int(input())
    print("enter no of bananas")
    no_bananas=int(input())
    print("enter no of oranges")
    no_bananas=int(input())
    t("enter the amount given by mother")
    amount_given=int(input())
    sum=(no_apples*cost_apple)*(no_bananas*cost_bananas)*(no_oranges*cost_orange)
    '''
'''
a=int(input())
if(a%2==0 and a>=0):
    print("positive even number")
elif(a%2!=0 and a<0):
    print("Negative odd number")
elif(a%2==0 and a>=0):
    print("positive even number")
else:
    print("Negative odd number")
   
   '''
#mr.z selected for olympic he is participated for selecting compition only 1 winner is selected mr.x and mr.y are friends of z and mr.x is participating in badminton and mr.y is participating to the selection committee the requirements for badminton players are height:140cms,weight factors of 2 body fat is less than 12%
#according to the selection comitte requirements for criteria for table tennins are height minimum 118cms to 148cms weight factors of no of medals won by mr.z body fat 14% according to the previous history z participation in 14 years how of which he is having success rate of 65%
#write  program to check whether mr.x mr.y and mr.z from India travel in a same place or not.
'''
z=True
h1=int(input())
w1=int(input())
body_fat1=int(input())
if(h1>140 and w1%2==0 and body_fat1<12):
    print("x is selected")
    x=True
h2=int(input())
w2=int(input())
body_fat2=int(input())
if((h2>=118 and h2<=148) and w2%7==0 and body_fat2<14):
    print("y is selected")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   selected")
    y=True
if(x==True and y==True and z==True):
    print("All three are travelling in same plane")
else:
    print("No")
    '''
#check whether given number is palindrome or not
'''
n = input("enter the value:")
reverse = n[::-1]
if(n == reverse):
    print("yes it is a palindrome")
else:
   print("no it is not a palindrome")
   '''
#Armstrong number
'''
a=int(input())
sum=0
rem=0
while(n>0):
rem=a%10
a = a / 10
sum=sum+rem+rem+rem
return sum=original
'''
'''
#first n natural numbers
n=int(input())
sum=0
 while(n>0):
print(i)
i=i+1
#friendly numbers
   '''
'''''
x=int(input())
y=int(input())
sum1=0
sum2=0
for i in range(1,x):
    if(x%i==0):
        sum1=sum1+i
for j in range(1,y):
        if(y%j==0):
          sum2=sum2+j
if(sum1==y and sum2==x):
            print("friendly number")    
else:
            print("not friendly number")
    '''
#check whether given num is armstrong or not
'''
n=int(input())
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit*digit*digit
    temp=temp//10
if sum==n:
    print("it is an Armstrong number")
else:
    print("it is not a Armstrong number")
    '''
'''
n=int(input())
sum=0
for i in range(1,n):
    sum=sum+i
print(sum)
'''
n=int(input())
sum=0
print(n*(n+1)//2)

