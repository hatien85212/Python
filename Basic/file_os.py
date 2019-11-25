import os #os contains functions to get information on local directories, files, processes, and environment variables.
"""https://www.bogotobogo.com/python/python_files.php
os.getcwd(): current working directory
os.chdir(subdir): change the current working directory
os.listdir(): list items belong to path. Ex: os.listdir(x) --> return a list
os.path.join():  will add an extra slash to the pathname before joining it to the filename. Example: x=os.path.join('c:/','intel')
os.path.split():  split full pathnames, directory names, and filenames into their constituent parts. --> return tuple 
os.path.splitext():  splits a filename and returns a tuple containing the filename and the file extension
os.path.expanduser(): 
os.stat() function returns an object that contains several different types of metadata about the file
- st_mtime : modify time
- st_size : file size

"""
#A: WORKING DIRECTORY
def directory():
	global join_path
	def get_current_directory():
		current_path = os.getcwd() #C:\WORKING\10_PYTHON\Basic
		print("Current path: " + current_path) 
		print(os.path.split(current_path)) # 2 parts: full path name + directory name 'C:\\WORKING\\10_PYTHON', 'Basic')

	#Change path to 'mod' (by join path or change p)and list items inside
	#join_path = os.path.join(os.getcwd(),'modules')
	def change_path_and_dir():
		os.chdir('mod')  #C:\WORKING\10_PYTHON\mod
		global join_path
		join_path = os.getcwd() #C:\WORKING\10_PYTHON\mod
		print('Change path to: ' + join_path + ' and files INSIDE a FOLDER')  #Change path to: C:\WORKING\10_PYTHON\Basic\mod and files INSIDE a FOLDER
		# list dir
		print(os.listdir(join_path)) #None: []
	
	#separe the pathname and directory
	def split_path():
		print(os.path.split(join_path)) #('C:\\WORKING\\10_PYTHON\\Basic', 'mod')
		(dirname, filename) = os.path.split(join_path)
	get_current_directory()
	change_path_and_dir()
	split_path()

#B. FILE: separe the filename and extension
"""

"""
def file(): #os.chdir('mod')  #C:\WORKING\10_PYTHON\mod
	print(os.path.splitext("test.py")) #('test', '.py')
	print(os.path.exists('support.py')) #FILE #false
	print(os.path.exists('test')) #FOLDER #true: existed folder "test" inside

#C: FILE METADATA: creation date, last-modified date, file size, and so on
def file_metadata(): #https://www.tutorialspoint.com/python/os_stat.htm
	pass
#sut_path = os.path.join(os.path.dirname(__file__),
                                      #'..', 'sut', 'login.py')
#sut_path = os.path.join('c:/','intel') #c:/intel
#os.path.dirname(__file__)
directory()
file()
file_metadata()

print (sut_path)
#print ('__file__:',__file__) #Print file name: ('__file__:', 'file_os.py')