liczba = 1
slowo = 'slowo'

def foo(num1, num2, num3):
    print(num1 + num2 + num3)

foo(1,2,3)

class Robot: 
    name = 'Mike'

    def __init__(self, age):
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def greet(self):
        print('Hello, my name is {} and I\'m {} years old'.format(self.get_name(), self.get_age()))

print('Tutaj tworze robota')
robot = Robot(20)
print('Tutaj robot jest juz stworzony')
print('teraz pytam robota o imie')
print(robot.name)
print('Teraz zapytam robota o wiek')
print(robot.age)

robot.greet()

l = [1,2,3,4,5,6,7,8]
for x in l:
    if x == 1:
        print('zamiana')
    else:
        print(x)
    if x in [4,5,6]:
        print('hehe')

