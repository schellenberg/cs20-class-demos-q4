def square_root(number):
    the_square_root = number / 2
    for value in range(5):
        the_square_root = 0.5 * (the_square_root + number / the_square_root)
    return the_square_root


print(square_root(9))