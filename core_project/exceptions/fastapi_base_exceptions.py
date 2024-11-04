from asyncio import Protocol

from pydantic import ValidationError

from .base_exceptions import BaseCoreException


class OutputValidationError(Protocol, BaseCoreException):
    def __init__(self, exception: ValidationError):
        errors_content = exception.errors()
        result_message = []
        for error in errors_content:
            output_error_content = {
                'variable': error['loc'][0],
                'value': error['input'],
                'message': error['msg']
            }
            result_message.append(output_error_content)

        self.message = result_message
        super().__init__()


class OutputUnknownError(Protocol, BaseCoreException):
    def __init__(self, exception: Exception):
        self.message = f'Unknown error {type(exception)} with message: {exception.args}'
        super().__init__()
