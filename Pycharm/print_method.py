x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...' #repr(a): convert number, adds string quotes and backslashes:
print s #The value of x is 32.5, and y is 40000...
for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),
    # Note trailing comma on previous line
    print repr(x*x*x).rjust(4)