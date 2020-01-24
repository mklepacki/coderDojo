# FizzBuzz 
# program wypisuje liczby od 1 do 100000000
# Jesli liczba jest podzielna przez 3 wyswietla Fizz
# Jesli liczba jest podzielna przez 5 wyswietla Buzz
# Jesli jest podzielna przez 3 i 5 to wyswietla FizzBuzz
# Jesli nie jest podzielna przez zadna z tych liczb wyswietla siebie
# Przyklad: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, ...
# --------------------------------



# Implement a program that translates from English to Pig Latin.

# Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below), but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

# Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
# Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. Consonant sounds can be made up of multiple consonants, a.k.a. a consonant cluster (e.g. "chair" -> "airchay").
# Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
# Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
# Stworz program ktory uzywa tylko pierwszej reguly. Vowel = samogloska
# ala = alaay
# kot otkay
# Ala ma kota => Alaay amay otakay

s = 'Ala ma kota'
# def podziel_na_slowa(s):
#     temp_str = ''
#     l = []
#     for letter in s:
#         if letter != ' ':
#             temp_str += letter
#         if letter == ' ':
#             l.append(temp_str)
#             temp_str = ''
#     l.append(temp_str)
#     return l
# print(podziel_na_slowa(s))
# l = s.split(' ')
# print(l[0])
# print(l[0][0])
# word = 'Slowo'
# print(word[0])

# #Slicing
# s = '0123456789'
# print(s[1:])
# new_s = s[1:] + s[0] + 'ay'
# print(new_s)

# l = ['a', 'b', 'c', 'd']
# s = 'zzzz'.join(['asd', 'zxc'])
# print(s)

# Given a string of digits, calculate the largest product for a contiguous substring of digits of length n.
# For example, for the input '1027839564', the largest product for a series of 3 digits is 270 (9 * 5 * 6), and the largest product for a series of 5 digits is 7560 (7 * 8 * 3 * 9 * 5).
# Note that these series are only required to occupy adjacent positions in the input; the digits need not be numerically consecutive.
# For the input '73167176531330624919225119674426574742355349194934', the largest product for a series of 6 digits is 23520.

digits = '1027839564'
first = '102'
second = '027'
third = '278'


substring = digits[0:3]
temp_int = 1
for x in third:
    temp_int *= int(x)
# print(temp_int)
# print(digits[1:4])
# print(digits[2:5])
def largest_product(digits, substring_length):
    products = []
    for x in range(len(digits)-substring_length+1):
        substring = digits[x:x+substring_length]
        substring_multi = 1
        for i in substring:
            substring_multi *= int(i)
        products.append(substring_multi)
    return max(products)

print(largest_product(digits, 5))    
