class Auto:
    def __init__(self, input_rekisteritunnus, input_huippunopeus):
        self.rekisteritunnus = input_rekisteritunnus
        self.huippunopeus = input_huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0


    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

    def testi(self):
        print(f'Rekisterinumero: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus}, Kuljettu matka:{self.matka}, Tämän hetken nopeus:{self.nopeus}')