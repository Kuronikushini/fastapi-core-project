from fastapi.responses import JSONResponse
from fastapi.requests import Request

from core_project.exceptions import BaseCoreException, OutputValidationError, OutputUnknownError

from pydantic import BaseModel, ValidationError


class ErrorContent(BaseModel):
    service_name: str
    message: str | list | dict
    error_number: str

    @classmethod
    def from_exception(
            cls,
            exception: BaseCoreException,
    ):
        assert issubclass(type(exception), BaseCoreException)
        return cls(
            service_name=exception.service_name,
            message=exception.message,
            error_code=exception.error_number,
        )


class ErrorJSONResponse(JSONResponse):
    def __init__(
            self,
            exception: BaseCoreException,
            status_code: int
    ) -> None:
        assert issubclass(type(exception), BaseCoreException)
        content = ErrorContent.from_exception(exception).dict()
        super().__init__(content, status_code)


def validation_error_json_content_factory(
        core_exception_class: type[OutputValidationError],
        status_code: int = 400,
):
    def exception_handler(validation_error: ValidationError):
        exception = core_exception_class(validation_error)
        return ErrorJSONResponse(exception, status_code)

    return exception_handler


def unknown_error_json_content_factory(
        core_exception_class: type[OutputUnknownError],
        status_code: int = 500,
):
    def exception_handler(exception: Exception):
        output_exception = core_exception_class(exception)
        return ErrorJSONResponse(output_exception, status_code)

    return exception_handler


def base_core_error_json_content_handler(
    request: Request,
    exc
):
    return ErrorJSONResponse(exc, status_code=500)
