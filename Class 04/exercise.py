# =========================== If Statement Assignments ===========================

# Write a program to check whether a person is eligible to vote or not?


# eligibility = 18
# name = input("Enter your Name \n")
# age = int(input("Enter your age \n"))


# if age >= eligibility :
#     print("You are eligible to vote")
# else:
#     print("You are not eligible for vote")

# ===================================================================================

# ------------ Write a program to check char is vowel or not. ------------

# char = input("Enter a character ")

# if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#     print("Character is vowel")
# else: 
#     print("Character is not vowel")


# ===================================================================================

# ------ Write a program to check the number is positive or negative. User input. ------

# num1 = int(input("Enter a Number\n"))

# if num1 > 0:
#     print("Number is Positive")
# elif num1 == 0:
#     print("Neither Positive Nor Negative")
# else:
#     print("Number is Negative")


# ===================================================================================


# -------- Write a program to check whether a number is odd or even? --------

# num = int(input("Enter a Number\n"))

# if (num % 2) == 0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is odd")


# ===================================================================================


# -------- Write a program to display the grade of the user in subject A, ask user marks obtained out of 100 --------


# usermarks = int(input("Enter Marks Obtained out of 100\n"))

# if usermarks >= 80:
#     print("Marvelous Performance!\nyou obtained \"A+\" Grade")
# elif usermarks >= 70:
#     print("Super Performance!\nyou obtained \"A\" Grade")
# elif usermarks >= 60:
#     print("Good Performance!\nyou obtained \"B\" Grade")
# elif usermarks >= 50:
#     print("Nice But needs improvement!\nyou obtained \"C\" Grade")
# else:
#     print("\"Fail\"")


# =========================== List Assignments ===========================


# -------- Create a list of juices, add 5 items using append --------

# juices = ["Apple Juice", "Beet Juice", "Blueberry Juice"]
# print(juices)
# juices.append("Pineapple Juice") 
# juices.append("Orange Juice") 
# juices.append("Pomegranate Juice") 
# juices.append("Grapefruit Juice") 
# juices.append("Grape Juice")
# print(juices)

# ===================================================================================


# -------- Create a list of cars, add 5 items using insert --------

# cars = ["BMW", "Mercedes", "Audi"]
# print(cars)
# cars.insert(0, "Ferrari")
# cars.insert(4, "Lamborghini")
# cars.insert(5, "Bugatti")
# cars.insert(2, "Rolls Royce")
# cars.insert(6, "Fortuner")
# print(cars)


# ===================================================================================

# -------- Remove last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]	using pop and len 
# output should display [‘bed’, ‘table’, ‘chair’] --------


# list1 = ["bed", "table", "chair", "sofa"]
# print(list1)

# list1.pop()
# print(list1)


# ===================================================================================

# -------- Remove second last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’] 
# by len and index --------

# output should display [‘bed’, ‘table’, ‘sofa’]


# list2 = ["bed", "table", "chair", "sofa"]
# print(list2)

# list2.pop(-2)
# print(list2) 


# ===================================================================================

# -------- Remove first item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’] 
# output should display [‘table’, ‘chair’, ‘sofa’] --------


# list3 = ["bed", "table", "chair", "sofa"]
# print(list3)

# list3.pop(0)
# print(list3)


# ===================================================================================

# -------- Remove the item “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]
# output should display [‘bed’, ‘table’, ‘sofa’] --------


# list4 = ["bed", "table", "chair", "sofa"]
# print(list4)

# list4.remove("chair")
# print(list4)


# ===================================================================================


# -------- Remove all “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’, ‘chair’]

# output should display [‘bed’, ‘table’, ‘sofa’] --------


# list5 = ["bed", "table", "chair", "sofa", "chair"]
# print(list5)

# list5 = [i for i in list5 if i != "chair"]

# print(list5)


# ===================================================================================


# -------- Merge two lists [‘A’, “B”, “C”] and [“D”, “E”, “F”]
# output should display [‘A’, “B”, “C”, “D”, “E”, “F”] --------

# list6 = ["A", "B", "C"]
# list7 = ["D", "E", "F"]
# print(list6)
# print(list7)

# list6.extend(list7)
# print(list6)


# ===================================================================================

# -------- Write a Python program to check if a list is empty or not. --------


# list8 = []

# if list8 == []:
#     print("List is empty")
# else:
#     print("List is not empty")