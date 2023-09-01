# def add(x,y):
#     return x + y

# def subtract(x,y):
#     return x - y

# def multiply(x,y):
#     return x * y

# def divide(x,y):
#     return x / y

# print("Enter Operator")
# print("1 Enter Addition")
# print("2 Enter Subtraction")
# print("3 Enter Multiplication")
# print("4 Enter Division")
# while True:
#     operator = input("Enter Choice 1/2/3/4: ")
#     if operator in ("1", "2", "3", "4"):    
#         try:
#             num1 = int(input("Enter First Number: "))
#             num2 = int(input("Enter Last Number: "))

#         except ValueError:
#             print("Invalid input. Please enter a number.") 

#         if operator == "1":
#             print(num1, "+", num2, "=", add(num1, num2))
#         elif operator == "2":
#             print(num1, "-", num2, "=", subtract(num1, num2))
#         elif operator == "3":
#             print(num1, "*", num2, "=", multiply(num1, num2))
#         elif operator == "4":
#             print(num1, "/", num2, "=", divide(num1, num2))
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#             break
#         elif next_calculation == "yes":
#             continue
#         elif next_calculation != "yes" or next_calculation != "no":
#             print("Invalid Input")
#             break
