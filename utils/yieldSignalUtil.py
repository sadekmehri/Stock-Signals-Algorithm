# -*- coding: utf-8 -*-
import logging
import sys
from typing import Optional, List
from pandas import DataFrame
from constants.AlphaVantage import AlphaVantageDataFields
from constants.SignalActions import SignalActions
from constants.Stocks import StockActions, StockIndicators
from constants.YieldActions import YieldActions
from utils.defineSignalsUtil import filterSignalsAction


# Define signal actions
def calculateYieldSignalAction(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        # Get coherent signal actions
        buySignal, sellSignal = filterSignalsAction(df=df)

        df = yieldPreconfigure(df=df)
        df = calculateBuyActionYield(df=df, buySignals=buySignal)
        df = calculateSellActionYield(df=df, sellSignals=sellSignal)

        return df
    except Exception as ex:
        logging.error(f"Unable to calculate yield for signal actions: {ex}!")
        sys.exit(1)


# Buy (Prix d'achat / Prix de clôture) -1.
# Calculate yield for buy action
def calculateBuyActionYield(df: Optional[DataFrame], buySignals: List[List[list]]) -> Optional[DataFrame]:
    try:
        for buySignal in buySignals:
            openBuyValues, closeBuyValue = buySignal

            totalYield = 0.0
            for openBuyValue in openBuyValues:
                firstOpenBuy, lastOpenBuy = openBuyValue

                for buyIndex in range(firstOpenBuy, lastOpenBuy + 1):
                    df.loc[buyIndex, [SignalActions.BUY.value]] = StockActions.OPEN_BUY.value
                    totalYield = totalYield + (df.at[buyIndex, StockIndicators.WHITE_INDICATOR.value] / df.at[closeBuyValue, StockIndicators.WHITE_INDICATOR.value] - 1)

            df.loc[closeBuyValue, [SignalActions.BUY.value]] = StockActions.CLOSE_BUY.value
            df.loc[closeBuyValue, [YieldActions.BUY.value]] = totalYield

        return df
    except Exception as ex:
        logging.error(f"Unable to calculate yield for buy action: {ex}!")
        sys.exit(1)


# Sell -((Prix de vente / Prix de clôture) -1).
# Calculate yield for sell action
def calculateSellActionYield(df: Optional[DataFrame], sellSignals: List[List[list]]) -> Optional[DataFrame]:
    try:
        for sellSignal in sellSignals:
            openSellValues, closeSellValue = sellSignal

            totalYield = 0.0
            for openSellValue in openSellValues:
                firstOpenSell, lastOpenSell = openSellValue

                for buyIndex in range(firstOpenSell, lastOpenSell + 1):
                    df.loc[buyIndex, [SignalActions.SELL.value]] = StockActions.OPEN_SELL.value
                    totalYield = totalYield + (-(df.at[buyIndex, StockIndicators.WHITE_INDICATOR.value] / df.at[closeSellValue, StockIndicators.WHITE_INDICATOR.value] - 1))

            df.loc[closeSellValue, [SignalActions.SELL.value]] = StockActions.CLOSE_SELL.value
            df.loc[closeSellValue, [YieldActions.SELL.value]] = totalYield

        return df
    except Exception as ex:
        logging.error(f"Unable to calculate yield for sell action: {ex}!")
        sys.exit(1)


def yieldPreconfigure(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        # Drop Stock Indicators
        # df.drop(columns=[el.value for el in StockActions], inplace=True)

        # Add yield fields
        df.insert(loc=0, column=AlphaVantageDataFields.DATE.value, value=df.index)
        df.insert(loc=len(df.columns), column='Index', value=range(0, len(df)))
        df.insert(loc=len(df.columns), column=SignalActions.SELL.value, value='')
        df.insert(loc=len(df.columns), column=YieldActions.SELL.value, value='')
        df.insert(loc=len(df.columns), column=SignalActions.BUY.value, value='')
        df.insert(loc=len(df.columns), column=YieldActions.BUY.value, value='')

        # Set numeric index column as main index for dataframe
        df.set_index('Index', inplace=True)

        return df
    except Exception as ex:
        logging.error(f"Unable to pre-configure yield action calculation: {ex} !")
        sys.exit(1)
