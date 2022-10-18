print('Введите первый член прогрессии:')
b0 = int(input())
print('Введите знаменатель прогрессии:')
q = int(input())
print('Введите количество членов прогрессии:')
n = int(input())

for i in range(0, n, 1):
  b1 = b0 * q
  print(b1)
  b0 = b1
  





