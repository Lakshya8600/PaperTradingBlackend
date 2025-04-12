from flask import Flask , jsonify
import yfinance as yf
from datetime import date
import pandas as pd

app = Flask(__name__)

@app.route('/info/<name>/<period>/<duration>')
def get_info(name, period, duration):
    data = yf.download(tickers=name+".NS",period="1mo" , interval=duration)
    # data = yf.download(tickers=name+".NS",start=dat, end=date.today(), interval=duration)
    # data = yf.download(tickers="RELIANCE.NS",start="2018-01-01", end=date.today(), interval='1d',)
    data = data.reset_index()
    print(data)

        # f'Name: {name}<br>'
        # f'Date: {date}<br>'
        # f'Duration: {duration} minutes'
    # return "jsonify(data)"
    # result = data.to_dict(orient='records')
    return data.to_json()

if __name__ == '__main__':
    app.run(debug=True)