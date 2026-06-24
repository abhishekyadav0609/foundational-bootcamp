### Unit Converter
##
###print("1. Kilometer to Meter")
##print("2. Liter to Milliliter")
##
##choice = int(input("Enter your choice: "))
##
##if choice == 1:
##    km = float(input("Enter kilometers: "))
##    meter = km * 1000
##    print("Meters =", meter)
##
##elif choice == 2:
##    liter = float(input("Enter liters: "))
##    milliliter = liter * 1000
##    print("Milliliters =", milliliter)
##
##else:
##    print("Invalid Choice")

# Read an integer from the user
#num = int(input("Enter an integer: "))

# Check the value
##if num > 0:
##    print("Positive")
##elif num < 0:
##    print("Negative")
##else:
##    print("Zero")
# Read year from the user
#year = int(input("Enter a year: "))

# Check for leap year
# Read year from the user
#year = int(input("Enter a year: "))

# Check for leap year
##if (year % 400 == 0):
##    print(year, "is a leap year.")
##elif (year % 100 == 0):
##    print(year, "is not a leap year.")
##elif (year % 4 == 0):
##    print(year, "is a leap year.")
##else:
##    print(year, "is not a leap year.")
##pin = int(input("Enter your 4-digit PIN: "))
##
##if pin == 1234:
##    print("PIN accepted. Access granted.")
##
##    amount = float(input("Enter amount to withdraw: "))
##
##    if amount <= 5000:
##        print("Dispensing amount")
##    else:
##        print("Amount exceeds limit")
##
##else:
##    print("Invalid PIN. Access denied.")

# Temperature Adviser Program
##
##temp = float(input("Enter temperature in Celsius: "))
##
##if temp < 0:
##    print("Wear a heavy coat.")
##elif 0 <= temp <= 15:
##    print("Wear a jacket.")
##elif 16 <= temp <= 30:
##    print("Comfortable weather.")
##else:  # temp > 30
##    print("Wear light clothing and stay hydrated.")


# Loan Eligibility Checker

##income = float(input("Enter your monthly income: "))
##emi = float(input("Enter your existing EMI: "))
##
##if income < 30000:
##    print("Not eligible for loan.")
##    print("Reason: Income too low.")
##elif emi > 0.4 * income:
##    print("Not eligible for loan.")
##    print("Reason: High debt burden.")
##else:
##    print("Eligible for loan.")

# Student Performance Classification
##
##marks = float(input("Enter student's marks: "))
##
##if marks > 40:
##    print("Result: Pass")
##
##    if marks > 90:
##        print("Grade: Distinction")
##    elif marks > 75:
##        print("Grade: First Division")
##    elif marks > 60:
##        print("Grade: Second Division")
##    else:
##        print("Grade: Third Division")
##else:
##    print("Result: Fail")

# Job Application Screener

##age = int(input("Enter your age: "))
##degree = input("Enter your degree (B.Tech/MCA): ")
##cgpa = float(input("Enter your CGPA: "))
##
##if 21 <= age <= 40:
##    if degree.lower() == "b.tech" or degree.lower() == "mca":
##        if cgpa > 7.0:
##            print("Interview Shortlisted")
##        else:
##            print("Rejected: CGPA must be greater than 7.0")
##    else:
##        print("Rejected: Degree must be B.Tech or MCA")
##else:
##    print("Rejected: Age must be between 21 and 40")

##    total_amount = float(input("Enter the total amount: "))
##
##if total_amount > 5000:
##    discount = total_amount * 0.15
##    print("You get a 15% discount of", discount)
##    premium_member = input("Are you a premium member? (yes/no): ")
##
##    if premium_member == "yes":
##        additional_discount = total_amount * 0.05
##        print("As a premium member, you get an additional 5% discount of", additional_discount)
##        
##
##if total_amount <= 5000:
##    discount = total_amount * 0.05
####    print("You get a 5% discount of", discount)
##def grade(m,max_marks=100):
##    print(f"You scored {m}/{max_marks}")
##    percentage = (m/max_marks)*100
##    print(f"percentage : {percentage:.2f}")
##    
##    if 90<=m<=100:
##        grade,cgpa,remarks="A+",10,"Exceptional"
##    elif 80<=m<=89:
##        grade,cgpa,remarks="A",9,"Excellent"
##    elif 70<=m<=79:
##        grade,cgpa,remarks="B+",8,"Very Good"
##    elif 60<=m<=69:
##        grade,cgpa,remarks="B",7,"Good"
##    elif 50<=m<=59:
##        grade,cgpa,remarks="C",6,"Avaerage"
##    else:
##        grade,cgpa,remarks="D",4,"Fail"
##
##    print(f"Your Score : grade {grade},cgpa {cgpa} and your performance is {remarks}.")
##m = int(input("Enter your marks : "))
##grade(m)

