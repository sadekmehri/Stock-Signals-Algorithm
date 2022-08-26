# -*- coding: utf-8 -*-
import logging
import sys

from alpha_vantage.timeseries import TimeSeries
from console.readFromConsole import readStockSymbol
from constants.Stocks import Stocks
from validators.apiKeyValidator import isKeyProvided


# Get alphaVantage instance
def initializeAlphaVantage():
    try:
        isKeyProvided()
        return TimeSeries(key=Stocks.API_KEY.value, output_format='pandas')
    except Exception as ex:
        raise Exception(ex)


# Get alpha - vantage data stock by giving a symbol
def getAlphaVantageDataStock(timeSeries: TimeSeries) -> list:
    while True:
        try:
            symbol = readStockSymbol()
            logging.info(f'Launching search process for {symbol} data. Please wait ...')
            data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='1min', outputsize='full')
            logging.info('Success ...')

            return [data, meta_data]
        except Exception as ex:
            logging.error(f"Symbol not found: {ex}!")
            sys.exit(1)
