# -*- coding: utf-8 -*-
from constants.Stocks import Stocks


# Check if the key is provided
def isKeyProvided() -> None:
    if not Stocks.API_KEY.value:
        raise Exception('Please provide api key in stocks file')
