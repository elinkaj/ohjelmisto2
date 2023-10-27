from hissi import Hissi
class Talo:
    def __init__(self, alin, ylin, hissien_lukumaara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissien_lukumaara):
            hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)
        print(f"Hissi {hissin_numero} on nyt halutussa kerroksessa {kohdekerros}")

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)
        print("Palohälytys! Hissit ovat nyt 1. kerroksessa.")

    def kerro_hissien_sijainnit(self):
        print("Talon hissien sijainnit:")
        for i in range(len(self.hissit)):
            print(f"Hissi {i+1} on kerroksessa {self.hissit[i].sijainti}")


Talo = Talo(1, 13, 3)


Talo.aja_hissia(1, 7)
Talo.aja_hissia(2, 2)
Talo.kerro_hissien_sijainnit()


Talo.palohalytys()
Talo.kerro_hissien_sijainnit()