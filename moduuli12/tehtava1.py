import requests


pyynto = "https://api.chucknorris.io/jokes/random"


print(pyynto)

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print("Tässä sinulle Chuck Norris vitsi, ole hyvä")
        print(json_vastaus["value"])
except requests.exceptions.RequestException as e:

    print("Hakua ei voitu suorittaa.")

print("Hakutapahtuma on ohi.")