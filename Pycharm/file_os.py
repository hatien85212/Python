import os
#https://www.w3schools.com/python/python_file_write.asp
def read_file(file_name):
    #1. Open and read file: f = open(f, "r")
    f = file_name # "demofile.txt" #"../test.txt" to open a file outside
    f = open(f, "r")
    #print(f.read()) #print entire file content

    #2. Read Only Parts of the File: f.read()
    #print(f.read(5)) #Hello -- first 5 chars

    #3. Read Lines: By calling readline() two times, you can read the two first lines:
    #print(f.readline()) #read first line
    #print(f.readline()) #read 2nd line
    for x in f: #By looping through the lines of the file, to read the whole file, line by line:
      print(x)
      #print(f.readline())
    #print f.readlines() #read and print whole file content including break line: \n

    #4. Close Files
    f.close()


#Write with 2 modes: a (append to the end) and w(overwrite)
def write_file_a(file_name):#demofile2.txt
    f = open(file_name, "a") #will append to the end of the file
    f.write("Now the file has more content!")
    # open and read the file after the appending:
    f = open(file_name, "r")
    print(f.read())
    f.close()


def write_file_w(file_name):#demofile3.txt
    f = open(file_name, "w") #will overwrite any existing content
    f.write("Woops! I have deleted the content!")
    f.close()

    # open and read the file after the appending:
    f = open(file_name, "r")
    print(f.read())


#to create a file, use open() method with one of parameters
#"x" - Create - will create a file, returns an error if the file exist
#"a" - Append - will create a file if the specified file does not exist
#"w" - Write - will create a file if the specified file does not exist
def create_file(file_name):
    f = open(file_name, "a")

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("The file does not exist")
def create_folder(path, folder_name):
    try:
        os.mkdir(path+folder_name)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
def delete_folder(folder_name):# by using rmdir()
    if os.path.exists(folder_name):
        os.rmdir(folder_name)
    else:
        print("The folder does not exist")
read_file("demofile.txt")
write_file_a("demofile2.txt")
write_file_w("demofile3.txt")
create_file("myfile.txt")
delete_file("myfile.txt")
path = os.getcwd()
print path
create_folder(path, "/defd")
delete_folder("test")
file_path = '../test.txt'
print(os.path.exists(file_path))
try:
    fo = os.open("file.txt","w+")
    for i in range(10):
        fo.write("This is line %d\r\n" % (i + 1))
    # print(fo.read())

    print ("Closed or not : ", fo.closed)
    print ("Opening mode : ", fo.mode)
    print ("Softspace flag : ", fo.softspace)
except Exception:
    print ("Can't open file")

"""File object attribute

"""
