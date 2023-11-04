class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(self.nimi, self.kirjoittaja, self.sivumaara)

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(self.nimi, self.paatoimittaja)



kirja = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
kirja.tulosta_tiedot()
lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
lehti.tulosta_tiedot()