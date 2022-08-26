# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class DirectoryName(Enum):
    ASSETS = 'assets'
    SIGNALS = 'signals'
    EXCELS = "excels"
