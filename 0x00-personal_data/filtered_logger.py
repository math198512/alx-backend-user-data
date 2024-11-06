#!/usr/bin/env python3
"""
Module for filtered_logger
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> List[str]:
    """ obsfucating a field """
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message
