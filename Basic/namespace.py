a_num = 10
print (dir()) # ['__builtins__' .... '__spec__', 'a_num'] #global
def some_func():
    b_num = 11
    print(dir()) #['b_num'] --> local namespace, inside a function
print(dir())     
some_func() # ['b_num'] --> local namespace, Created when a function is called, end when function returns

print(dir())
 
dir()
# ['__builtins__' ... '__spec__', 'a_num', 'some_func'] #global

def outer_func():
    c_num = 12
    def inner_func():
        d_num = 13
        print(dir(), ' - names in inner_func') #(['d_num'], ' - names in inner_func')
    e_num = 14
    inner_func()
    print(dir(), ' - names in outer_func') #(['c_num', 'e_num', 'inner_func'], ' - names in outer_func')
print(dir())
outer_func()
# ['d_num']  - names in inner_func
# ['c_num', 'e_num', 'inner_func']  - names in outer_func
print('==========')
a_num = 10
b_num = 11
 
def outer_func():
    global a_num
    a_num = 15
    b_num = 16
    def inner_func():
        #global a_num
        a_num = 20
        b_num = 21
        print('a_num inside inner_func :', a_num)
        print('b_num inside inner_func :', b_num)
    inner_func()
    print('a_num inside outer_func :', a_num)
    print('b_num inside outer_func :', b_num)
     
outer_func()
print('a_num outside all functions :', a_num)
print('b_num outside all functions :', b_num)
 
# a_num inside inner_func : 20
# b_num inside inner_func : 21
 
# a_num inside outer_func : 20
# b_num inside outer_func : 16
 
# a_num outside all functions : 20
# b_num outside all functions : 11