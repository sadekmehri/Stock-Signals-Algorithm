# -*- coding: utf-8 -*-
import logging
import sys
from typing import Optional, List
from typing import Union
from pandas import DataFrame
from console.readFromConsole import readExcelFields
from constants.AlphaVantage import AlphaVantageMetaDataFields
from constants.DirectoryName import DirectoryName
from constants.FileExtensions import FileExtensions
from utils.pathUtil import saveFileInDirectory


# Convert data frame to excel
def convertDfToExcel(df: Optional[DataFrame], metaData: str) -> None:
    try:
        # Read excel fields from console
        excelFields: List[str] = readExcelFields(df=df)

        logging.info('Converting data to excel in progress. Please wait ...')
        symbol = metaData.get(AlphaVantageMetaDataFields.SYMBOL.value)

        # Create directory if it doesn't exist
        filePath = saveFileInDirectory(fileDirectory=DirectoryName.EXCELS.value,
                                       fileExtension=FileExtensions.EXCEL.value,
                                       metaData=metaData)

        df = df[excelFields]
        df.to_excel(filePath, sheet_name=symbol)
        logging.info('Success ...')
    except Exception as ex:
        logging.error(f"Unable to convert data to excel: {ex}!")
        sys.exit(1)


# Convert dataframe columns to dictionary
def convertDfColumnsToDict(df: Optional[DataFrame]) -> List[Union[dict, int]]:
    length = len(df.columns)

    if length == 0:
        raise Exception('Empty list provided as param!')

    dictResult = {key + 1: val for key, val in enumerate(df.columns)}
    return [dictResult, length]
