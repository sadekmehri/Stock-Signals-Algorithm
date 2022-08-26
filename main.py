#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Digitarab"
__copyright__ = "Copyright 2022, Digitarab"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Digitarab"
__status__ = "Production"

import logging
import sys
from alpha_vantage.timeseries import TimeSeries
from converters.dfConverter import convertDfToExcel
from utils.alphaVantageUtil import getAlphaVantageDataStock, initializeAlphaVantage
from utils.calculateIndicatorsUtil import calculateIndicators
from utils.defineActionIndicatorsUtil import defineActionIndicators
from utils.initLoggerUtil import initLogger
from utils.signalActionsChartUtil import drawSignalActionsChart
from utils.yieldSignalUtil import calculateYieldSignalAction

if __name__ == '__main__':
    try:
        # Add custom logger
        initLogger()
        # Get alpha vantage instance
        ts: TimeSeries = initializeAlphaVantage()
        # Read stock symbol and check if it is available
        data, meta_data = getAlphaVantageDataStock(timeSeries=ts)
        # Calculate indicators white-indicator, green-indicator, grey-indicator, rose-indicator
        df = calculateIndicators(data=data)
        # Define action indicators (open-buy, close-buy, open-sell, close-sell)
        df = defineActionIndicators(df=df)
        # Calculate yields for every signal actions
        df = calculateYieldSignalAction(df=df)
        # Convert data frame to excel
        convertDfToExcel(df=df, metaData=meta_data)
        # Draw indicator fields (white-indicator, green-indicator, grey-indicator, rose-indicator) + (open-buy, close-buy, open-sell, close-sell)
        drawSignalActionsChart(df=df, metaData=meta_data)
    except Exception as ex:
        logging.error(ex)
        sys.exit(1)
