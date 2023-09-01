# ============================ Concatination ================================= 

# x = "Hello"
# y =  "World"
# z = x + y 

# print(z)
# print(x + " " + y)

# num1 = 5
# num2 = 10

# print(num1 + num2)

# num11 = "5"
# num12 = "10"

# print(num11 + num12)


# ========================= String Interpolation ===================================

# ========================= Three Methods ==========================================

# ( Method 1 ) -------------------------- f string -------------------------------------------

# h = "World"

# print(f"Hello {h}")

# name = "Saad"
# age = 16

# print(f"My name is {name}. I am {age} years old")


# ( Method 2 ) -------------------------- .format string method ------------------------------

# name = "Saad"
# age = 16

# print("My name is {}. I am {} years old".format(name, age))


# ( Method 3 ) ------------------------- %s string interpolation method ----------------------

# name = "Saad"
# age = 16

# print("My name is %s. I am %s years old" %(name, age))



# ============================== Escape Characters ==================================

# name = "My name is Saad"
# age = "I'm 16"

# print(name + "\n" + age)
# print(name + " \t" + age)



# ============================== User Input Function ===================================

# print (input("Please Enter your name: "))

# x = "ABCD"

# i1 =  input(f"Enter your name: hint {x} ")
# i2 =  input("Enter your age: ")

# print(f"My Name is {i1}. I'm {i2}")



# ================================== Exercises ===========================================



""" 1) ----------------------- Write a program to ask user his name. 
The name should be asked in new line --------------------------- """ 

# x = input("Enter your name: \n")


# 2) You have to print ( Hi User_Input! Welcome back )

# inp1 = input("Enter your name: ")
# print(f"Hi {inp1}! Welcome back.")



# ================================== Ask user two numbers and display their sum ====================================

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))

# num1 = input("Enter First Number: ")
# num2 = input("Enter Second Number: ")

# print(type(num1))

# num1 = int(num1) # convert str to int
# num2 = int(num2) # convert str to int

# print(type(num1))

# sum = num1 + num2
# print(f"Sum of {num1} + {num2} is {sum}")



# ================================== Ask user two numbers and display their squares ====================================

# sq1 = int(input("Enter number \n"))

# square = sq1 * sq1
# print(f"Square of {sq1} is {square}")



# =========================== Write a program to ask user 3 subjects scores and display ==== =============================
# Maths: Score
# English: Score
# Physics: Score

# sub1 = input("Enter Maths Score\n")
# sub2 = input("Enter English Score\n")
# sub3 = input("Enter Physics Score\n")

# print(f"Maths: {sub1}\nEnglish: {sub2}\nPhysics: {sub3}")



# ========================== Ask user 2 number and display SUM, MULTIPLICATION, SUBTRACTION and DIVISION ========================================

# num1 = int(input("Enter First Number\n"))
# num2 = int(input("Enter Second Number\n"))

# print(f"Addition: {num1 + num2} \nSubtraction: {num1 - num2} \nMultiplication: {num1 * num2}     \nDivision: {num1 / num2}")



# ==================== Write a Program to swap the variable values ==========================

# x = 1
# y = 2
# print("x is ", x)
# print("y is ", y)

# Use some technique here to replace the variable values
# z = y
# y = x
# x = z
# print("x is ", x)
# print("y is ", y)



# ==================================== String Methods ====================================
# txt = "hello world"
# print(txt.format())

# print(txt.lower()) # make all character to lower
# print(txt.capitalize()) # make first character to capital
# print(txt.upper()) # make all character to upper

# txt1 = " Hello World "
# print(txt1)
# print(txt1.strip())

# print(txt)
# print(txt.replace("world", "myworld"))



# ============================== Built-in Methods ===================================


# print("hello world")
# x = "hello world"
# print(len(x))

# y = 1.567
# print(round(y , 2))

# input("Enter")

# print(type(y))

# print(isinstance(x,str))
# print(isinstance(x,int))

# ============================ Arithmetic Operators ================================
# plus: +
# subtraction: -
# multiply: *
# divide: /
# modulus: %

# ----------------------------------------------------------------------------------

print("5 % 1 = ", 1%5)
# print("5 % 2 = ", 2%5)
# print("5 % 3 = ", 3%5)
# print("5 % 4 = ", 4%5)
# print("5 % 5 = ", 5%5)

# print("----------")
# print("----------")
# print("----------")

# print("5 % 6 = ", 6%5)
# print("5 % 7 = ", 7%5)
# print("5 % 8 = ", 8%5)
# print("5 % 9 = ", 9%5)
# print("5 % 10 = ", 10%5)