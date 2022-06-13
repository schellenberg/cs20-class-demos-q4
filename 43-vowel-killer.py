def vowel_killer(word):
    '''Returns the string, with all vowels removed.'''
    vowels = "aeiouyAEIOUY"
    new_string = ""
    for letter in word:
        if letter not in vowels:
            new_string = new_string + letter
    return new_string
        
print(vowel_killer("walter murray")) #wltr mrr
print(vowel_killer("computer science")) #cmptr scnc