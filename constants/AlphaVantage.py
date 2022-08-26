# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class AlphaVantageDataFields(Enum):
    OPEN = '1. open'
    HIGH = '2. high'
    LOW = '3. low'
    CLOSE = '4. close'
    VOLUME = '5. volume'
    DATE = 'date'


@unique
class AlphaVantageMetaDataFields(Enum):
    INFORMATION = '1. Information'
    SYMBOL = '2. Symbol'
    LAST_REFRESHED = '3. Last Refreshed'
    INTERVAL = '4. Interval'
