# #WAP using func to find greatest of 3 numbers

# def great(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
    
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print("Greatest number is: ",great(a,b,c))











# #WAP using func to convert celsius to fahrenheit

# #c/5 = (f-32)/9
# #c = 5*(f-32)/9


# def C_t_F(f):
#     return (5*((f-32)/9))

# f = int(input("Enter temperature in fahrenheit: "))
# print("Temperature in celsius is: ",C_t_F(f),end=" *C")















# #WAP of print statement using end
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello ",name," your age is ",age,end=" years!")











# #WAP class "Programmer" for storing information of few programmers working at Microsoft
# class Programmer:
#     company = "Microsoft"

#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin


# p= Programmer("John Doe", 80000, 1234)
# print(f"{p.name} work at p.company with a salary of {p.salary} and its pin is {p.pin}")


# r= Programmer("Rohan", 1200000, 3234)
# print(f"{r.name} work at p.company with a salary of {r.salary} and its pin is {r.pin}")













# #WAP class "calculator" capable of finding square, cube, square root of a number

# class Calculator:
#     def square(self,number):
#         return number ** 2 
    
#     def cube(self,number):
#         return number ** 3
    
#     def square_root(self, number):
#         return number ** 0.5
    

# calc = Calculator()
# num = int(input("Enter a number: "))
# print(f"Square of {num} is {calc.square(num)}")
# print(f"Cube of {num} is {calc.cube(num)}")
# print(f"Square Root of {num} is {calc.square_root(num)}")




















# #WAP class a it having its own value after changing the value by object.a = 10(something like that) is it change?

# class A:
#     a = 2


# o = A()
# print(o.a)  
# o.a = 12
# print(A.a)      #Here the value of a in class A remains unchanged
# print(o.a)      #While the instance value of a is changed to 12





# #Roughly
# print(A.__dict__)  #This will show the attributes of class A
# print(o.__dict__)  #This will show the attributes of instance o



















# #WAP add greet "Hello" method in class Programmer

# class Calculator:
#     @staticmethod
#     def greet():
#         print("Hello! Welcome to the Calculator Program.")


#     def square(self,number):
#         return number ** 2 
    
#     def cube(self,number):
#         return number ** 3
    
#     def square_root(self, number):
#         return number ** 0.5
    

# calc = Calculator()
# calc.greet()  
# num = int(input("Enter a number: "))
# print(f"Square of {num} is {calc.square(num)}")
# print(f"Cube of {num} is {calc.cube(num)}")
# print(f"Square Root of {num} is {calc.square_root(num)}")














# #WAP of class Train which has methods to book a ticket, getstatus(no of seats available), get fare information of running train under Indian Railways
# from random import randint

# class Train:
#     def __init__(self, name, from_station, to_station ):
#         self.name = name
#         self.from_station = from_station 
#         self.to_station = to_station
#         self.fare = randint(222,999)
#         self.seats = randint(10,100)
#         self.booked_seats = randint(0, self.seats)
#         self.available_seats = self.seats - self.booked_seats

#     def book_ticket(self, num_tickets):
#         if (num_tickets <= self.available_seats):
#             self.booked_seats += num_tickets
#             self.available_seats -= num_tickets
#             print(f"{num_tickets} tickets booked successfully!")
#         else:
#             print("Not enough seats available!")

#     def get_status(self):
#         print(f"Train Name: {self.name}")
#         print(f"From: {self.from_station} To: {self.to_station}")
#         print(f"Total Seats: {self.seats}")
#         print(f"Booked Seats: {self.booked_seats}")
#         print(f"Available Seats: {self.available_seats}")

#     def get_fare_info(self):
#         print(f"Fare from {self.from_station} to {self.to_station} is: ₹{self.fare}")
#         print("Note: Fare may vary based on availability and season.")
# # Example usage
# train = Train("Express Train", "Delhi", "Mumbai")
# train.get_status()
# train.get_fare_info()
# num_tickets = int(input("Enter number of tickets to book: "))
# train.book_ticket(num_tickets)
# train.get_status()  # Check status after booking
# train.get_fare_info()  # Check fare information
# print(f"Your total fare for {num_tickets} tickets is: ₹{train.fare * num_tickets}")


















# #WAP class(2D vector) and use it to create another class represent a 3D vector.

# class Vector2D:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"Vector2D is {self.i}i + {self.j}j")
    
# class Vector3D(Vector2D):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f"Vector3D is {self.i}i + {self.j}j + {self.k}k")
    

# a = Vector2D(3, 5)
# b = Vector3D(4, 2, 1)
    
# a.show()
# b.show()















# #Create a class "Pets" from a class "Animals" and further create a clas "Dog" from "Pets".Add a method "bark to clas "Dog". 

# class Animals: 
#     pass

# class Pets(Animals):
#     pass

# class Dog(Pets):

#     @staticmethod
#     def bark():
#         print("Woof! Woof!")



# dog = Dog()
# dog.bark()
















# #Create a class "Employee" and add salary and increament properties to it.




# class Employee:
#     def __init__(self, salary,increment):
#         self.salary = salary
#         self.increment = increment
#     def show(self):
#         print(f"The salary is {self.salary} and its increment is {self.increment}%")


# empl = Employee(12000,20)
# empl.show()

