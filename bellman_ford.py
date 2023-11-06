nazwa_pliku = "MinPaths_data5.txt"  # odczyt danych z pliku o wskazanej nazwie

import time

t1 = time.time()

with open(nazwa_pliku, 'r') as file:
    N = int(file.readline())
    tablica = [0] * N
    for i in range(len(tablica)):
        tablica[i] = list(map(int, file.readline().strip().split()))

zrodlo = 0  # inicjalizacja punktu początkowego i listy odległości o odczytanym z pliku rozmiarze 

odleglosci = [float('inf')] * N
odleglosci[zrodlo] = 0

for _ in range(N - 1):  # relaksacja krawędzi N-1 przy każdej z krawędzi
    for i in range(N):
        for j in range(N):
            if tablica[i][j] != 0 and odleglosci[i] + tablica[i][j] < odleglosci[j]:
                odleglosci[j] = odleglosci[i] + tablica[i][j]

for i in range(N):  # sprawdzenie obecności cykli o ujemnej wadze
    for j in range(N):
        if tablica[i][j] != 0 and odleglosci[i] + tablica[i][j] < odleglosci[j]:
            print("Graf zawiera cykl o ujemnej wadze")
            break
    else:
        continue
    break
else:
    for i in range(len(odleglosci)):
        print(f"Najkrótsza odległość z punktu {zrodlo} do {i} to {odleglosci[i]}")

t2 = time.time()
taken_time = t2 - t1
print("Czas działania programu:", taken_time)
