# ================================= Exercise 3 =================================

# Write a Python program to copy a list using for loop. consider a list
# li = [1, 2, 3, 4]
# li_2 = []
# use for loop and add al the items in li_2

# -------------------------------------------------------------

# li = [1, 2, 3, 4]
# li_2 = []

# for i in li:
#     li_2.append(i)
# print(li_2)


# -------------------------------------------------------------

# Write a Python function that takes two lists and returns True if they have at least one common member.
# consider list l1 = [1, 2, 3, 4] and l2 = [5, 6, 7, 3]
# in both list value "3" is common
# use for loop
# hint: nested loop

# -------------------------------------------------------------

# def list_function(l1, l2):
#     result = False
#     for x in l1:
#         for y in l2:
#             if x == y:
#                 result = True
#                 return result


# print(list_function([1, 2, 3, 4], [5, 6, 7, 3]))

# -------------------------------------------------------------

# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
# 3 400

# -------------------------------------------------------------

# l = [100, 200, 300, 400]

# for x, y in enumerate(l):
#     print(x, y)

# -------------------------------------------------------------

# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

# -------------------------------------------------------------

# l1 = ['a', 'b', 'c', 'd']
# l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# l3 = l1 + l2
# l4 = []
# for x in l3:
#     h = l3.count(x)
#     if x not in l4:
#         l4.append(x)
#         print(f"{x}: {h}", end=", ")

# -------------------------------------------------------------

# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"

# -------------------------------------------------------------

# num = 2783
# count = 0

# while num != 0:
#     num //= 10
#     count += 1
# print(f"Number of Digits: {count}")

# -------------------------------------------------------------

# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”

# -------------------------------------------------------------

# inp = input("Enter any number\n")

# while inp != "0":
#     inp = input("Enter any number\n")

# -------------------------------------------------------------

# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list

# -------------------------------------------------------------

# ask_user = int(input("enter number\n"))
# x = 1
# l = []

# while x < 6:
#     l.append(ask_user)
#     x = x + 1
#     ask_user = int(input("enter number\n"))


# s =  sum(l)
# print(l)
# print(s)

# -------------------------------------------------------------

# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.

# -------------------------------------------------------------

# ask = int(input("enter any number\n"))
# l1 = []

# while ask > 0:
#     l1.append(ask)
#     ask = int(input("enter any number\n"))


# print("=================")
# add = sum(l1)
# print(f"Sum of all entered numbers: {add}")

# -------------------------------------------------------------

# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

# -------------------------------------------------------------

# name = input("Enter any name: ").capitalize()

# end = "End"
# done = "I am done"

# while True:
#     if name == end or name == done:
#         break
#     else:
#         print(name)
#         name = input("Enter any name: ").capitalize()

# -------------------------------------------------------------

# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"

# -------------------------------------------------------------

# l1 =  [11, 33, 50]

# for i in l1:
#     print(i, end="")

# -------------------------------------------------------------

# Write a Python program to copy a dict using for loop. consider a dict
# d1 = {"id": 1, "name": "your-name", "gender": "male"}
# d2 = {}
# use for loop and add al the items in d2
# hint: https://github.com/mdanish0320/teaching-class/blob/de18a6216425cde375c82a793480919af824a67c/JP-BE-PY-batch-1/loop/enumerate_.py#L12C1-L19C16

# -------------------------------------------------------------

# d1 = {"id": 1, "name": "your-name", "gender": "male"}
# d2 = {}

# for key, val in d1.items():
#     d2[key] = val

# print(d2)

# -------------------------------------------------------------


# ================================= Exercise 1 =================================

# Write a program to create a function that takes two arguments, name and age. print them inside function.

# -------------------------------------------------------------

# def function(name, age):
#     print(f"My name is {name} and my age is {age}")

# function("Saad", 16)

# -------------------------------------------------------------

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# -------------------------------------------------------------

# def show_employee(name, salary= 9000):
#     print(name)
#     print(salary)

# show_employee("Ali")
# print("==========")
# show_employee("Saad", 15000)

# -------------------------------------------------------------

# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10 
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

# -------------------------------------------------------------

# def list_function(a, b, c, d):
#     return [a, b, c, d]

# p =  list_function(a = 4, b = 8, c = 10, d = 12)
# print(p)
    
# -------------------------------------------------------------

# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.

# -------------------------------------------------------------

# def km_to_miles(kilometer):
#     conv_fac = 0.621371
#     miles = kilometer * conv_fac
#     text = "%0.2f kilometer is equal to %0.2f miles" %(kilometer, miles)
#     return text

# print(km_to_miles(3))

# -------------------------------------------------------------

# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.

# -------------------------------------------------------------

# def is_divisable_by_11(integar):
#     divisible =  f"{integar} is divisible by 11: {integar % 11 == 0}"
#     return divisible

# print(is_divisable_by_11(14523))

# -------------------------------------------------------------

# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

# -------------------------------------------------------------

# def get_highest(num1, num2):
#     if num1 > num2:
#         return f"{num1} is highest"
#     elif num2 > num1:
#         return f"{num2} is highest"
#     else:
#         return f"Both are equal"

# print(get_highest(15, 11))
# print(get_highest(111, 150))
# print(get_highest(0, 0))

# -------------------------------------------------------------

# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg and "fuel_per_liter" as optional arg that has default value to 280. The function should return the cost in Rs.

# -------------------------------------------------------------

# def fuel_cost(distance, fuel_per_liter= 280):
#     consumption = 20
#     liters_required = distance // consumption
#     total_cost = liters_required * fuel_per_liter
#     return f"Rs {total_cost}"

# print(fuel_cost(40))

# -------------------------------------------------------------

# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.

# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number

# hint: use if statement 6 times to check each rule. if any one rule failed return false

# -------------------------------------------------------------
















