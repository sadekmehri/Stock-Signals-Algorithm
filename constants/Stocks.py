# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class Stocks(Enum):
    API_KEY = ''
    TESLA = 'TSLA'
    MICROSOFT = 'MSFT'
    APPLE = 'AAPL'
    AMAZON = 'AMZN'
    NVIDIA = 'NVDA'
    VISA = 'V'
    FACEBOOK = 'META'


@unique
class StockActions(Enum):
    OPEN_SELL = 'Open Sell Action'
    CLOSE_SELL = 'Close Sell Action'
    OPEN_BUY = 'Open Buy Action'
    CLOSE_BUY = 'Close Buy Action'


@unique
class StockIndicators(Enum):
    MOVING_AVERAGE = 20
    STANDARD_DEVIATION_INDICATOR = 'standard_deviation_indicator'
    ROSE_INDICATOR = 'rose_indicator'
    WHITE_INDICATOR = 'white_indicator'
    GREEN_INDICATOR = 'green_indicator'
    GREY_INDICATOR = 'grey_indicator'
