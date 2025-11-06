def make_adder(n):
    """
    Returns a function that adds n to its argument.
    """
    # Define the function that we will return
    def f(m):
        """
        A function that adds a certain number to its argument.
        """
        return m+n
    # Return the function
    return f

z = make_adder(3)
print(z(12))


def factorial(n):
    """
    Returns n!
    """
    # Handle the base case
    if n == 0:
        return 1
    # Induction step
    return n*factorial(n-1)

print(f"6! is {factorial(6)}")


def fib(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1)+fib(n-2)    

print(fib(9))

#McNuggets_cache = {0:1, 1:2, 2:3, 3:4, 4:5}
#a = 1
#b = 1
#c = 1
#def McNuggets(n)
#    if n > 0 & n%3 == 1
#        McNuggets_cache[1] = 


def my_func():
    y = 'peas'
    print(f'inside the function, x is {x}')
    print(f'inside the function, y is {y}')

x = 'fish'
y = 'chips'
print(f'outside the function, x is {x}')
# call the function
my_func()
print(f'outside the function, x is now {x}')
print(f'outside the function, y is now {y}')
#print(f'outside the function, y is now {y}')


def increment(n):
    print("n brefore:", n)
    n+=1
    print("n after:", n)

a = 4
increment(a)
print(a)




    
    
