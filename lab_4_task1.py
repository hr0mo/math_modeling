def summa(a):
    b0 = 0
    for i in range(0, len(a), 1):
        b0 = b0 + a[i]
    print(b0 / len(a))
a = [7, 8, 9, 6]
summa(a)