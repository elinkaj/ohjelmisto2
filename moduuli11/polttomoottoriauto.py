from auto import Auto

class Polttomoottoriauto(Auto):
    def __init__(self, input_rekisteritunnus, input_huippunopeus, tankki):
        super().__init__(input_rekisteritunnus, input_huippunopeus)
        self.tankki = tankki