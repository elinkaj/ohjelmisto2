from auto import Auto

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.kapasiteetti = kapasiteetti
