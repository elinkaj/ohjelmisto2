from auto import Auto

car = Auto(input_rekisteritunnus='ABC-123', input_huippunopeus=142)

car.kiihdyta(30)
car.kiihdyta(70)
car.kiihdyta(50)
car.testi()

car.kiihdyta(-200)
car.testi()