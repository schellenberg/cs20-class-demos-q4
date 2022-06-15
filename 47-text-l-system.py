def apply_rules(letter):
    if letter == 'A':
        return 'B'
    elif letter == 'B':
        return 'AB'
    else:
        return letter
    
def process_string(the_string):
    transformed = ''
    for letter in the_string:
        transformed = transformed + apply_rules(letter)
    return transformed

def create_l_system(number_of_iterations, axiom):
    the_string = axiom
    for counter in range(number_of_iterations):
        the_string = process_string(the_string)
    return the_string

print(create_l_system(10, 'A'))
    
    