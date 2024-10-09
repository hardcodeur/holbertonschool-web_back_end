#!/usr/bin/env python3
""" Write a function called filter_datum
that returns the log message obfuscated """
import logging
import mysql.connector
import os
import re
from typing import List


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
        """ Implement the function filter_datum """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Return log message obfuscated """
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message


def get_logger() -> logging.Logger:
    """ Create a logger """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns a connector to the database """
    connection = mysql.connector.connection.MySQLConnection(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return connection


def main():
    """ Main """
    db = get_db()
    logger = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        message = "name={}; email={}, phone={}, ssn={}; password={}; \
ip={}; last_login={}, user_agent={}; ".format(row[0], row[1], row[2], row[3],
                                              row[4], row[5], row[6], row[7])
        message = filter_datum(PII_FIELDS, '***', message, '; ')
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == '__main__':
    """ Execute main """
    main()