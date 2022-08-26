# -*- coding: utf-8 -*-
import logging
import sys
from typing import Optional
import numpy as np
from pandas import DataFrame
from constants.Stocks import StockIndicators, StockActions


# Define a bunch of action indicators (open-buy, close-buy, open-sell, close-sell)
def defineActionIndicators(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        # Define open-sell indicator
        df = defineOpenSellActionIndicator(df=df)

        # Define close-sell indicator
        df = defineCloseSellActionIndicator(df=df)

        # Define close-buy indicator
        df = defineOpenBuyActionIndicator(df=df)

        # Define close-buy indicator
        df = defineCloseBuyActionIndicator(df=df)

        # Fill first nth rows of indicators with 0. It depends on the value of moving average
        df.loc[df[StockIndicators.STANDARD_DEVIATION_INDICATOR.value].isna(), [el.value for el in StockActions]] = 0

        return df
    except Exception as ex:
        logging.error(f"Unable to define action indicators: {ex}!")
        sys.exit(1)


# Determine open sell action
def defineOpenSellActionIndicator(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        df[StockActions.OPEN_SELL.value] = np.where(
            df[StockIndicators.WHITE_INDICATOR.value] > df[StockIndicators.ROSE_INDICATOR.value], 1, -1)

        return df
    except Exception as ex:
        logging.error(f"Unable to define open sell action indicators: {ex}!")
        sys.exit(1)


# Determine close sell action
def defineCloseSellActionIndicator(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        df[StockActions.CLOSE_SELL.value] = np.where(
            df[StockIndicators.WHITE_INDICATOR.value] <= df[StockIndicators.GREY_INDICATOR.value], 1, -1)

        return df
    except Exception as ex:
        logging.error(f"Unable to define close sell action indicators: {ex}!")
        sys.exit(1)


# Determine open buy action
def defineOpenBuyActionIndicator(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        df[StockActions.OPEN_BUY.value] = np.where(
            df[StockIndicators.WHITE_INDICATOR.value] < df[StockIndicators.GREEN_INDICATOR.value], 1, -1)

        return df
    except Exception as ex:
        logging.error(f"Unable to define open buy action indicators: {ex}!")
        sys.exit(1)


# Determine close buy action
def defineCloseBuyActionIndicator(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        df[StockActions.CLOSE_BUY.value] = np.where(
            df[StockIndicators.WHITE_INDICATOR.value] >= df[StockIndicators.GREY_INDICATOR.value], 1, -1)

        return df
    except Exception as ex:
        logging.error(f"Unable to define close buy action indicators: {ex}!")
        sys.exit(1)
