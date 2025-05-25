#Welcome to KGupta learning sesssion!

#If you wanna to use or test the code so please uncomment out the code topic and enjoy the code!

#like just remove the "#"  symbol and run it 


# print("Welcome to KGupta Learning tutorial!")              #remove the comment(#) section from starting and run















#Comments in python

#1.  #This is a comment
#2.  """" This is also a comment"""








# #                     #Print command in python

                    # #Just normal print command

# print("Hello World")












# # int, str, float   explian


# a = float(input())

# a= int(input())

# a= str(input())





                # #also do normal calculations
# print(2+3)
# print(2-3)
# print(2*3)
# print(2/3)












# # usage of dictionary


# #1st explain
# dic={"a":56,"d":56,74:"f"}
# for key,value in dic.items():
#     print(value)




# # 2st explain

# print("a")
# print(dic[45])




# #3st explain

# dic={"a":56,"d":56,74:"f"}
# for key,value in dic.items():
#     print(value)


# #4st explain

# for i in dic:
#     print(i)




# #5st explain

# dic={"a":56,"d":56,74:"f"}

# print(dic["a"],dic["d"],dic[74])















# # Using of if elif else

# a=int(input("Enter: "))
# b=int(input("Enter: "))
# opr=str(input("Enter: "))
# if("+"==opr):
#     print(a+b)
# elif("-"==opr):
#     print(a-b)
# elif("*"==opr):
#     print(a*b)
# elif("/"==opr):
#     print(a/b) 
# else:
#     print("default")
  



# """
# Difference or comparision b/w Pyhton and C++ if else, if else if   &    if elif else

# cout<<"Enter: ";
# cin>>a;
# cout<<"Enter: ";
# cin>>b;
# cout<<"Enter: ";
# cin>>opr;
# if("+"==opr){
#     print(a+b)}
# else if("-"==opr){
#     print(a-b)}
# else if("*"==opr){
#     print(a*b)}
# else if("/"==opr){
#     print(a/b)}
# else{cout<<"not"}

# """

















# # #                     #Modules in python

                # #Module like flask,django,pyjokes,pandas,requests


# #pip install flask
# #pip install django
# #pip install pyjokes
# #pip install pandas
# #usage in code
# import pyjokes      # print a random joke
# print(pyjokes.get_joke())

# # import requests and libraryname













# #                       Loops:- for, while

# # For loop example
# for i in range(1, 6):
#     print(f"For loop: {i}")





# # While loop example
# count = 1
# while count <= 5:
#     print(f"While loop: {count}")
#     count += 1















# #                       Nested Loops

# # Nested for loop example
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"for-for: i={i}, j={j}")











# # Nested while loop example
# i = 1
# while i <= 3:
#     j = 1
#     while j <= 3:
#         print(f"while-while: i={i}, j={j}")
#         j += 1
#     i += 1










# # #                     #Functions in python



"""
Two types of functions
1. Built in functions
2. User defined functions
Built in functions are those which are already defined in python
User defined functions are those which are defined by user

"""




# # usage of function
  
# def func():
# 	print("heifn")
  
# func()
  

# """
# #ERROR due to indentation
# def func():
	
# print("fsfe")           #they also work with the indentation
# func()


# """














# #                     #Built in functions




#                     # Functions 


# a = 12 
# b= 45
# c= 32
# average = (a+b+c)/3
# print(average)


# a = 12 
# b= 45
# c= 32
# average = (a+b+c)/3
# print(average)



# #                     #so we use here functions


# def avg():       #Function definition
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = int(input("Enter third number: "))

#     average = (a+b+c)/3
#     print(average)


# avg()
# avg()         #Function calling
# avg()


                            #OR WE ALSO USE FUNCTION WITH return as




# def average(a,b,c):
#     return (a+b+c)/3
# a = 12
# b= 45  
# c= 32

# print(average(a,b,c))
# print(average(a,b,c))
# print(average(a,b,c))
# print(average(a,b,c))



# #So here we use functions as we want to calculate average of 3 numbers





# #                     #User defined functions


