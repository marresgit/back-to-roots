from flask import Flask
import requests
import config
import json

app = Flask (__name__)

@app.route("/")
def index():
    rSteveAccount = requests.get(f'https://api.opendota.com/api/players/62297546/matches?api_key={config.API_KEY}')
    # return r.json()
    # hero_id =

    for request in rSteveAccount.json():
        return request


@app.route("/heroes")
def heroes():
    rDotaHeroes = requests.get(f'https://api.opendota.com/api/heroes?api_key={config.API_KEY}')
    return rDotaHeroes.json()



if __name__ == '__main__':
    app.run(debug=True)