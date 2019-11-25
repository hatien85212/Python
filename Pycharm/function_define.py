#https://docs.python.org/2/tutorial/controlflow.html#arbitrary-argument-lists
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a + b
    return result

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

r = fib2(200)
print r
#print fib2(200)

r = ask_ok('Do you really want to quit?')
#r = ask_ok('OK to overwrite the file?', 2)
#r = ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
#print r

i = 5

def f(arg=i):
    print arg

i = 6
f() #will print 5


def f(a, L=[]):
    L.append(a)
    return L

print f(1) #[1]
print f(2) #[1,2]
print f(3) #[1,2,3]

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print f2(1) #[1]
print f2(2) #[2]
print f2(3) #[3]

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


def cheeseshop(kind, *arguments, **keywords): #keyword arguments: include key = "value" passed to function
    print "-- I'm sorry, we're all out of", kind #I'm sorry, we're all out of Limburger
    for arg in arguments:
        print arg #It's very runny, sir. It's really very, VERY runny, sir.
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
#shopkeeper='Michael Palin',
#client="John Cleese",
#sketch="Cheese Shop Sketch")

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

It's very runny, sir.
It's really very, VERY runny, sir.

def write_multiple_items(file, separator, *args):#Arbitrary Argument Lists
    file.write(separator.join(args))

#Unpacking Argument Lists
print range(3, 6)             # normal call with separate arguments
[3, 4, 5]
args = [3, 6]
print range(*args)            # call with arguments unpacked from a list
[3, 4, 5]

#In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
def parrot(voltage, state='a stiff', action='voom'):#Keyword Arguments
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"} #Unpacking Argument Lists
parrot(**d) #-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

#4.7.5. Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print f(0) #42
print f(1) #43