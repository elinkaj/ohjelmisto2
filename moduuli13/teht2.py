import mysql.connector
from flask import Flask, Response
import json

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user='root',
    password='Chica02!',
    autocommit=True
    )

@app.route('/kenttä/<icao>')
def haeKentta(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident = '" + icao + "'"
    print(sql)
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchone()
    print(tulos)
    return tulos


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)