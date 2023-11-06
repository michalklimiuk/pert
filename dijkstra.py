import sys
import time

t1 = time.time()

nazwa_pliku = "MinPaths_data5.txt"  # odczyt danych z pliku o wskazanej nazwie

with open(nazwa_pliku, 'r') as file:
    N = int(file.readline())
    tablica = [0] * N
    for i in range(len(tablica)):
        tablica[i] = list(map(int, file.readline().strip().split()))

zrodlo = 0  # inicjalizacja punktu początkowego oraz listy odległości o odczytanym z pliku rozmiarze i listy odwiedzonych punktów
odleglosci = [float('inf')] * N
odwiedzone = [False] * N
odleglosci[zrodlo] = 0

for _ in range(N): # szukanie wierzchołka o najmniejszej odległości, który nie został jeszcze odwiedzony
    min_odleglosc = sys.maxsize
    min_index = -1
    for i in range(N):  # iteracja po kazdym wierzchołku aby znaleźć najmniejszą odległość
        if not odwiedzone[i] and odleglosci[i] < min_odleglosc:
            min_odleglosc = odleglosci[i]
            min_index = i

    odwiedzone[min_index] = True

    for i in range(N):  # aktualizacja odległości dla sąsiadów bieżącego wierzchołka
        if not odwiedzone[i] and tablica[min_index][i] > 0:
            nowa_odl = odleglosci[min_index] + tablica[min_index][i]
            if nowa_odl < odleglosci[i]:
                odleglosci[i] = nowa_odl

for i in range(len(odleglosci)):
        print(f"Najkrótsza odległość z punktu {zrodlo} do {i} to {odleglosci[i]}")

t2 = time.time()
taken_time = t2 - t1
print("Czas działania programu:", taken_time)
