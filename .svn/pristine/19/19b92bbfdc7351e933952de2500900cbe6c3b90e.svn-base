class DataSourceError(Exception):

    def __init__(self, message, expression: Exception = None, error_code: str = ""):
        self.expression = expression
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return repr(self.message)
