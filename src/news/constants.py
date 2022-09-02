import os

SUPPORTED_STOCKS = os.environ.get('SUPPORTED_STOCKS').split(",")


class ErrorMessage:
    INVALID_STOCK = f'Stock is not supported. List of supported stocks: {SUPPORTED_STOCKS}'
    INVALID_PAGINATION = "Pagination parameters are invalid"
