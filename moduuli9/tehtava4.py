from auto import Auto
import random
import prettytable

def speed():
    return random.randint(100, 200)

def acceleration():
    return random.randint(-10, 15)

auto_lista = []

for i in range(1, 11):
    rekisteri_tunnus = 'ABC-' + str(i)
    huippu_nopeus = speed()
    coche = Auto(rekisteri_tunnus, huippu_nopeus)
    auto_lista.append(coche)

table = prettytable.PrettyTable(["Rekisteritunnus", "Huippunopeus", "Matka", "Nopeus"])
for coche in auto_lista:
    table.add_row([coche.rekisteritunnus, coche.huippunopeus, coche.matka, coche.nopeus])


while True:
    for coche in auto_lista:
        coche.kiihdyta(random.randint(-10, 15))
        coche.kulje(1)

    if any(coche.matka >= 10000 for coche in auto_lista):
        break

    table.clear_rows()
    for coche in auto_lista:
        table.add_row([coche.rekisteritunnus, coche.huippunopeus, coche.matka, coche.nopeus])

print(table)