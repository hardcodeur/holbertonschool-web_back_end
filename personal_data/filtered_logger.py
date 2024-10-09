#!/usr/bin/env python3

import re
import logging
from typing import List

class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class for logging sensitive information.
    
    This formatter redacts sensitive fields such as 'password', 'ssn', and 'email' from log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        logging.basicConfig(format=self.FORMAT, level=logging.DEBUG)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Redact sensitive information from the log message."""
        formatted_text = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return formatted_text


def get_logger() -> logging.Logger:
    """Creates and configures a logger that redacts sensitive information."""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=["password", "ssn", "email"])
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Redact sensitive fields in a log message.

    Args:
        fields (List[str]): List of fields to redact.
        redaction (str): The string to replace sensitive information.
        message (str): The log message containing sensitive data.
        separator (str): The field separator.

    Returns:
        str: The redacted message.
    """
    pattern = '|'.join([f'{field}=[^\\{separator}]*' for field in fields])
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}", message)