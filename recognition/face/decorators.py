from functools import wraps

from face.common.constants import EnvironmentVariables
from rest_framework.exceptions import APIException


class WithRetry:
    def __init__(
            self,
            retries_limit: int = EnvironmentVariables.DEFAULT_RETRIES_LIMIT,
            allowed_exceptions=None,
    ) -> None:
        self.retries_limit = retries_limit
        self.allowed_exceptions = allowed_exceptions or (APIException,)

    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None

            for _ in range(self.retries_limit):
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exceptions as error:
                    last_raised = error
            raise last_raised

        return wrapped