#                               RECURSION
# #Recursion is a process in which a function calls itself directly or indirectly.



"""

factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1

factorial(n) = n x n-1 x....2 x 1

factorial(n) = n x factorial(n-1)



                                    
                                        OR

                                        


factorial(1) = 1
factorial(2) = 2 * factorial(1) = 2 * 1 = 2 
factorial(3) = 3 * factorial(2) = 3 * 2 * factorial(1) = 3 * 2 * 1 = 6
factorial(4) = 4 * factorial(3) = 4 * 3 * factorial(2) = 4 * 3 * 2 * factorial(1) = 4 * 3 * 2 * 1 = 24
factorial(5) = 5 * factorial(4) = 5 * 4 * factorial(3) = 5 * 4 * 3 * factorial(2) = 5 * 4 * 3 * 2 * factorial(1) = 5 * 4 * 3 * 2 * 1 = 120




1. Basically the end condition is when n = 1
   and the function will return 1

2. and function will call itself with n-1

3. and the function will return n * factorial(n-1)

"""



# def factorial(n):
#     if n > 1 :
#         return n * factorial(n-1)
#     else:
#         return 1
    
# n = int(input("Enter a number: "))
# print(factorial(n))


                            #OR 


# def factorial(n):

#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    

# n = int(input("Enter a number: "))
# print(factorial(n))
















# # #                     #Data types in python




# # #1. int

# a = int(input("Enter a number: "))
# print(a)
#                      #OR
# a = 12
# print(a)




# # #2. float

# b = float(input("Enter a float number: "))
# print(b)

        
#                      #OR
# b = 12.34
# print(b)






# # #3. str

# c = str(input("Enter a string: "))
# print(c)        

#                      #OR
# c = "Hello World"
# print(c)




# # #4. list

# d = list(input("Enter a list: "))
# print(d)


#             #OR

# d = [1,2,3,4,5]
# print(d)




# # #5. tuple

# e = tuple(input("Enter a tuple: "))
# print(e)

#                    #OR



# e = (1,2,3,4,5)
# print(e)





# # #6. set

# f = set(input("Enter a set: "))
# print(f)

#                    #OR  

# f = {1,2,3,4,5}
# print(f)



# # #7. dict

# g = dict(input("Enter a dict: "))
# print(g)

#                    #OR  

# g = {'name': 'John', 'age': 30, 'city': 'New York'}
# print(g)




# # #8. bool
# h = bool(input("Enter a bool: "))
# print(h)

#                    #OR  
# h = True
# print(h)



# # #9. complex
# i = complex(input("Enter a complex number: "))
# print(i)

#                    #OR 
# i = 1 + 2j
# print(i)




# # #10. None
# j = None
# print(j)

#                    #OR 
# j = None
# print(j)














#                           #OOP in python
# # #                     #Classes and objects

# class Dog:



#     def __init__(self,name,age):  #Constructor           
#        self.name = name
#        self.age = age
#        print("Woof! Woof!")

#     def bark(self):  #Method
#         print(f"{self.name} is barking!")
    
#     def get_name(self):   
#         return self.name

#     def get_age(self):
#         return self.age
    
#     @staticmethod
#     def static_method():
#         print("This is a static method.")


#     @classmethod
#     def class_method(cls):
#         print("This is a class method.")
        


# # dog = Dog()  # Removed because it causes an error due to missing arguments:- self, name and age



# dog = Dog("Buddy", 3)  #Creating an object of the class and passing arguments to the constructor
# dog.bark()  #Accessing the attributes of the object
# print(dog.get_name())  #Accessing the attributes of the object
# print(dog.get_age())   #Accessing the attributes of the object
# dog.static_method()  #Calling the static method
# dog.class_method()   #Calling the class method


  

# # dog = Dog()  #Creating an object of the class and passing
# # dog.name = "Buddy"  #Accessing the attributes of the object
# # dog.age = 3  #Accessing the attributes of the object
# # print(dog.name,dog.age)















# #                     #Inheritance
## Inheritance is a mechanism in object-oriented programming that allows a new class (child class) to inherit

# class Animal:

#     # a_name = "Animal"


