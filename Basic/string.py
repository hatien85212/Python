#!/usr/bin/python
# -*- coding: ascii -*-
"""
- get length: len(a)
- trim text at the beginning: a.strip()
- get letter at specific position
+ 1 letter: a[index]
+ sub set: a[from:to] (to: don't include)
- upper and lower: a.lower(), b.upper()
- slit: a.split()
- replac A by B: a.replace("A","B")
- Convert number to string: ???

print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string
"""
#Unicode: This Python file uses the following encoding: utf-8
""" Put at the 1st or 2nd line: This Python file uses the following encoding: utf-8
The built-in function unicode() provides access to all registered Unicode codecs (COders and DECoders). Some of the more well known encodings which these codecs can convert are Latin-1, ASCII, UTF-8, and UTF-16. The latter two are variable-length encodings that store each Unicode character in one or more bytes. The default encoding is normally set to ASCII, which passes through characters in the range 0 to 127 and rejects any other characters with an error. When a Unicode string is printed, written to a file, or converted with str(), conversion takes place using this default encoding.
"""
x= u"abc" #u is unicode before the single quote
print(u"abc") #abc
print(x) #'abc' when runing on python command, but running file is abc
print("S'ome method with string")
x = ur'Hello\\u00200World!'
#x = u'Hello World !'
print("Python Unicode-Escape encoding: " + x) #Hello World! The escape sequence \u0020 indicates to insert the Unicode character with the ordinal value 0x0020 (the space character) at the given position.
print("Python Unicode-Escape encoding: " + u'Hello\u0020World !') #Hello World! \u0020: ,


a = "Hello, World!"
print(a[1:]) #output: e
print("=== Last char:" + a[-1]) #output: e
print("=== Third-last to the end: " + a[-3:]) #ld!
b = "Hello, World! "
print(b[2:5]) #ouput:llo  5 (not included)

print(b+ "after removing spaces at begining or the end:" + b.strip()) # returns "Hello, World!"  --> strip() method removes any whitespace from the beginning or the end
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J")) #'str' object does not support item assignment: a[0]="J". Can chang by a="J"+a[1:]
print(a.split(",")) # returns ['Hello', ' World!']

c= 'spam eggs' # single quotes
print(c)
c='doesn\'t'  # use \' to escape the single quote...
print(c)
c="doesn't"  # ...or use double quotes instead
print(c)
c='"Yes," they said.'
print(c)
c="\"Yes,\" they said."
print(c)
c='"Isn\'t," they said.'
print(c)
#new line
c = 'First line.\nSecond line.'  # \n means newline
print(c)
c=r'C:\some\name' # note the r before the quote to save all
#print r'C:\some\name'
print(c)
c = """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
print(c)
c=3 * 'un' + 'ium' # 3 times 'un', followed by 'ium'
print(c)
c='Py'  'thon' #Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print(c)
#use () to concatenate content
c = ('Put several strings within parentheses '
     'to have them joined together.')
print(c)
prefix='Py'
print(prefix + 'thon')
#Command-line String Input by using the input() method
#print("Enter your name:")
#x = input()
#print("Hello, ", x)
