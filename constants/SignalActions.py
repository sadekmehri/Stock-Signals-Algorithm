# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class SignalActions(Enum):
    SELL = 'Sell Signal'
    BUY = 'Buy Signal'
