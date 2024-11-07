#!/usr/bin/env python3
"""
Module for filtered_logger
"""

from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """to filter values in incoming log records"""
        msg = super(RedactingFormatter, self).format(record)
        log = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return log


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ obsfucating a field """
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message
