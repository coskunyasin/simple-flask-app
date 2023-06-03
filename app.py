from flask import Flask
from pygelf import GelfTcpHandler
import logging
import os

app = Flask(__name__)

@app.route("/ping")
def hello():
    return "pong"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.addHandler(GelfTcpHandler(host='192.168.49.1', port=12201))
logger.info('hello gelf')
