# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class YieldActions(Enum):
    SELL = 'Yield Sell'
    BUY = 'Yield Buy'
