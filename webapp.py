from flask import Flask
import requests

app = Flask (__name__)

API_KEY="378e3722-bb85-4e3c-9599-ecf118cf25ab"

@app.route("/")
def hello():
    r = requests.get('https://api.opendota.com/api/matches/271145478?api_key=378e3722-bb85-4e3c-9599-ecf118cf25ab')

    return "Hello world " + str(r.status_code)

if __name__ == '__main__':
    app.run()