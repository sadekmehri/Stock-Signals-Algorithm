# -*- coding: utf-8 -*-
from typing import List


# Check list is empty or not
def isListEmpty(lst: List[any]) -> None:
    nbrLstItems = len(lst)

    if nbrLstItems == 0:
        raise Exception('Empty list provided as param!')
