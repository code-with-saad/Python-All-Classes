# =============================== File Handling ===============================

f = open("file.txt", "r")

content = f.read() # read whole file at once but in string form
content = content.replace("**name**", "Saad")
print(content)


# content = f.readlines() # read whole file at once but in list form
# print(len(content))
# print(content)


# f1 = open("another_file.txt", "r")

# row = f1.readline()
# print(row)
# row = f1.readline()
# print(row)


# myline = f1.readline()
# while myline:
#     print(myline)
#     myline = f1.readline()
# f1.close()



# f2 = open("new_file.txt", "r") # if the operation is set to "r" = read, it will give you error in starting try printing
# print(f2)
# but if we use "w" = write, operation it will create or a file exist it will overide the data

# f2 = open("new_file.txt", "w")

# s = f2.write("A B C D\n")
# print(s)
# s = f2.write("E F G H")
# print(s)
# s = f2.writelines(["A", "B","\n" "C", "D"])
# print(s)


# f3 = open("another_file.txt", "a")
# f3.write(" A B C D\n")
# f3.close()

# f3 = open("another_file.txt", "r")

# s = f3.read()
# print(s)


# f = open("new_file.txt", "w+")
# print("Pointer Position: ", f.tell())

# f.write("1234")
# print("Pointer Position: ", f.tell())

# f.seek(0)
# print("Pointer Position: ", f.tell())

# content = f.read()
# print(content)


# f = open("new_file.txt", "r+")
# print("Pointer Position: ", f.tell())

# f.read()
# print("Pointer Position: ", f.tell())

# f.seek(0)
# print("Pointer Position: ", f.tell())

# f.write("abcddddddddddddd")



# f = open("new_file.txt", "a+")
# f.write("using append method line 1\n")
# f.write("using append method line 2\n")
# f.seek(0)

# content = f.read()
# print(content)

# import time
# f = open("new_file.txt", "w")

# for i in range(60):
#     print("write line", i)
#     f.write("line" + str(i) + "\n")
#     if i % 10 == 0:
#         print("Flushed")
#         f.flush()
#     time.sleep(1)

# f.close()


import os

current_working_dir = os.getcwd()


# print(current_working_dir)
# print(__file__)
# print(os.listdir())

# files_and_folder_in_dir = os.listdir()

# path = os.path.join("folder_1", "folder_2", "folder_3", "folder_4", "file_1.py")
# print(path)


# path = os.path.join("..", " parent_file.txt")
# print(path)

# f = open(path, "w")
# f.write("my report1")



# parent_dir = os.path.join("")
current_working_dir = os.getcwd()
# print(f)

parent_dir = os.path.abspath(current_working_dir)

path = os.listdir("..")
print(parent_dir)
# print(path)






























