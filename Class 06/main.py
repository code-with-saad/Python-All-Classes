# Iterate over dictionary

# obj = {
#     "id": 1,
#     "name": "Saad",
#     "is_employeed": False,
#     "is_active": True,
# }

# print(obj)

# for i in obj:
#     # print(i)
#     print(obj[i])


# enumerate() is a for loop function
# for k, v in enumerate(obj):
#     print(k, v)


# l = [100, 200, 300, 400, 500]

# for x, y in enumerate(l):
#     print(x, y)
# l2 = []
# for i in l:
#     l2.append(i)
#     print(l2)



lis = [
{
    "id": 1,
    "name": "Saad",
    "is_employeed": False,
    "is_active": True,
},
{
    "id": 2,
    "name": "Rasheed",
    "is_employeed": False,
    "is_active": True,
},
{
    "id": 3,
    "name": "Hassan",
    "is_employeed": False,
    "is_active": True,
},
{
    "id": 4,
    "name": "Ahmed",
    "is_employeed": False,
    "is_active": True,
}
]

# for obj in lis:
#     if obj.get("name") ==  "Ali":
#         print(obj)
#     else:
#         print("Please enter a valid name")
#         break


# x = "hello world"

# for i in x:
#     print(i)

# for i in x:
#     if i == "o" or i == "r":
        # print(i)



# nested loop

# for i in range(1, 5):
#     for j in range(i):
#         print(i, end="")
#     print()


# While Loop

# x = 5

# while x > 0:
#     print(x)
#     x-=1



# user_input = input("enter a number between 1 and 10\n")
# user_input = int(user_input)

# while user_input < 0 or user_input > 10:
#     user_input = input("Please enter a number between 1 and 10\n")
#     user_input = int(user_input)
# print("valid number is", user_input)






# write a program that increment variable value by 1 and it keeps incrementing the value until the value reaches 20 using while loop

# x = 1

# while x <= 20:
#     print(x)
#     x += 1


# write a program that remove items from the list inside while loop

# l = [1, 2, 3, 4, 5]

# while len(l) > 0:
#     print(l)
#     l.pop()
# print(l)



# Functions

# def my_function():
#     print("Hello from my_function")

# my_function()


# def functions(*kids):
#     print("The youngest child is ", kids[2])

# functions("Rasheed", "Saad", "Hassan")



# def sum(x, y):
#     x = x + y
#     # print(x)
#     return x
#     print(x)

# x = sum(1, 2)
# print(x)
# x = 0
# sum(1, 2)
# print(x)




l = [
{
    "id": 1,
    "name": "Saad",
    "gender": "Male",
    "age": 15
},
{
    "id": 2,
    "name": "Rasheed",
    "gender": "Male",
    "age": 18
},
{
    "id": 3,
    "name": "Hassan",
    "gender": "Male",
    "age": 14
},
{
    "id": 4,
    "name": "Ahmed",
    "gender": "Male",
    "age": 15
},

]


def get_employee_by_id(id):
    for i in l:
        if i.get("id") == id:
            return i

x = get_employee_by_id(1)
print(x)




















# ============================== Jarvis My Personal Assignment ==============================

"""
name = input("Enter your username\n")
passw = input("Enter your password\n")

name1 = "Saad"
pass1 = "123456"
def check_user(username, password):
            print(f"Welcome {name} from Jarvis")

while 1 > 0:
    if name != name1 and passw != pass1:
        print(f"Invalid username or password")
        inp1 = input("Do you want to try again? (y/n): ")
        if inp1 == "y":
            name = input("Enter your username\n")
            passw = input("Enter your password\n")
    else:
        check_user(name1, pass1)
        break
"""