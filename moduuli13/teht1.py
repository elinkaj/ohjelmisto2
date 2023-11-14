from flask import Flask, Response
import json

app = Flask(__name__)

def alkuluku(nro):
    if nro <= 1:
        return False
    for i in range(2, int(nro**0.5) + 1):
        if nro % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    try:
        if alkuluku(luku):
            tilakoodi = 200
            vastaus = {
                "Number": luku,
                "isPrime": True
            }
        else:
            tilakoodi = 200
            vastaus = {
                "Number": luku,
                "isPrime": False
            }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
