import requests

def letter_count(text, letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total_letters_seen = 0
    specific_letter_seen = 0
    
    for character in text:
        if character in alphabet:
            total_letters_seen += 1
            if character == letter:
                specific_letter_seen += 1
    
    percent = (specific_letter_seen/total_letters_seen) * 100
    percent = round(percent, 2)
    print(f'{letter}: {percent}%')

def letter_frequency(text):
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        letter_count(text, letter)

url = 'https://www.gutenberg.org/files/1342/1342-0.txt'
to_analyse = str(requests.get(url).content)

letter_frequency(to_analyse)
