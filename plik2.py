# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = []
#
# for i in list1:
#     list2.append(pow(i, 2))
# print(list2)
# list2 = [x**2 for x in list1]
# print(list2)
# list3 = [3**y for y in range (0, 6)]
# print(list3)
# list4 = [x for x in list2 if x % 2 == 1]
# print(list4)
# list5 = [(x,y) for x in list3 for y in list4]
# print(list5)
# list6 = []
# for x in 13:
#     for y in 14:
#         list6.append(x, y)
# print(list6)
import math


# s1 = {1: 2, 2: 3,3: 4,4: 5}
# s2 = {}
# for key, value in s1.items():
#     s2[value] = key
# print(s1)
# print(s2)
# s3={v: k for k, v in s1.items()}
# print(s3)

# def rownanie_kwadratowe(a, b, c):
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         print('brak pierwiastkow')
#         return 0
#     elif delta == 0:
#         print('jeden pierwiastek')
#         x = (-b) / (2*a)
#         return x
#     elif delta > 0:
#         print('dwa pierwiastki')
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         return x1, x2
#
# print(rownanie_kwadratowe(6, 1, 3))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(1, 4, 2))
#
# def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)
#
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(4,2,6,3))
# print(dlugosc_odcinka(y2=5,y1=5,x2=2,x1=8))
# print(dlugosc_odcinka(3,5,y2=4,y1=3))

# plik = open('pliczek.txt','r', encoding='utf-8')
# znaki = plik.read(10)
#
# linia = plik.readline()
# linie = plik.readlines()
# plik.close()
# print(znaki)
# print(linia)
# print(linie)
#
# for l in linie:
#     print(l)
# plik = open('pliczek.txt', 'a+')
# plik.write('aaaaaaa')
# plik.seek(105)
# znaki = plik.read(10)
# plik.close()

# with open('pliczek.txt', 'r') as f:
#     lines = f.readlines()
# print(lines)

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