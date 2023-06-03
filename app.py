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
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFTCPHandler('192.168.49.1', 12201)
my_logger.addHandler(handler)

my_logger.debug('This is a test from a Python script!')
