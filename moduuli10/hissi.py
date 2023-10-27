class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = alin

    def kerros_ylos(self):
        if self.sijainti < self.ylin:
            self.sijainti += 1
        print(f"Hissi on nyt {self.sijainti}. kerroksessa")
        return

    def kerros_alas(self):
        if self.sijainti > self.alin:
            self.sijainti = self.sijainti - 1
        print(f"Hissi on nyt {self.sijainti}. kerroksessa")
        return

    def siirry_kerrokseen(self, haluttu_kerros):
        if self.sijainti < haluttu_kerros:
            while self.sijainti < haluttu_kerros:
                self.kerros_ylos()
        elif self.sijainti > haluttu_kerros:
            while self.sijainti > haluttu_kerros:
                self.kerros_alas()
        return
