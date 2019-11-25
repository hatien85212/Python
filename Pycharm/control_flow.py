def if_stat():
    x = int(raw_input("Please enter an integer: "))
    if x < 0:
         x = 0
         print('Negative changed to zero')
    elif x == 0:
         print('Zero')
    elif x == 1:
         print('Single')
    else:
         print('More')

def for_state():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))
    for w in words[:]:  # Loop over a slice copy of the entire list.
        if len(w) > 6:
            words.insert(0, w) #insert word whose len is large than 6 at index 0
    print(words)
    for i in range(len(words)): #range([start,] stop [, step]) -> range object
        print(i,words[i])
def break_prime_number():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n / x
                break
        else: #runs when no break occurs
            # loop fell through without finding a factor
            print n, 'is a prime number'
def continue_even_number():
    for num in range(2, 10):
        if num % 2 == 0:
            print "Found an even number", num
            continue #continue next iteration in the loop: don't execute the next statement
        print "Found a number", num
def pass_stat(): #pass statement means do nothing
    pass
def while_fib(n):# write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    #i = 0
    while a <= n:
        print(str(a) + "\n")
        a, b = b, a + b
        #i += 1


for_state()
break_prime_number()
continue_even_number()
pass_stat()
if __name__ == '__main__':
    while_fib(500)

print(range(5,10)) #1range([start,] stop [, step]) -> range object
