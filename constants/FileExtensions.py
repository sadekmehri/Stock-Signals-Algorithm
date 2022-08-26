# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class FileExtensions(Enum):
    EXCEL = 'xlsx'
    PNG = 'png'
