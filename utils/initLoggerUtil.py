# -*- coding: utf-8 -*-
import logging


def initLogger():
    level = logging.INFO
    format = '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
    logging.basicConfig(level=level, format=format)
