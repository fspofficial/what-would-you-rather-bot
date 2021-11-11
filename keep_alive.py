from flask import Flask
from threading import Thread

app = Flask('')
web = 'REEEEEEEEEEEEEEEEEEEEEE! This is WUMPUS TEXT!'

@app.route('/')
def home():
    return web

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()