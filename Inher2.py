class Father:
    def father_speak():
        return "Father class"
class Mother:
    def mother_speak():
        return "Mother class"
class Kid:
    def kid_speak():
        return "i have properties"    
obj1=Father
print(obj1.father_speak())    
obj2=Mother
print(obj2.mother_speak())
obj3=Kid
print(obj3.kid_speak())