'''
class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):                                                                                                            
        return a/b
    def mod(a,b):
        return a%b
obj1=Myclass
obj2=Myclass
obj3=Myclass
print(obj1.add(2,5))
print(obj2.sub(12,5))
print(obj3.div(23,6))
print(obj3.mod(97,6))
 '''
#constructor and destructor
#program execution starts from initialization 
class Myclass:
    def __init__(self,a,b):
      
        self.a=a
        self.b=b
        return a+b
 #class var
'''
class Myclass:   
    ins_var_add="in instance var"
    print(ins_var_add)
'''    