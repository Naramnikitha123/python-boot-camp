#single inheritance
class Animal:
    def speak():
      return "Animal is speaking"
class Dog(Animal):
   def Bark():
      return "Bow..."
class Puppy(Dog):   
   def Puppy_speak():
      return "i am happy"
obj1=Animal
print(obj1.speak())
obj2=Dog
print(obj2.Bark())
obj3=Puppy
print(obj3.Puppy_speak())
#class Puppy(Dog):
#   def puppy_speak
   