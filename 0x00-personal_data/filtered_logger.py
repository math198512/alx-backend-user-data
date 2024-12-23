#!/usr/bin/env python3
"""
Module for filtered_logger
"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """takes no arguments and returns a logging.Logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.propagate = False
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to secure database"""
    PERSONAL_DATA_DB_HOST = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    PERSONAL_DATA_DB_USERNAME = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    PERSONAL_DATA_DB_PASSWORD = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    PERSONAL_DATA_DB_NAME = os.getenv('PERSONAL_DATA_DB_NAME')
    cnx = mysql.connector.connect(
        host=PERSONAL_DATA_DB_HOST,
        port=3306,
        user=PERSONAL_DATA_DB_USERNAME,
        password=PERSONAL_DATA_DB_PASSWORD,
        database=PERSONAL_DATA_DB_NAME)
    return cnx


def main():
    """Read and filter data, the whole picture"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        print(filter_datum(PII_FIELDS, 'xxx', row, ';'))
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()