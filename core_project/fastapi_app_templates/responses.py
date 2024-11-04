
from .error_content import ErrorContent

response_code_list = [400, 500]

response_code_dict = {
    code: {
        "model": ErrorContent
    }
    for code in response_code_list
}
