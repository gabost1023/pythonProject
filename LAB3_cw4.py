def czytrojkat(a, b, c):
    if max(a, b, c) == a:
        if b**2 + c**2 == a**2:
            print('Trojkat jest prostokatny')
        else:
            print('Trojkat nie jest prostokatny')
    elif max(a, b, c) ==b:
        if a**2 + c**2 == b**2:
            print('Trojkat jest prostokatny')
        else:
            print('Trojkat nie jest prostokatny')
    elif max(a, b, c) == c:
        if a**2 + b**2 == c**2:
            print('Trojkat jest prostokatny')
        else:
            print('Trojkat nie jest prostokatny')

liczba1 = int(input('Podaj bok a: '))
liczba2 = int(input('Podaj bok b: '))
liczba3 = int(input('Podaj bok c: '))

print(czytrojkat(liczba1, liczba2, liczba3))

