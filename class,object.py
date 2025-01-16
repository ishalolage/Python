# class school:
#     def student(self):
#         print("hello")



# obj=school()
# obj.student()       

class person:
    def __init__(self,name,age):
     self.myname=name
     self.myage=age

 
p1= person("isha",20)
p2= person("shreya",20)

print("Name :",p1.myname)
print("Age :",p1.myage)
print(p2.myname)
print(p2.myage)

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def speak(self):
        pass  # Placeholder method to be overridden by child classes

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"  # Override the speak method

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!
