from flask import Flask
import requests
import config

app = Flask (__name__)

@app.route("/")
def hello():
    r = requests.get(f'https://api.opendota.com/api/players/62297546/matches?api_key={config.API_KEY}')

    return "Hello world " + str(r.status_code) + " " + str(r.json())

if __name__ == '__main__':
    app.run()