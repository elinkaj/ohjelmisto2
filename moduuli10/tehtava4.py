import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, aika):
        lisa_matka = self.nopeus * aika
        self.matka = self.matka + lisa_matka
        return


class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            nopeus_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeus_muutos)
            auto.kulje(1)
        return

    def tulosta_tilanne(self):
        print(f"Rekkari \tMax\t Speed\t Matka")
        for auto in self.autolista:
            print(f"{auto.rekisteritunnus} \t\t{auto.huippunopeus} \t{auto.nopeus} \t{auto.matka} ")
        return

    def kilpailu_ohi(self):
        kilpailu_paattynyt = False

        for auto in self.autolista:
            if auto.matka >= self.pituus:
                kilpailu_paattynyt = True
                break
        return kilpailu_paattynyt

    def lajittelija(self, kilpailija):
        return kilpailija.matka

    def tulosta_lopputilanne(self):
        self.autolista.sort(reverse=True, key=self.lajittelija)
        self.tulosta_tilanne()
        return


kilpailijat = []

for nro in range(1, 11):
    rekisteritunnus = "ABC-" + str(nro)
    maxnopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, maxnopeus)
    kilpailijat.append(auto)

kisa = Kilpailu("Suuri romuralli", 8000, kilpailijat)
kisa_aika = 0
kisa_kaynnissa = True


while kisa_kaynnissa:
    kisa.tunti_kuluu()
    kisa_aika += 1
    if kisa.kilpailu_ohi() == True:
        kisa_kaynnissa = False
    if kisa_aika % 10 == 0:
        print(f"\n-- Tilanne {kisa_aika} tunnin jälkeen: --")
        kisa.tulosta_tilanne()


print(f"\n--- Kisa on päättynyt, se kesti {kisa_aika} tuntia ---")
print("Alla ovat kilpailun lopputulokset: \n")
kisa.tulosta_lopputilanne()