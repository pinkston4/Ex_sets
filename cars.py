showroom = set()
showroom.add('tesla')
showroom.add('wrx')
showroom.add('sti')
showroom.add('ls430')
showroom.add('tesla')
print(len(showroom))

showroom.add('tesla')
print(showroom)

showroom.update({'civic'})
showroom.update({'accord'})
print(showroom)

showroom.discard('tesla')
print(showroom)

junkyard = {'civic', 'tesla', 'jeep', 'ls460', 'ls430', 'mustang'}
print(showroom & junkyard)

new_showroom = showroom | junkyard
print(new_showroom)

new_showroom.discard('wrx')
print(new_showroom)