#include <stdio.h>

##include <stdio.h>

#include <stdio.h>

#include <stdio.h>
#include <stdio.h>

##int main() {
##    int a, b;
##
##    printf("Enter two numbers: ");
##    scanf("%d %d", &a, &b);
##
##    if (a > b)
##        printf("Maximum number = %d\n", a);
##    else
##        printf("Maximum number = %d\n", b);
##
##    return 0;
##}\
##n = int(input("Enter a number: "))
##
##if n % 2 != 0:
##    n = n + 7
##else:
##    n = n + 4
##
##print("Result =", n)


#import random
##
##secret_number = random.randint(1, 10)
##
##guess = int(input("Guess a number between 1 and 10: "))
##
##if guess == secret_number:
##    print("Congratulations! You guessed correctly.")
##else:
##    print("Sorry! The correct number was", secret_number)

##n=5
##if n>=0:
##    if n==0:
##        print("number is 0")
##else:
##    print("number is positive")
##
##if (a>b):
##    print("a is max")
##    if(a>c):
##        print("c is max")
##    else:
##        if(b>c):
##            print("b is max")
##else:
##    print("c is max")

##num=int(input("enter a number"))
##if num>0:
##    print("number is postive")
##    if num<0:
##        print("number is negative")
##    else:
##        print("number is zero")
##

##num1=int(input("enter a number"))
##num2=int(input("enter a number"))
##num3=int(input("enter a number"))
##if num1>num2:
##    print("number is greater")
##    if num2>num3:
##        print("number2 is greater")
##        else:

##a=float(input("enter a number"))
##if a>90:
##    print("A")
##elif a>80:
##    print("B")
##elif a>70:
##    print("C")
##else:
##    print("fail")



##for i in range(1, 11):
##    for j in range(1, 11):
##        product = i * j
##        print(f"{product:4}", end="")
##    print()

##
##numbers = [2, 5, 7, 10, 12]
##
##print("SQUARED
#NUMBERS")
##
##for num in numbers:
##    squared = num ** 2
##    print(f"The square of {num} is {squared}")


##number = 1
##total_sum = 0
##
##while number <= 50:
##    total_sum += number
##    number += 2
##
##print(f"The sum of all odd numbers between 1 and 100 is: {total_sum}")


##for i in range(1, 51):
##    if i % 7 == 0:
##        continue
##    print(i)

##import random
##
##count = 0
##
##while True:
##    num = random.randint(1, 10)
##    count += 1
##    print(num)
##
##    if num > 7:
##        break
##
##print("Total numbers generated:", count)

##def factorial(n):
##    if n == 1:   
##        return 1
##    return n * factorial(n - 1)
##
##print(factorial(5))

##def celsius_to_fahreinheit (c):
##    return(c*9/5)+32
##print(celsius_to_fahreinheit(0))

##text = input("Enter text: ")
##
##clean_text = text.replace(" ", "").lower()
##if clean_text == clean_text[::-1]:
##    print("It is a palindrome")
##else:
##    print("It is not a palindrome")

##n = int(input("Enter number of terms: "))
##
##a = 0
##b = 1
##
##print("Fibonacci Series:")
##
##for i in range(n):
##    print(a)
##    c = a + b
##    a = b
##    b = c

