

class BaseCoreException(Exception):
    """
    This base exception is designed to register all types of anticipated errors
    To use please, specify:
    _service_error_code - number of service
    _architecture_level_code - level of error (api - 1, interface - 2, use case - 3, entities - 4)
    _package_code - package code (for example, inside interfaces level - s3_repo - 1, postgres_repo - 2 etc)
    _error_code - number of error inside package (for example, connection_error - 1, permission_denied - 2 etc)

    Inside exception defined error_number property
    It returns full error number like "1.4.15.27"
    """

    _service_error_code: int = -1  # It means you not specified your exception code
    _architecture_level_code: int = -1  # It means you not specified your exception code
    _package_code: int = -1  # It means you not specified your exception code
    _error_code: int = -1  # It means you not specified your exception code

    service_name: str = 'Base core project'

    message: str | list | dict = 'Base core exception message'

    def __init__(self, *args, **kwargs):
        if self._service_error_code == -1:
            raise NotImplementedError('Please specify service error code')
        elif self._architecture_level_code == -1:
            raise NotImplementedError('Please specify architecture level code')
        elif self._package_code == -1:
            raise NotImplementedError('Please specify package code')
        elif self._error_code == -1:
            raise NotImplementedError('Please specify error code')
        elif self.service_name == 'Base core project':
            raise NotImplementedError('Please specify service name of message')
        elif self.message == 'Base core exception message':
            raise NotImplementedError('Please specify error code')

    @property
    def error_number(self) -> str:
        """
        It returns full error number like "1.4.15.27"
        """
        return f"{self._service_error_code}.{self._architecture_level_code}.{self._package_code}.{self._error_code}"
