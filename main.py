'''
2. Feladat
Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. A bekérés akkor fejeződjön be, amikor a felhasználó intervallumon kívüli értéket ad meg! A program írja ki a megadott intervallumba eső számokat és az összegüket!
'''

lista = []

while True:
    szam = int(input("Kérek egy számot -5-5 között!"))
    if -5 <= szam <= 5:
        lista.append(szam)
    else:
        break

print(lista)

osszeg = 0
for i in lista:
    osszeg += i

print(osszeg)