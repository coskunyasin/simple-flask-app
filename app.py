from flask import Flask
import logging
import graypy
import os

app = Flask(__name__)

@app.route("/ping")
def hello():
    return "pong"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
my_logger = logging.getLogger('test_logger')
handler = graypy.GELFTCPHandler('172.20.0.4', 12201)
while True:
    my_logger.debug('Danger, Will Robinson, Danger!') 
    time.sleep(1)