#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Animal speaks")
#     def get_name(self):
#         return self.name
#     def set_name(self, name):
#         self.name = name
#     def __str__(self): 
#         return f"Animal name: {self.name}"
#     def __repr__(self):
#         return f"Animal({self.name})"



# class Dog(Animal):

#     # d_name = "Dog"

#     def __init__(self, name, breed):
#         super().__init__(name)  # Call the constructor of the parent class      
#         #super() is used to call the parent class constructor
#         self.breed = breed

#     def speak(self):
#         print("Woof! Woof!")

#     def get_breed(self):
#         return self.breed

#     def set_breed(self, breed):
#         self.breed = breed

#     def __str__(self):
#         return f"Dog name: {self.name}, breed: {self.breed}"
    
#     def __repr__(self):
#         return f"Dog({self.name}, {self.breed})"



# # Print the name of the animal and its speak method from Animal, but via the Dog class
# dog = Dog("Max", "Labrador")
# print(dog.get_name())
# super(Dog, dog).speak()  # Calls Animal's speak method via Dog instance




# # Example usage
# dog = Dog()  
# print(dog.a_name,dog.d_name)









# # Multiple Inheritance


# class Employee:
    
#     a = 1

# class Programmer(Employee):
   
#     b = 2

# class Manager(Programmer):
 
#     c = 3

# #  Example usage
# empl = Employee()  
# print(empl.a)


# # Example usage
# prog = Programmer()
# print(prog.a, prog.b)  # Accessing attributes from both Employee and Programmer classes

# # Example usage
# manager = Manager()
# print(manager.a, manager.b, manager.c)  # Accessing attributes from both Employee and Manager classes







# # super()

# class Employee:
#     def __init__(self):
#         print(f"Constructor of Employee ")
    
#     a = 1

# class Programmer(Employee):
#     def __init__(self):
#         super().__init__()  # Call the constructor of the parent class
#         print(f"Constructor of Programmer")
    
#     b = 2

# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()  # Call the constructor of the parent class
#         print(f"Constructor of Manager")
    
#     c = 3


# # # Example usage
# # empl = Employee()
# # print(empl.a)  # Accessing attribute from Employee class

# # # Example usage
# # prog = Programmer()
# # print(prog.a, prog.b)  # Accessing attributes from both Employee and Programmer classes

# # # Example usage
# # manager = Manager()
# # print(manager.a, manager.b, manager.c)  # Accessing attributes from Employee, Programmer, and Manager classes







# # @classmethod


# class Employee:
#     company = "TechCorp"
#     @classmethod
#     def show(cls):
#         print(f"Company: {cls.company}")

# # Example usage
# empl = Employee()
# empl.company =  "Tech Innovations"  # Changing the company name for this instance   B'z it always prefer first instance 
# # empl.show()  # Output: Company: Tech Innovations without using class method


# # but here we want to show the stored company name  so for that we use class method
# empl.show()  # Output: Company: Tech Corp








# # @proeperty, @name.setter, getter, setter


# class employee:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"The class attribute is {cls.a}")

#     @property           #After the property always add on setter
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name(self, value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1] 
    

# e = employee()
# e.a = 34
# e.show()

# e.name = "Rohan Gupta"
# print(e.lname)








# # #                     Operator overloading
# # # Operator overloading allows us to define how operators behave for user-defined classes.

# class Number:
#     def __init__(self,n):
#         self.n = n

#     def __add__(self, num):
#         return self.n + num.n

# number1 = Number(2)
# number2 = Number(4)

# print(number1 + number2)












# # #                     #Polymorphism
# #Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same method name.


# class Animal:
#     def speak(self):
#         print("Animal speaks")
    
#     def eat(self):
#         print("Animal eats")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
    
#     def eat(self):
#         print("Dog eats")


# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")
    
#     def eat(self):
#         print("Cat eats")

# def animal_sound(animal):
#     animal.speak()  # Calls the speak method of the specific animal type
#     animal.eat()    # Calls the eat method of the specific animal type

