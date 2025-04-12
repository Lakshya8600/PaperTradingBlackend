from flask import Flask , jsonify
import yfinance as yf
from datetime import date
import pandas as pd

app = Flask(__name__)

@app.route('/info/<name>/<perio>/<duration>')
def get_info(name, perio, duration):

    data = yf.download(tickers=name+".NS",period=perio , interval=duration)
    # data = yf.download(tickers=name+".NS",start=dat, end=date.today(), interval=duration)
    # data = yf.download(tickers="RELIANCE.NS",start="2018-01-01", end=date.today(), interval='1d',)
    data = data.reset_index()
        # f'Name: {name}<br>'
        # f'Date: {date}<br>'
        # f'Duration: {duration} minutes'
    # return "jsonify(data)"
    # result = data.to_dict(orient='records')
    return data.to_json()

if __name__ == '__main__':
    app.run(debug=True)