# ============================ OS Module Exercise ============================

import os

cwd = os.getcwd()
def open_folder(path, folder_name= ""):
    path1 = os.path.join(path, folder_name)

# open_folder(cwd, "folder_3")


def move_to_parent_folder(path):
    path1 = os.path.join(path)

# move_to_parent_folder("..")

    

# cwd2 = os.getcwd()
pap = open_folder(cwd, "folder_3")
pop = move_to_parent_folder("..")
def display_files_and_folder(path):
    files_folder_in_parent = os.listdir(path)
    print(files_folder_in_parent)


display_files_and_folder(pop)