# dog = Dog()
# cat = Cat()
# animal_sound(dog)  # Output: Dog barks
# animal_sound(cat)  # Output: Cat meows
# # Using polymorphism to call the same method on different objects
# # This allows us to treat different animal types uniformly
# # without needing to know their specific types at compile time.
# # This is a key feature of polymorphism in object-oriented programming.













# # #                        #Encapsulation  
# # Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit, or class.


# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew: {amount}. New balance: {self.__balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")

#     def get_balance(self):
#         return self.__balance

#     def get_account_number(self):
#         return self.__account_number

#     def __str__(self):
#         return f"BankAccount(account_number={self.__account_number}, balance={self.__balance})"

#     def __repr__(self):
#         return f"BankAccount({self.__account_number}, {self.__balance})"


# # # Example usage
# account = BankAccount("123456789") # Creating a new bank account
# account.deposit(1000)  # Depositing money
# account.withdraw(500)  # Withdrawing money
# print(f"Account Number: {account.get_account_number()}")  # Accessing account number
# print(f"Balance: {account.get_balance()}")  # Accessing balance
# print(account)  # Calling the __str__ method
# print(repr(account))  # Calling the __repr__ method
# # print(account.__dict__)  # Accessing the attributes of the object (note: private attributes are name-mangled)
# # print(account.__class__)  # Accessing the class of the object
# # print(account.__class__.__name__)  # Accessing the name of the class
# # print(account.__class__.__bases__)  # Accessing the bases of the class
# # print(account.__class__.__module__)  # Accessing the module of the class
# # # To access private attributes directly, use name mangling:
# # print(account._BankAccount__account_number)  # Accessing the private account number
# # print(account._BankAccount__balance)         # Accessing the private balance
# # print(account.__class__.__dict__)  # Accessing the attributes of the class













# # #                     #Abstraction
# ## Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object.



# class Shape:
#     def area(self):
#         pass  # Abstract method, to be implemented by subclasses

#     def perimeter(self):
#         pass  # Abstract method, to be implemented by subclasses

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# # Example usage
# rectangle = Rectangle(5, 10)  # Creating a rectangle object
# print(f"Rectangle Area: {rectangle.area()}")  # Calculating area
# print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Calculating perimeter
# circle = Circle(7)  # Creating a circle object
# print(f"Circle Area: {circle.area()}")  # Calculating area
# print(f"Circle Perimeter: {circle.perimeter()}")  # Calculating perimeter
# # This code demonstrates abstraction by defining an abstract class `Shape` with abstract methods `area` and `perimeter`.
# # The subclasses `Rectangle` and `Circle` implement these methods, providing specific behavior for each shape type.
# # This allows us to work with different shapes uniformly, without needing to know their specific implementations.
# # The `Shape` class serves as a blueprint for all shapes, ensuring that any shape must implement the `area` and `perimeter` methods.


# # #                     #Modules and Packages
# # A module is a file containing Python code, which can define functions, classes, and variables.
# # A package is a collection of modules in directories that give a package hierarchy.

# import math
# from math import pi
# import requests




# # Example 1: Importing a built-in module
# print(math.sqrt(16))  # Output: 4.0



# # Example 2: Importing a specific function from a module
# print(pi)  # Output: 3.141592653589793



# # Example 3: Creating and importing your own module
# # Suppose you have a file named mymodule.py with the following content:
# # def greet(name):
# #     print(f"Hello, {name}!")
# #
# # You can import and use it as follows:
# # import mymodule
# # mymodule.greet("Alice")  # Output: Hello, Alice!



# # Example 4: Using a package (a folder with __init__.py and modules inside)
# # Directory structure:
# # mypackage/
# #   __init__.py
# #   module1.py
# #   module2.py
# #
# # In your script:
# # from mypackage import module1
# # module1.some_function()



# # Example 5: Installing and using external packages
# # Use pip to install: pip install requests
# response = requests.get("https://api.github.com")
# print(response.status_code)  # Output: 200

# # Summary:
# # - Use 'import module' to import a module.
# # - Use 'from module import something' to import specific items.
# # - Packages organize modules in directories.
# # - Use pip to install third-party packages.



