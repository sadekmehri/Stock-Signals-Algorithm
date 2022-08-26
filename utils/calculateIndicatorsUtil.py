# -*- coding: utf-8 -*-
import logging
import sys
from typing import Optional
import pandas as pd
from pandas import DataFrame
from constants.AlphaVantage import AlphaVantageDataFields
from constants.Stocks import StockIndicators


# Calculate a bunch of indicators (green-indicator, white-indicator, green-indicator, grey-indicator)
def calculateIndicators(data: list) -> Optional[DataFrame]:
    try:
        df = pd.DataFrame(data) \
            .sort_values(by=[AlphaVantageDataFields.DATE.value], ascending=True)

        # Calculate gey indicator (Moving average)
        df = calculateGreyIndicator(df)

        # Calculate white indicator (Close value)
        df = calculateWhiteIndicator(df)

        # Calculate standard deviation value
        df = calculateStandardDeviation(df)

        # Calculate rose indicator (Moving average + 2 * standardDeviation)
        df = calculateRoseIndicator(df)

        # Calculate green indicator (Moving average - 2 * standardDeviation)
        df = calculateGreenIndicator(df)

        return df
    except Exception as ex:
        logging.error(f"Unable to calculate indicators: {ex}!")
        sys.exit(1)


# calculate standard deviation indicator
def calculateStandardDeviation(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        df[StockIndicators.STANDARD_DEVIATION_INDICATOR.value] = df.get(StockIndicators.WHITE_INDICATOR.value) \
            .rolling(StockIndicators.MOVING_AVERAGE.value) \
            .std()

        return df
    except Exception as ex:
        logging.error(f"Unable to calculate standard deviation indicator: {ex}!")
        sys.exit(1)


# Calculate grey indicator
def calculateGreyIndicator(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        df[StockIndicators.GREY_INDICATOR.value] = df.get(AlphaVantageDataFields.CLOSE.value) \
            .rolling(StockIndicators.MOVING_AVERAGE.value) \
            .mean()

        return df
    except Exception as ex:
        logging.error(f"Unable to calculate grey indicator: {ex}!")
        sys.exit(1)


# Calculate white indicator
def calculateWhiteIndicator(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        df[StockIndicators.WHITE_INDICATOR.value] = df[AlphaVantageDataFields.CLOSE.value]

        return df
    except Exception as ex:
        logging.error(f"Unable to calculate white indicator: {ex}!")
        sys.exit(1)


# Calculate rose indicator
def calculateRoseIndicator(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        df[StockIndicators.ROSE_INDICATOR.value] = df[StockIndicators.GREY_INDICATOR.value] \
                                                   + 2 * df[StockIndicators.STANDARD_DEVIATION_INDICATOR.value]

        return df
    except Exception as ex:
        logging.error(f"Unable to calculate rose indicator: {ex}!")
        sys.exit(1)


# Calculate rose indicator
def calculateGreenIndicator(df: Optional[DataFrame]) -> Optional[DataFrame]:
    try:
        df[StockIndicators.GREEN_INDICATOR.value] = df[StockIndicators.GREY_INDICATOR.value] \
                                                    - 2 * df[StockIndicators.STANDARD_DEVIATION_INDICATOR.value]

        return df
    except Exception as ex:
        logging.error(f"Unable to calculate green indicator: {ex}!")
        sys.exit(1)
