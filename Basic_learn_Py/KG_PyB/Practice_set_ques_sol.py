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











# #WAP to print all even number

# for i in range(1,10):
#     if (i%2)==0:
#         print(i)
#     else:
#         continue














# # WAP to print the mmultiplication table

# # table with for loop

# # n = int(input("Enter the number of table you need: "))
# # for i in range(1,11):
# #     print(f"{n} x {i} = {n*i}")



# # table with while loop

# n = int(input("Enter the number of table you need: "))
# i = 1
# while(i<=10):
#     print(f"{n} x {i} = {n*i}")
#     i+=1









# # WAP to print table 

# n = int(input("Enter a number: "))

# table = [i*n for i in  range(1,11)]

# k = range(1,11)
# for j in table:
#    print(f"{j}")
# #    print(f"{n} x {k} = {j} " )













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













# #WAP to sum up and multiply the complex numbers

# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i 

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         # (a+bi)*(c+di) = (ac-bd) + (ad+bc)i
#         real = self.r * c2.r - self.i * c2.i
#         imag = self.r * c2.i + self.i * c2.r
#         return Complex(real, imag)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"

# # Example usage
# c1 = Complex(2, 3)
# c2 = Complex(4, 5)
# sum_result = c1 + c2
# mul_result = c1 * c2
# print(f"Sum: {sum_result}")
# print(f"Product: {mul_result}")


















# #WAP to guess a number

# import random 

# n = int(random.randint(1,101))
# num = int(input("Guess a Number:"))
# if (num!=n):
#     count = 0
#     while(num!=n):
#         num = int(input("Please again guess a number: "))
#         count += 1
#         if(num > n):
#             print(f"Higher Number!")
#         elif(num < n):
#             print(f"Lower Number!")
#         else:
#             print(f"You tried number {n} totally {count} times.")
#             break
# elif(num == n):
#     print("YOU WON!")

# else:
#     print("\tERROR!\tERROR!\tERROR!Invalid Syntax!\tERROR!\tERROR!\tERROR!")













# #WAP open the files read file, if not exist then except the error 

# try:
#     with open("file1.txt","r") as f:
#         print(f.read())

# except FileNotFoundError as e:
#     print(e)

# try:
#     with open("file2.txt","r") as f:
#         print(f.read())

# except FileNotFoundError as e:
#     print(e)

# try:
#     with open("file3.txt","r") as f:
#         print(f.read())
        
# except FileNotFoundError as e:
#     print(e)
















# #WAP to print 3rd, 5th or 7th element of a list using enumerate function

# list_name = ["Rohan", "Gupta", "is", "a", "good","programmer", "and", "a", "good", "friend"]
# i_value = [3, 5, 7]
# for index, value in enumerate(list_name):
#     if index in i_value:
#         print(f"Element at index {index} is {value}")
#     else: 
#         continue





# list_name = ["Rohan", "Gupta", "is", "a", "good","programmer", "and", "a", "good", "friend"]
# i_value = [3, 5, 7]
# for index, value in enumerate(list_name):
#     if index in i_value:
#         print(f"Element is in index {index}")
#     else: 
#         continue















# # WAP to print triangle star * like:-
# # *
# # **
# # ***
# # ****

# n =int(input())
# i =1
# while(i<=n):
#     j=1
#     while(j<=i):
#         print("*",end="")
#         j+=1
#     print()
#     i+=1


# # n = int(input("Enter: "))
# # for i in range(n):
# #     for j in range(i+1):
# #         print("*",end="")
# #     print()















# # WAP to print pattern:-

# # * * *
# # * * *
# # * * *



# # n = int(input("Enter: "))
# # i = 1
# # while(i<=n):
# #     j = 1
# #     while(j<=n):
# #         print("*",end=" ")
# #         j+=1
# #     print()
# #     i+=1

# n = int(input("Enter:"))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1
