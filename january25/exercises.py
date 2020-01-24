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