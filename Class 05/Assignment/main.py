# =================================== Exercises List 1 ===================================


# 1. output the numbers from 1 to 10 using range function and for loop
# output should be like
# 1
# 2
# 3
# etc
# ----------------------------------------------------------

# for i in range(1, 11):
#     print(i)

# ----------------------------------------------------------


# 2. output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc


# ----------------------------------------------------------

# for i in range(35, 51):
#     print(i)

# ----------------------------------------------------------

# 3. output the numbers from -15 to -25 using range function and for loop
# output should be like
# -15
# -16
# -17
# etc

# ----------------------------------------------------------


# for i in range(-15, -26, -1):
#     print(i)

# ----------------------------------------------------------


# 4. output the numbers from 5 to -10 using range function and for loop
# output should be like
# 5
# 4
# 3
# etc

# ----------------------------------------------------------

# for i in range(5, -11, -1):
#     print(i)

# ----------------------------------------------------------


# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# output should be like
# 0
# 3
# 6
# 9
# etc

# ----------------------------------------------------------

# for i in range(0, 50, 3):
#     print(i)


# ----------------------------------------------------------

# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc

# ----------------------------------------------------------

# for i in range(1, 11):
#     print(f"2 x {i} = {i * 2}")


# ----------------------------------------------------------


# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint: 
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i


# ----------------------------------------------------------

# l = [3, 5, 2, 1, 4]
# x = 0

# for i in l:
#     x+=i
# print(x)


# ----------------------------------------------------------


# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop


# ----------------------------------------------------------

# l = [3, 5, 2, 1, 4]
# x = 0

# for i in l:
#     if x < i:
#         x = i
# print(x)

# ----------------------------------------------------------


# =================================== Exercises List 2 ===================================

# 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].
# output should be 360
# hint: use a variable x outside the loop and assign the first value of list
# inside the loop * the value of x with the local variable of loop
# x *= 

# ----------------------------------------------------------


# l = [3, 5, 2, 1, 4]
# x = l[0]

# for i in l:
#     x*=i
# print(x)


# ----------------------------------------------------------

# 2. create a list from 0 to 100 using range function and iterate over the list
# display the number that satisfied following conditions
# The number must be divisible by 5
# If the number is greater than 30 and less than 50 then skip it
# If the number is greater than 80, then stop the loop

# ----------------------------------------------------------


# for i in range(0, 101, 5):
#     if i > 30 and i < 50:
#         print(i)
#         continue
#     elif i > 80:
#         print(i)
#         break


# ----------------------------------------------------------

# 3. consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

# ----------------------------------------------------------


# lis = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']

# for i in lis:
#     if len(i) > 5:
#         print(i)


# ----------------------------------------------------------

# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']

# ----------------------------------------------------------


# l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# m = l[0], l[4], l[5]

# new_list = []

# for i in l:
#     if i not in m:
#         new_list.append(i)
# print(new_list)


# ----------------------------------------------------------

# 5. Write a program to display odd numbers only. odd number upto 100
# hint use for loop and range function

# ----------------------------------------------------------


# for i in range(1, 100, 20:
#     print(i)


# ----------------------------------------------------------

# 6. List contains 30 elements. Display first 5 and last 5 elements

# ----------------------------------------------------------


# l = list(range(1, 31))

# for i in l:
#     print(l[:5])
#     print(l[25:30])
#     break


# ----------------------------------------------------------

# 7. Display output: helloworld from the list [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
# output should be 'helloworld' in one line

# ----------------------------------------------------------


# l1 = ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]

# for i in l1:
#     print(i,end="")


# ----------------------------------------------------------

# 8. Write a Python program to append a list to the second list.
# consider l1 is [1, 2, 3, 4, 5] and l2 is []
# using loop add items of l1 in l2

# ----------------------------------------------------------


# l1 = [1, 2, 3, 4, 5]
# l2 = []

# for i in l1:
#     l2.append(i)
#     print(l2)  


# ----------------------------------------------------------

# 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# use for loop and find the count that how many times the word "hi" present in list.
# output should be 3

# ----------------------------------------------------------


# list1 = ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']

# for i in list1:
#         print(list1.count("hi"))
#         break


# ----------------------------------------------------------
