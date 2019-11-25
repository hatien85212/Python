# This Python file uses the following encoding: utf-8
#!/usr/bin/python
# -*- coding: ascii -*-
#A module is a Python object with arbitrarily named attributes that you can bind and reference.
# a module is a file consisting of Python code
# Will call to a Python object or module "support.py". To use methods in module "support.py", use the format: import module1[, module2[,... moduleN]
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
""" from...import Statement: import specific attributes from a module into the current namespace
from modname import *
from fib import fibonacci
from robot.api import logger --> logger.py is a module just with methods; robot.api is path Lib/site-packages/robot/api/logger.py
from robot.utils import NormalizedDict
from selenium.webdriver.remote.webelement import WebElement ==> webelement can be a package or .py. 
- If webelement = package(folder) --> WebElement is a module
- if webelement = module (.py) --> WebElement is a module--> then WebElement will be a name (varialbe, method, class)
import support  --> support.py is module with methods

The dir() function only outputs the list of names inside the current scope
"""
#'PATH VARIBLE'. Path variable helps in running any .exe (executable) file whose path is given in Path variable directly through cmd without specifying it's full path.
""" Locate modules: When you import a module, the Python interpreter searches for the module in the following sequences
1. The current directory.
2. If the module is not found, Python then searches each directory in the shell variable PYTHONPATH.
...Lib\site.py
Add sys.path.append("path contain modules")
3. If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.
The module search path is stored in the system module sys as the sys.path variable. The sys.path variable contains the current directory, PYTHONPATH, and the installation-dependent default. 
"""

#!/usr/bin/python

# Import module support
#import support #1. loads a Python module into its own namespace: support.pyc is created. To access a method: support.print_func("Zara")
#from support import print_func, person1  #2. loads a Python module into the current namespace, so that you can refer to it without the need to mention the module name: print_func("Zara") instead of support.print_func("Zara") if use import support
import support as s #3. Use alias, can put in if...else (below)
"""
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw
"""
import os, sys #os (C:\Python27\Lib)contains functions to get information on local directories, files, processes, and environment variables.
lib_path = os.path.abspath(os.path.join('/modules'))# lấy ra đường dẫn đến thư mục modules ở trong projetc hiện hành
sys.path.append(lib_path)# thêm thư mục cần load vào trong hệ thống
# import
#from modules.support import *

# Now you can call defined function that module as follows
print(dir()) #the list of names inside the current scope: ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'lib_path', 'os', 'support', 'sys']

s.print_func("Zara") #import support, use support.function_name
s.print_func("Zara2")
print(dir())
b = s.person1["age"] #access to a variable on support module: use support.person1 if import
print(b) #36
print(dir()) #['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'b', 'lib_path', 'os', 'support', 'sys']
import math 
content = dir(math)
print (content)
print(dir())

print ('__package__:',__package__) #('__package__:', None)
print ('__builtins__:',__builtins__) #('__builtins__:', <module '__builtin__' (built-in)>)
print ('__doc__:',__doc__) #first content under the block which first start and end with """
print ('__file__:',__file__) #Print file name: ('__file__:', 'module.py')
print ('__name__:',__name__) #('__name__:', '__main__') as this file is called first. If it called as module from another file, it's have value is file name = module
