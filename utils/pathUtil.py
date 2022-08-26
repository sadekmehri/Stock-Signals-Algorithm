# -*- coding: utf-8 -*-
import os
from os import path
from constants.AlphaVantage import AlphaVantageMetaDataFields
from constants.DirectoryName import DirectoryName
from utils.dateUtil import getCurrentDateTime


# Create directory
def createDirectory(directoryName: str) -> str:
    projectPath = os.path.dirname(os.path.dirname(__file__))
    directory = path.join(projectPath, f'{projectPath}/{directoryName}')
    if not path.isdir(directory):
        os.makedirs(directory, exist_ok=True)

    return directory


# Create directory if it doesn't exist
def saveFileInDirectory(fileDirectory: str, fileExtension: str, metaData: str) -> str:
    currDate, currTime = getCurrentDateTime()
    directoryName = f'{DirectoryName.ASSETS.value}/{fileDirectory}/{currDate}'

    directoryPath = createDirectory(directoryName)

    stockSymbol = metaData.get(AlphaVantageMetaDataFields.SYMBOL.value)
    fileName = f'{stockSymbol}_{currTime}.{fileExtension}'
    filePath = f'{directoryPath}/{fileName}'

    return filePath