##def student_report(name, marks):
##    print("\n----- Student Report -----")
##    print("Name :", name)
##    print("Marks:", marks)
##
##def add_bonus(marks):
##    marks = marks + 5
##    print("Inside Function Marks:", marks)
##
##def sum_marks(n):
##    if n == 1:
##        return 1
##    return n + sum_marks(n - 1)
##
##def square(x):
##    return x * x
##
##def cube(x):
##    return x * x * x
##
##def apply_operation(func, value):
##    return func(value)
##
##name = input("Enter Student Name: ")
##marks = int(input("Enter Marks: "))
##
##student_report(name, marks)
##
##add_bonus(marks)
##print("Outside Function Marks:", marks)
##
##n = int(input("Enter a number for recursive sum: "))
##print("Recursive Sum =", sum_marks(n))
##
##print("\nChoose Operation")
##print("1. Square")
##print("2. Cube")
##
##choice = int(input("Enter Choice: "))
##num = int(input("Enter Number: "))
##
##if choice == 1:
##    operation = square
##elif choice == 2:
##    operation = cube
##else:
##    print("Invalid Choice")
##    exit()
##
##result = apply_operation(operation, num)
##print("Result =", result)
##

##L1=[1,2]
##L2=[3,4]
##L3=L1+L2
##for i in L3:
##    print(i)

##r i in range(3):
##    for j in range(1, 11):
##        print(i, "x", j, "=", i * j)
##    print()
##
##r i in range(1,5):
##    for j in range(1, 11):
##        print(i, "x", j, "=", i * j)
##    print()

##for i in range(1, 6):
##    for j in range(1, i + 1):
##        print("*", end=" ")
##    print()

##import random
##secret_number = random.randint(1, 100)
##
##print("Welcome to the Random Number Guessing Game!")
##print("I'm thinking of a number between 1 and 100.")
##
##while True:
##    try:
##        guess = int(input("Enter your guess: "))
##
##        if guess < 1 or guess > 100:
##            raise ValueError("Number must be between 1 and 100.")
##
##        if guess < secret_number:
##            print("Too low! Try again.")
##        elif guess > secret_number:
##            print("Too high! Try again.")
##        else:
##            print(f"Congratulations! You guessed the number {secret_number}.")
##            break
##
##    except ValueError as e:
##        print(f"Invalid input: {e}")
##    except Exception as e:
##        print(f"An unexpected error occurred: {e}")

##class Dog:
##    species="carine"
##    def bark(self):
##        print("woof")
##dog1=Dog()
##dog1.bark()

##class Book:
##    def __init__(self, title, author, is_borrowed=False):
##        self.title = title
##        self.author = author
##        self.is_borrowed = is_borrowed
##
##    def display_info(self):
##        print(f"Title: {self.title}, Author: {self.author}, Borrowed: {self.is_borrowed}")
##
##
##book1 = Book("The Alchemist", "Paulo Coelho")
##book2 = Book("1984", "George Orwell", True)
##book3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
##
##book1.display_info()
##book2.display_info()
##book3.display_info()



##class BankAccount:
##    def __init__(self):
##        self.balance = 0
##
##    def deposit(self, amount):
##        self.balance += amount
##
##    def withdraw(self, amount):
##        if amount <= self.balance:
##            self.balance -= amount
##        else:
##            print("Insufficient funds")
##
##acc1 = BankAccount()
##acc2 = BankAccount()
##
##acc1.deposit(1000)
##print(acc1.balance)
##
##acc1.withdraw(300)
##print(acc1.balance)
##
##acc2.deposit(500)
##print(acc2.balance)
##
##acc2.withdraw(700)
##print(acc2.balance)

class Ticket:
    def __init__(self, movie_name, available_seats, requested_seats):
        self.movie_name = movie_name
        self.available_seats = available_seats
        self.requested_seats = requested_seats

        print(f"\nMovie: {self.movie_name}")

        if requested_seats <= available_seats:
            self.available_seats -= requested_seats
            print("Booking Confirmed!")
            print("Requested Seats:", requested_seats)
            print("Seats Left:", self.available_seats)
        else:
            print("Sorry! Requested seats are not available.")

t1 = Ticket("Avengers", 100, 4)
t2 = Ticket("Pushpa 2", 20, 25)
t3 = Ticket("Interstellar", 50, 10)

class Product:

    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


data = [
    (1, "Laptop", 50000, 2),
    (2, "Mouse", 500, 5),
    (3, "Keyboard", 1200, 3)
]

products = []

for i in data:
    p = Product(i[0], i[1], i[2], i[3])
    products.append(p)

grand_total = 0

for p in products:
    print("ID:", p.id)
    print("Name:", p.name)
    print("Total Value:", p.total_value())
    print()

    grand_total = grand_total + p.total_value()

print("Total Inventory Value =", grand_total) 

