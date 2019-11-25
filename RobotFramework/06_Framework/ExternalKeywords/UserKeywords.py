import os


def create_folder(file_name):
    if os.path.exists(file_name): #Example: C:\\RF
        os.mkdir(file_name)
    else:
        print("The folder is exist")