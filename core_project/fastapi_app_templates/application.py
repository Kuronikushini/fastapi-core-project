from fastapi import FastAPI
from fastapi.applications import AppType
from pydantic import ValidationError

from core_project.exceptions import BaseCoreException, OutputValidationError, OutputUnknownError
from .error_content import validation_error_json_content_factory, base_core_error_json_content_handler, \
    unknown_error_json_content_factory

from .responses import response_code_dict


class ModifiedFastAPI(FastAPI):
    def __init__(
            self: AppType,
            validation_error_class: type[OutputValidationError],
            unknown_error_class: type[OutputUnknownError],
            *args,
            **kwargs
    ):
        if 'responses' not in kwargs:
            kwargs['responses'] = response_code_dict
        super().__init__(*args, **kwargs)

        self.add_exception_handler(
            ValidationError,
            validation_error_json_content_factory(validation_error_class)
        )
        self.add_exception_handler(
            BaseCoreException,
            base_core_error_json_content_handler
        )
        self.add_exception_handler(
            Exception,
            unknown_error_json_content_factory(unknown_error_class)
        )
