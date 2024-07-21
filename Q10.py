#find the elements that is  present in k+ith index 
#input:
# k is given by user k=3
#N=2
#test case-1
# The input parametrs are: 3 6 8 4 61 2 
#output:2
#test case-2
#k=3
#N=4
#80 70 54 36 72
#op=error
lst=list(map(int,input().split()))
k=int(input())
n=int(input())
c=k+n
#print(my_list[k+n],end==" ") # alteration also it wor
#break#my_list(k+1) because of the break statement
if(c>len(lst)): 
    print("error")
else:
    for i in range(0,len(lst)):
        a=(lst[c])
    print(a,end="")
