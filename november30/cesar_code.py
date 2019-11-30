import string
# Jesli przesuniecie to 1, to A -> B, B -> C, D -> E itd

def cesar_code(message, num):
    interpunkcja = list(string.punctuation) + [' ']
    if num > 26:
        num = num % 26
    encrypted_messasge = ''
    for letter in message:
        if letter in interpunkcja:
            encrypted_messasge += letter
            continue
        letter_ord = ord(letter)
        letter_ord += num
        if letter_ord > 122:
            letter_ord -= 26
        character = chr(letter_ord)
        encrypted_messasge += character

    return encrypted_messasge

def decypher_codde(encrypted_message, num):
    message = ''

    # wasz kod

    return message

# cesar_code('abc', 1) -----> 'bcd'
# Example
print('To jest warotsc ord() litery a')
print(ord('a'))
print('To jest wartosc chr() liczby 97')
print(chr(97))

print('Przykladowa transformacja a o 1')
letter = 'a'
letter = ord(letter)
letter += 1
letter = chr(letter)
print(letter)


print('Przykladowe przesuniecie dla litery z')
letter = 'z'
letter = ord(letter)
print('ord litery z:', letter)
letter += 1
letter = chr(letter)
print(letter)
print('wszystkie znaki interpunkcyjne')
print(string.punctuation)
print('Wynik: ')
print(cesar_code('Spotkajmy sie o polnocy', 1))