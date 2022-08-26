# -*- coding: utf-8 -*-
from time import gmtime, strftime


# Get current date time
def getCurrentDateTime():
    dateTime = gmtime()
    return [strftime("%Y-%m-%d", dateTime), strftime("%H_%M_%S", dateTime)]
