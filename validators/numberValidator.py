# -*- coding: utf-8 -*-


# Check if the given string is numeric or not
def isStringNumeric(ch: str):
    if not ch.isnumeric():
        raise Exception("Please provide a numeric value")


# Check if the given number is strict positive or not
def isStrictPositiveNumber(number: float):
    if number <= 0:
        raise Exception("Please provide strict positive value")


# Check if the number between a given range
def isNumberBetweenRange(number: int, minRange: int, maxRange: int):
    if minRange >= maxRange:
        raise Exception(f"Min value {minRange} is greater then max value {maxRange}!")

    if number < minRange or number > maxRange:
        raise Exception(f"The given value {number} is not between {minRange} and {maxRange}!")
