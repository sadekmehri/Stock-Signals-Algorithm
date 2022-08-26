# -*- coding: utf-8 -*-
import logging
import sys
from typing import Optional, List
from pandas import DataFrame, Series
from constants.Stocks import StockIndicators, StockActions


# Filter signal actions
def filterSignalsAction(df: Optional[DataFrame]):
    try:
        # Calculating firstIndex and lastIndex of valid buy operation
        buySignal = filterOpenCloseBuySignal(df=df)

        # Calculating firstIndex and lastIndex of valid sell operation
        sellSignal = filterOpenCloseSellSignal(df=df)

        return buySignal, sellSignal
    except Exception as ex:
        logging.error(f"Unable to filter signal actions: {ex}!")
        sys.exit(1)


# Filter open close sell signal
def filterOpenCloseSellSignal(df: Optional[DataFrame]) -> List[List[list]]:
    try:
        openSellSignalAction = getFirstLastOccStockAction(actionList=df[StockActions.OPEN_SELL.value])
        closeSellSignalAction = getFirstLastOccStockAction(actionList=df[StockActions.CLOSE_SELL.value])

        sellSignal = defineSignal(actions=[openSellSignalAction, closeSellSignalAction])

        return sellSignal
    except Exception as ex:
        logging.error(f"Unable to filter open close signal: {ex}!")
        sys.exit(1)


# Filter open close buy signal
def filterOpenCloseBuySignal(df: Optional[DataFrame]) -> List[List[list]]:
    try:
        openBuySignalAction = getFirstLastOccStockAction(actionList=df[StockActions.OPEN_BUY.value])
        closeBuySignalAction = getFirstLastOccStockAction(actionList=df[StockActions.CLOSE_BUY.value])

        buySignal = defineSignal(actions=[openBuySignalAction, closeBuySignalAction])

        return buySignal
    except Exception as ex:
        logging.error(f"Unable to filter open close signal: {ex}!")
        sys.exit(1)


# Define signal actions
def defineSignal(actions):
    try:
        i, j = 0, 0
        signalList = []
        openAction, closeAction = actions
        firstLastOpenAction, firstLastOpenActionLstLength = openAction
        firstLastCloseAction, firstLastCloseActionLstLength = closeAction

        while i < firstLastOpenActionLstLength and j < firstLastCloseActionLstLength:
            while j < firstLastCloseActionLstLength and firstLastOpenAction[i][1] > firstLastCloseAction[j][0]:
                j = j + 1

            actionList = []
            while j < firstLastCloseActionLstLength and i < firstLastOpenActionLstLength and firstLastCloseAction[j][0] > firstLastOpenAction[i][1]:
                actionList.append(firstLastOpenAction[i])
                i = i + 1

                # Last row
                if i >= firstLastOpenActionLstLength:
                    if firstLastCloseAction[j][0] > firstLastOpenAction[i - 1][1]:
                        signalList.append([actionList, firstLastCloseAction[j][0]])

                    return signalList

                # When last open value is greater than first close value
                if firstLastOpenAction[i][1] > firstLastCloseAction[j][0]:
                    signalList.append([actionList, firstLastCloseAction[j][0]])

        return signalList
    except Exception as ex:
        logging.error(f"Unable to define signal actions: {ex}!")
        sys.exit(1)


# Determine the first and last position of a given action (first open-buy, last open-buy, etc)
def getFirstLastOccStockAction(actionList: Series):
    try:
        firstLastList = []
        firstLastListLength = 0
        listLength = len(actionList)
        startIndex = StockIndicators.MOVING_AVERAGE.value - 1
        i, j = startIndex, startIndex

        while i < listLength and j < listLength:
            while i < listLength and actionList[i] != 1:
                i = i + 1

            j = i
            while j < listLength and actionList[j] == 1:
                j = j + 1

            # Last index
            if j >= listLength:
                if actionList[j - 1] == 1:
                    firstLastListLength = firstLastListLength + 1
                    firstLastList.append([i, listLength - 1])

                return firstLastList, firstLastListLength

            firstLastListLength = firstLastListLength + 1
            firstLastList.append([i, j - 1])
            i = j

        return firstLastList, firstLastListLength
    except Exception as ex:
        logging.error(f"Unable to calculate first last action indicators: {ex}!")
        sys.exit(1)
