# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class ActionColors(Enum):
    OPEN_BUY = '#FFD93D'
    CLOSE_BUY = '#062C30'
    OPEN_SELL = '#FF5F00'
    CLOSE_SELL = '#4700D8'
