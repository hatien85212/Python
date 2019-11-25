"""
A module containing the fibonacci
function. 
"""
 
def fib(n):
    a, b = 0, 1
    while b < n:
        print (b,)
        (a, b) = (b, a + b) #the expressions on the right hand side are evaluated before being assigned to the left hand side. So it is equivalent to:
 
 
# testing
 
if __name__ == '__main__':
   fib(500)