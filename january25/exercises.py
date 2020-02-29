"""
1. Introduction
Reverse a string

For example: input: "cool" output: "looc"
---------------------------------------------------------------------------------------------------

1. Wprowadzenie
Odwróć ciąg

Na przykład: input: „cool” output: „looc”

################################################################
2. Introduction
Given a year, report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.

If your language provides a method in the standard library that does this look-up, pretend it doesn't exist and implement it yourself.

Notes
Though our exercise adopts some very simple rules, there is more to learn!

For a delightful, four minute explanation of the whole leap year phenomenon, go watch this youtube video.
https://www.youtube.com/watch?v=xX96xng7sAE
-----------------------------------------------------------------------------
2. Wprowadzenie 
Biorąc pod uwagę rok, zgłoś, czy jest to rok przestępny.

Problem polega na tym, że w kalendarzu gregoriańskim następuje rok przestępny:

każdego roku, który jest równomiernie podzielny przez 4
   z wyjątkiem każdego roku, który dzieli się równomiernie przez 100
     chyba że rok jest również podzielny równo przez 400
Na przykład 1997 nie jest rokiem przestępnym, ale 1996 jest. 1900 to nie rok przestępny, ale 2000 rok.

Jeśli Twój język udostępnia metodę w standardowej bibliotece, która wykonuje to wyszukiwanie, udawaj, że ona nie istnieje i zaimplementuj ją samodzielnie.

Notatki
Chociaż w naszym ćwiczeniu przyjęto kilka bardzo prostych zasad, jest wiele do nauczenia się!

Aby uzyskać wspaniałe, czterominutowe wyjaśnienie fenomenu całego roku przestępnego, obejrzyj ten film na youtube.
https://www.youtube.com/watch?v=xX96xng7sAE


#############################################################################
3. Introduction
Write a function that returns the earned points in a single toss of a Darts game.

Darts is a game where players throw darts to a target.

In our particular instance of the game, the target rewards with 4 different amounts of points, depending on where the dart lands:

If the dart lands outside the target, player earns no points (0 points).
If the dart lands in the outer circle of the target, player earns 1 point.
If the dart lands in the middle circle of the target, player earns 5 points.
If the dart lands in the inner circle of the target, player earns 10 points.
The outer circle has a radius of 10 units (This is equivalent to the total radius for the entire target), the middle circle a radius of 5 units, and the inner circle a radius of 1. Of course, they are all centered to the same point (That is, the circles are concentric) defined by the coordinates (0, 0).

Write a function that given a point in the target (defined by its real cartesian coordinates x and y), returns the correct amount earned by a dart landing in that point.
------------------------------------------------------------------------------------------------------------------
3. Wprowadzenie
Napisz funkcję, która zwraca zdobyte punkty w jednym rzucie gry w rzutki.

Rzutki to gra, w której gracze rzucają rzutkami w cel.

W naszym szczególnym przypadku gry cel nagradza 4 różnymi ilościami punktów, w zależności od tego, gdzie wyląduje strzałka:

Jeśli rzutka wyląduje poza celem, gracz nie zdobywa punktów (0 punktów).
Jeśli strzałka wyląduje w zewnętrznym okręgu celu, gracz otrzymuje 1 punkt.
Jeśli strzałka wyląduje w środkowym kółku celu, gracz zdobywa 5 punktów.
Jeśli strzałka wyląduje w wewnętrznym okręgu celu, gracz zdobywa 10 punktów.
Zewnętrzny okrąg ma promień 10 jednostek (jest to równoważne z całkowitym promieniem całego celu), środkowy okrąg ma promień 5 jednostek, a wewnętrzny okrąg ma promień 1. Oczywiście wszystkie są wyśrodkowane na ten sam punkt (to znaczy koła są koncentryczne) zdefiniowany przez współrzędne (0, 0).

Napisz funkcję, która podała punkt w celu (zdefiniowana przez jego rzeczywiste współrzędne kartezjańskie X i Y - (X,Y) ), zwraca prawidłową kwotę zarobioną przez rzutkę lądującą w tym punkcie.
"""
# s = 'cool'
# print(''.join(reversed(s)))
# print(s[::-1])

import math
import random

def count_score(p):
  # liczyla punkty
  p1 = Point(0,0)
  length = points_length(p1, p)
  if length <=1:
    return 10
  elif length <=5:
    return 5
  elif length <= 10:
    return 1
  else: 
    return 0
  
def points_length(p1, p2):
  # sprawdza w ktorym jest okregu
  length = math.sqrt(math.pow(p2.x - p1.x, 2) + math.pow(p2.y - p1.y, 2))
  return length


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

p1 = Point(0,0)
p2 = Point(10, 10)

def fake_darts_game():
  players = [0,0,0,0]
  for x in range(4):
    for i in range(len(players)):
      x1 = random.randint(0, 8)
      y1 = random.randint(0,8)
      p = Point(x1, y1)
      score = count_score(p)
      players[i] += score
  return players

# counter = 0
# while True:
#   score_list = fake_darts_game()
#   score_list = sorted(score_list)
#   if score_list[3] == 40:
#     print('Scored 40', counter)
#     break
#   else:
#     print(counter)
#     counter += 1

"""
1 2 3           1 4 7
4 5 6   => T => 2 5 8
7 8 9           3 6 9
"""
m = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

# def transpose(m):
#   output_m =[]
#   for x in range(len(m[0])):
#     output_m.append([])
#   for x in range(len(m)):
#     for i in range(len(m[x])):
#       output_m[x] = m[x][i]
#   return output_m
# print(transpose(m))
a = [1, 2, 3]
b = [1, 2, 3, 4, 5]


def rekurencja(n=49):
  pass

def oblicz(n):
    if n==1:
        return -10
    return oblicz(n-1)/-2
# for x in range(1,10):
#     print(oblicz(x))


def zadanie134a(n):
  if n == 1:
    return 4
  return zadanie134a(n-1) + 3

# print(zadanie134a(1))
# print(zadanie134a(2))
# print(zadanie134a(3))

def zadanie134e(n):
  if n == 1:
    return 3
  if n%2 == 0:
    return zadanie134e(n-1) + 2
  else:
    return zadanie134e(n-1) - 1
# print(zadanie134e(1))
# print(zadanie134e(2))
# print(zadanie134e(3))

def zadanie135a(n):
  if n == 1:
    return 2
  return 3*zadanie135a(n-1) + 0.5
# for x in range(1,8):
#   print(zadanie135a(x))


