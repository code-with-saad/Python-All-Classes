print("============================= Arithmatic Operators =============================")

# + for addition
# - for subtraction
# * for multiplicatoin
# / for division

# // for floor division
# %  for remainder

# ===================================== Example =====================================

# ------------------------- Addition -------------------------

# Adding Two Integars 
print(2 + 5)        # 7

# Adding Two Strings ( Means Concatination that we learn in third class )
print("2" + "5")    # 25


# ------------------------- Subtraction -------------------------

# Subtracting Two Integars 
print(7 - 5)        # 2



# ------------------------- Multiplicatoin -------------------------

# Multiplication of Two Integars 
print(2 * 5)        # 10



# ------------------------- Division -------------------------

# Dividing Two Integars 
print(10 / 2)        # 5.0



# ------------------------- Floor Division -------------------------

# Floor Dividing Two Integars ( It works same as division but it shows the answer in integar )
print(10 // 2)        # 5



# ------------------------- Remainder -------------------------

# Getting Remainder of Two Integars 
print(11 % 2)        # 1






print("============================= Assignemnt Operator =============================")

# Below are the examples of assignment operators

# =		
# += 
# -= 
# *= 
# /= 
# %= 
# //= 



x = 5         # Value 5 is saved in the variale x
print(x)      # 5

# How to increment the value of x by 1
x = x + 1
print(x)    # 6

# Another way of incrementing the value of variable
x += 1
print(x)    # 7


# Other operators works similarly

# Subtraction
y = 10
print(y)    # 10
y -= 2      # 10 - 2
print(y)    # 8
y -= 5      # 8-5
print(y)    # 3


# Multiplication
y = 2
print(y)    # 2
y *= 5      # 2 * 5
print(y)    # 10
y *= 2      # 10 * 2
print(y)    # 20


# Division
y = 10
print(y)    # 10
y /= 2      # 10/2
print(y)    # 5.0
y /= 5      # 5.0/5
print(y)    # 1.0


# Floor Division
y = 10
print(y)    # 10
y /= 2      # 10/2
print(y)    # 5
y /= 5      # 5/5
print(y)    # 1


# NOTE: Python does not support post and pre increment operators
#For example:
#x++
#++x





print("============================= Comparison Operators =============================")

# Below are the Examples of Comparison Operators

"""
Operator		Name					            Example	
==			    Equal					                    x == y	
!=			    Not equal				                  x != y	
>			      Greater than				              x > y	
<			      Less than				                  x < y	
>=			    Greater than or equal to	        x >= y	
<=			    Less than or equal to		          x <= y
"""

x = 5
y = 8
print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x < y:", x < y)    # True
print("x > y:", x > y)    # False
print("x <= y:", x <= y)  # True
print("x >= y:", x >= y)  # False


x = 10
y = 6
print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x < y:", x < y)    # False
print("x > y:", x > y)    # True
print("x <= y:", x <= y)  # False
print("x >= y:", x >= y)  # True

x = 20
y = 20
print("x == y:", x == y)  # True
print("x != y:", x != y)  # False
print("x < y:", x < y)    # False
print("x > y:", x > y)    # False
print("x <= y:", x <= y)  # True
print("x >= y:", x >= y)  # True



print("============================= Logical Operators =============================")

# Comparison between more than 2 operands
# Below are the operators

"""
and => it returns true if all the operands are true otherwise it returns false
or  => it returns true if any one of the operands are true and return false if all operands returns false 
not => it revers the value. if value is true it will make it false. if value is false, it will make it to true
"""

print(True and True)    # True
print(True or True)     # True
print(False and False)  # False
print(False or False)   # False
print(True and False)   # False
print(True or False)    # True


# a = True
# b = True
# c = False
# d = False


# print(a and b)
# print(a or b)
# print(a or c)
# print(a and d)
# print(a and b or c)

# # wrong answer for all students
# print(a or b and c)

# # use round bracket to set priority
# print((a or b) and c)
# print(a or (b and c))



print((True and True) and (True and True))    # True
print((True and True) or (True and True))     # True

print((False and False) and (False and False)) # False
print((False or False) and (False or False))  # False

print((True and False) and (False and True))  # False
print((True or False) and (False or True))    # True

print((True and False) and (False or True))   # False
print((True and False) or (False or True))    # True




print("============================= If Statement =============================")

# it controls the flow of the program based on the condition provided
# review the below flow chart, this is how the if statement works
# https://i.ytimg.com/vi/WHH8Gx0u9Is/maxresdefault.jpg

# ----------------------- Syntax ----------------------------
condition = True
if condition == True:
  print("hello world")
else:
  print("hello universe")
# the above program will display "hello world"
  
condition1 = False
if condition1 == True:
  print("hello world")
else:
  print("hello universe")
# the above program will display "hello universe"

x = 20
if x == 5:
  print("the number is 5")
elif x == 10:
  print("the number is 10")
elif x == 15:
  print("the number is 15")
elif x == 20:
  print("the number is 20")
# the above program will display the number is 20


x1 = 25
if x1 == 5:
  print("the number is 5")
elif x1 == 10:
  print("the number is 10")
elif x1 == 15:
  print("the number is 15")
elif x1 == 20:
  print("the number is 20")
else:
  print("the number is not 5 or 10 or 15 or 20 :( ")
  # the above program will display "the number is not 5 or 10 or 15 or 20 :("





print("============================= List [ Arrays ] =============================")

# CRUD Operations

# We use list (array) in order to add multiple items in a variable i.e
l = ["pizza", "burger", "sandwich", "bbq"]
print(l)


# how to access 1 item from the list
l = ["pizza", "burger", "sandwich", "bbq"]
item_1 = l[0]
print(item_1) # pizza
item_2 = l[1]
print(item_2) # burger
item_3 = l[2]
print(item_3) # sandwich
item_4 = l[3]
print(item_4) # bbq

# item_5 = l[4] # it will produce an error: index out of range



# how to count items in a list
l = ["pizza", "burger", "sandwich", "bbq"]
total_items = len(l)
print(total_items) # 4


# how to access last item of the list - 1
l = ["pizza", "burger", "sandwich", "bbq"]
total_items = len(l)
last_item = l[total_items - 1]
print(last_item) # bbq

# how to access last item of the list - 2
l = ["pizza", "burger", "sandwich", "bbq"]
last_item = l[-1]
print(last_item) # bbq


# how to update item in a list
l = ["pizza", "burger", "sandwich", "bbq"]
print(l) # ["pizza", "burger", "sandwich", "bbq"]
l[0] = 'anda-paratha'
print(l) # ["anda-paratha", "burger", "sandwich", "bbq"]



print("============================= List [ Arrays ] Functions =============================")


# add item in the end of the list
l = ["pizza", "burger", "sandwich", "bbq"]
l.append("anda-paratha")
print(l) # ["pizza", "burger", "sandwich", "bbq", "anda-paratha"]
l.append("chicken-roll")
print(l) # ["pizza", "burger", "sandwich", "bbq", "anda-paratha", "chicken-roll"]

# add item at specified index in the list
l = ["pizza", "burger", "sandwich", "bbq"]
l.insert(1, "anda-paratha")
print(l) # ["pizza", "anda-paratha", "burger", "sandwich", "bbq"]

# remove item from the end of the list
l = ["pizza", "burger", "sandwich", "bbq"]
l.pop()
print(l) # ["pizza", "burger", "sandwich"]

# remove item from the list by providing index
l = ["pizza", "burger", "sandwich", "bbq"]
l.pop(2)
print(l) # ["pizza", "burger", "bbq"]

# remove item from the list by value
l = ["pizza", "burger", "sandwich", "bbq"]
l.remove("burger")
print(l) # ["pizza", "sandwich", "bbq"]

# remove all items from the list - 1
l = ["pizza", "burger", "sandwich", "bbq"]
l.clear()
print(l) # []

# remove all items from the list - 2
l = ["pizza", "burger", "sandwich", "bbq"]
l = []
print(l) # []

# merge 2 lists
l1 = ["pizza", "burger", "sandwich", "bbq"]
l2 = ["anda-paratah", "chicken-roll"]
l1.extend(l2)
print(l1) # ["pizza", "burger", "sandwich", "bbq", "anda-paratah", "chicken-roll"]

# sort items in the list in ascending order
l1 = ['d', 'b', 'a', 'c']
l1.sort() # ['a', 'b', 'c', 'd']
print(l1)

# sort items in the list in descending order
l1 = ['d', 'b', 'a', 'c']
l1.sort(reverse=True) # ['d', 'c', 'b', 'a']
print(l1)
