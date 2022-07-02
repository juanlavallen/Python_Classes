### Lambdas ###

# function normal
def add(a, b): return a + b

#function lambda
add = lambda a, b: a + b
print(add(10, 20))

### args - kwargs ###

def add_args(*args):
    total = 0
    for n in args:
        total +=  n
    return print('Total:', total) 
    
add_args(1, 2, 3, 4, 5)