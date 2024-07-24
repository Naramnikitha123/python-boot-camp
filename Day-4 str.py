#converting to uppercase
#input="Hello"
#print(input.upper())

#converting to lowercase
#input="Hello"
#print(input.lower())

#converting to titlecase
#input="Hello"
#print(input.title())

#converting swappingcase
#input="Hello"
#print(input.swapcase())

#converting to replace 
#input="Nikitha"
#print(input.replace('a','z'))

#converting to replace 
#input="   helloworld    " #it trims  the spaces beginning and ending
#print(input.strip())

#converting to replace 
#input="helloworld"
#print(input.split())

#converting to alphanumeric
#input="hello world"
#print(input.isalpha())

#converting to numeric
#input="123"
#print(input.isnumeric()) #storing numerics in strings

#converting to numeric
#input="Helloworld123"#spaces not allowed
#print(input.isalnum())

#converting to numeric
#input="Helloworld123"#spaces not allowed

#converting is acii
#input="hello world"
#print(input.isascii())

#taking same input to all
#input="hello world"
#input="HELLO WORLD"
#input="12344"
#print(input.isdigit())
#print(input.istitle())
#print(input.isupper())
#print(input.islower())
#print(input.isdigit())

#converting to ascii
#print(ord('A'))
#print(ord('a'))
#print(ord('0'))
#print(chr(60))

#check how many vowels are in a string
'''
check=['a','e','i','o','u']
count=0
input="hello world"
for i in input:
    if(i in check):
        count+=1
print(count)
'''
#write a program to print the vowels and consonents
'''
vowel="aeiou"
consonent="gsdghjhlklswklj"
count=0
c=0
l=input()
inp=l.lower()
for i in input:
 if(i in vowels):
      count+=1
for i in input:
 if(i in consonants):
   c+=1
print(count)
print(c)
'''

#write a program to print only consonants
''''
input="hello world"
vowel="aeiou"
consonents="bcwshkjjhihgb"
count=0
#input="helloworld"
for i in input:
    if(i in consonents):
        count+=1
print(count)
'''''

#print all the vowels followed by consonents
'''
str=input()
l=str.lower()
str1=""
str2=""
vowels="aeiou"
consonants="sfdfghgjhlik"
for i in l:
  if(i in vowels):
    str1+=i
    for i in l:
      if(i in consonants):
        str2+=i
        print(str1+str2)
        
'''



#printing lower and upper cases
''''
check=['a','e','i','o','u']
count=0
i="hello world"
input=i.lower()
for i in input:
    if(i in check):
        count+=1
print(count)
'''''
'''''
check=['a','e','i','o','u']
count=0
i="hello world"
input=i.upper()
for i in input:
    if(i in check):
        count+=1
print(count)
'''''

#print the non repeating characters in a string or print the given characters in a string #printing char only once in a string
'''''
vowel="aeiou"
consonent="dfjhjksdak"
ans=" "
i="hello world"
input=i.lower()
for i in input:
    if(i not in ans): #not printing repeatation
       ans+=i #incrementing the values
print(ans)
'''''
#printing the sum of numbers in a given string
#helloworld1,2,3     #helloworld
'''''
vowel="aeiou"
consonent="dfjhjksdak"
check="123456789"
ans=0
i="hello 1234 world"
input=i.lower()
for i in input:
    if(i in check): #not printing repeatation
       ans+=int(i) #incrementing the values
print(ans)
'''''


#(HW)reverse the numbers in a given string
n=int(input())
for i in n:
   n=ord(i)+4
   if n<=122:
      print(chr(n),end="")
   else:
      print(chr(n-26),end=" ")

''''
str="Nikitha"
a=str.isupper()
b=str.islower()
c=str.isalpha()
d=str.isdigit()
e=str.lower()
f=str.upper()
g=str.title()


print("isupper is",a)
print("islower is",b)
print("isalpha is",c)
print("isdigit is",d)
print("upper is",e)
print("lower is",f)
print("title is",g)
'''