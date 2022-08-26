# -*- coding: utf-8 -*-
import logging
from typing import Optional, List
from pandas import DataFrame
from console.printToConsole import printDict
from validators.nonEmptyListValidator import isListEmpty
from validators.numberValidator import isStringNumeric, isNumberBetweenRange


# Read stock symbol
def readStockSymbol() -> str:
    symbol = str(input("-> Please enter a symbol to see if it's found in alpha vantage database: ")).strip()
    return symbol


# Read excel fields
def readExcelFields(df: Optional[DataFrame]) -> List[str]:
    from converters.dfConverter import convertDfColumnsToDict

    potentialFields, length = convertDfColumnsToDict(df=df)
    printDict(menuFields=potentialFields)
    excelFields = []
    stopSymbol = 'Stop'
    allSymbol = 'All'

    while True:
        try:
            print(f"Please enter key '{stopSymbol}' to terminate reading field indexes - '{allSymbol}' key to select all fields")
            choice = str(input("-> Enter your choice: ")).strip()

            if stopSymbol.casefold() == choice.casefold():
                isListEmpty(excelFields)

                logging.info("Removing duplicate values ...")
                uniqueFields = [*set(excelFields)]
                logging.info(f"Your choice(s) is/are: {uniqueFields}")

                return uniqueFields

            if allSymbol.casefold() == choice.casefold():
                return [val for key, val in potentialFields.items()]

            isStringNumeric(choice)
            choice = int(choice)
            isNumberBetweenRange(choice, 1, length)

            excelFields.append(potentialFields[choice])

            currentValues = ' -- '.join(str(x) for x in excelFields)
            print(f'Current list values are: {currentValues}')

        except Exception as e:
            logging.error(e)
