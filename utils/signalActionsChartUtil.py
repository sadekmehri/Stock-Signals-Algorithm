# -*- coding: utf-8 -*-
import logging
import re
import sys
from typing import List, Optional
import matplotlib.pyplot as plt
from pandas import DataFrame
from constants.AlphaVantage import AlphaVantageDataFields
from constants.Colors import COLORS
from constants.DirectoryName import DirectoryName
from constants.FileExtensions import FileExtensions
from constants.SignalActions import SignalActions
from constants.Stocks import StockIndicators, StockActions
from constants.actionColors import ActionColors
from utils.pathUtil import saveFileInDirectory


# Displaying signal actions chart
def drawSignalActionsChart(df: Optional[DataFrame], metaData: str) -> None:
    try:
        logging.info('Drawing signal actions chart in progress. Please wait ...')
        # Get indicator Fields
        fields: List[str] = [el.value for el in StockIndicators if not el.value in (
            StockIndicators.MOVING_AVERAGE.value, StockIndicators.STANDARD_DEVIATION_INDICATOR.value)]

        # Use dark mode
        plt.style.use('dark_background')

        # Set date as index
        df.set_index(AlphaVantageDataFields.DATE.value, inplace=True)

        # Fil close value with color
        df[StockIndicators.WHITE_INDICATOR.value].plot.area(stacked=False, color=COLORS['TRANSPARENT_BLUE'], label='')

        # Check if the given column exists in dataframe else throw exception
        for field in fields:
            colorName = re.sub('_indicator', '', field).upper()
            plt.plot(df[field], label=field, color=COLORS[colorName])

        # Indicators
        sellSignalField = SignalActions.SELL.value
        buySignalField = SignalActions.BUY.value
        openBuyAction = StockActions.OPEN_BUY.value
        closeBuyAction = StockActions.CLOSE_BUY.value
        openSellAction = StockActions.OPEN_SELL.value
        closeSellAction = StockActions.CLOSE_SELL.value
        closePriceField = AlphaVantageDataFields.CLOSE.value

        # Plotting signal actions
        plt.plot(df.loc[df[buySignalField] == openBuyAction].index,
                 df[closePriceField][df[buySignalField] == openBuyAction], 'o',
                 color=ActionColors.OPEN_BUY.value, ms=5, markerfacecolor='none', label=openBuyAction)

        plt.plot(df.loc[df[buySignalField] == closeBuyAction].index,
                 df[closePriceField][df[buySignalField] == closeBuyAction], 'o',
                 color=ActionColors.CLOSE_BUY.value, ms=5, markerfacecolor='none', label=closeBuyAction)

        plt.plot(df.loc[df[sellSignalField] == openSellAction].index,
                 df[closePriceField][df[sellSignalField] == openSellAction], 'o',
                 color=ActionColors.OPEN_SELL.value, ms=5, markerfacecolor='none', label=openSellAction)

        plt.plot(df.loc[df[sellSignalField] == closeSellAction].index,
                 df[closePriceField][df[sellSignalField] == closeSellAction], 'o',
                 color=ActionColors.CLOSE_SELL.value, ms=5, markerfacecolor='none', label=closeSellAction)

        plt.title("Displaying signal actions")
        plt.rcParams['figure.figsize'] = 20, 10
        plt.grid(True, alpha=.3)
        plt.ylabel('Price')
        plt.xlabel('Date')
        fig = plt.gcf()
        plt.legend()
        plt.show()

        logging.info('Success ...')

        saveSignalActionsChart(figure=fig, metaData=metaData)
    except Exception as ex:
        logging.error(f"Unable to draw signal actions' plot: {ex}!")
        sys.exit(1)


# save signal actions plot
def saveSignalActionsChart(figure: any, metaData: str) -> None:
    try:
        logging.info("Saving signal actions' chart. Please wait ...")
        filePath = saveFileInDirectory(fileDirectory=DirectoryName.SIGNALS.value,
                                       fileExtension=FileExtensions.PNG.value, metaData=metaData)

        figure.savefig(filePath)
        logging.info('Success ...')
    except Exception as ex:
        logging.error(f"Unable to save signal actions' plot: {ex}!")
        sys.exit(1)
