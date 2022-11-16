# http://localhost:5000/tospring

from flask import Flask, render_template, request
import requests
import json

import urllib.request

app = Flask(__name__)

@app.route('/gongo/search/keyword/<purpose>/<price>', methods=['GET'])
def spring(purpose,price):

    return "플라스크 응답 확인" + "purpose" +  purpose + price
    


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1",port=5000)