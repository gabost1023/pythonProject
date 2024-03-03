import sys
# a = 56
# print(a)
# print(type(a))
# b= 5.5
# print(b)
# zmienna_tekstowa = 'wizualizacja danych'
# print(zmienna_tekstowa)
# print(type(zmienna_tekstowa))
# e=4
# f=a // b
# print(f)
# g=e**2
# print(g)
# h=pow(e,2)
# print(h)
#
# i=6 ** (1/2)
# j=pow(6,1/2)
# print(i)
# print(j)
#
# k='wizualizacja danych'
# l=' grupa '
# m=2
# print(k+l+str(m))
#
# print('liczba a jest rowna {:d}, liczba b jest rowna {:.2f}'.format(a,b))
#
# zmienna1 = input('Wprowadz liczbe: ')
# zmienna1=int(zmienna1)
# print(zmienna1)
# print(type(zmienna1))

# sys.stdout.write('Wprowadz liczbe: ')
# zmienna2=sys.stdin.readline()
# print(zmienna2 + ' to wartosc zmiennej 2')
# print(type(zmienna2))

# lista = [5, 6.6, 34, 'a','b',[2,3,4],'ab']
# print(lista)
# lista.append(67)
# print(lista)
# lista.insert(2,'c')
# print(lista)
# lista.extend([20,21,22])
# print(lista)
# lista.pop(2)
# print(lista)
# lista.remove([2,3,4])
# print(lista)
# del lista[1]
# print(lista)
# lista.reverse()
# print(lista)
# #lista.sort() #tylko wartosci, ktore da sie porownac

# slownik ={'klucz': 'wartosc', 1: 2, 'a': 5, 4: 'b'}
# print(slownik)
# print(slownik[4])
# slownik[6] = 45
# print(slownik)
# slownik.pop(1)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# del slownik[6]
# print(slownik)

#a = 6
#b = 7

# if a>b:
#     print("a is greater than b")
# elif a<b:
#     print("b is greater than a")
# else:
#     print("a is equal to b")

# a= int(input())
# b= int(input())
# c= int(input())
# d= int(input())
#
# if (a>b) & (c>d):
#     print(a,c)
# else:
#     print(b,d)

# for i in range(2, 8, 2):
#     print(i)
# else:
#     print('koniec petli')

# for i in lista:
#     print(i)

# for i in range(0,5):
#     for j in range(0,5):
#         result=i+j
#         print(result)
#     print('')

# licznik = 0
# while licznik < len(lista):
#     print(lista[licznik])
#     licznik +=1
# else:
#     print('koniec petli')

# licznik=0
# while licznik != 10:
#     if licznik == 7:
#         print(licznik)
#         break   #continue
#     else: licznik += 1
# else:
#     print('licznik')

#zad1
lista=[1,2,3,4,5,6]
a= int(input())

licznik= int(0)

while licznik < len(lista):
    if (a-lista[licznik]) == 0:
        print('Tak')
        break
    licznik +=1
else:
    print('Nie')
