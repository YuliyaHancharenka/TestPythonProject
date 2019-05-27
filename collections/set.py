bri = {'Бразилия', 'Россия', 'Индия'}

print('Индия' in bri)
print('США' in bri)

bric = bri.copy()

bric.add('Китай')
print(bric.issuperset(bri))

bri.remove('Россия')

print(bri & bric) # the same as below
print(bri.intersection(bric)) # the same as above

print(bri.pop())
print(bri.pop())

print()

if len(bri) == 0:
    print("Empty")
else:
    for item in bri:
        print(item)