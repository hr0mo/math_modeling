a1 = int(input())
a2 = int(input())
if a1 % a2 == 0:
  print('Делится')
else:
  print('Не делится')
b1 = a1 % a2
print('Остаток: ')
print(b1)
b2 = a1//a2
print('Частное:')
print(b2)