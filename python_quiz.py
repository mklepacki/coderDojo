s = 'Ala ma kota'
n = s.replace('a', 'x')
print(n)

l = [1,2,3,4]
l[2] = 4
print(l)

new_set = {1,2,3}
print(type(new_set))

second_set = set(l)
print(second_set)

l2 = ['ala', 'ma', 'kota', 'ala']
l2 = list(set(l2))
print(l2)
