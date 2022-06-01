# initialize the accumulator variable
# repeat:
#     modify the accumulator variable

# when the loop terminates the accumulator has
#  the correct value

def sum_to(number):
    the_sum = 0
    for value in range(number+1):
        the_sum = the_sum + value
    return the_sum


def square(number):
    the_square = 0
    for value in range(number):
        the_square = the_square + number
    return the_square

print(square(4))
    
    
    
    
    
    
