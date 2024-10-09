#!/usr/bin/env python3

import re
import logging
from typing import List

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self,fields):
        super(RedactingFormatter, self).__init__(self.FORMAT,fields)
        logging.basicConfig(format=self.FORMAT,level=logging.DEBUG)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        formatText = filter_datum(self.fields,self.REDACTION,record.getMessage(),self.SEPARATOR)
        logger = logging.getLogger("MyLogger")
        return logger.info(formatText)


def get_logger():
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)  
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=["password", "ssn", "email"])
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    for field in fields:
        message = re.sub(field + "=.*?" + separator,field + "=" + redaction + separator, message)
    return message