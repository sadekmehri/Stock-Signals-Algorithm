# -*- coding: utf-8 -*-
from typing import Dict, List


# Display dictionary to console
def printDict(menuFields: Dict[int, str]) -> None:
    print('-> Displaying available fields ...')
    for key, val in menuFields.items():
        print(key, '--', val)


# Display list to console
def printList(lst: List, message: str = "") -> None:
    print(message)
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(lst)))
