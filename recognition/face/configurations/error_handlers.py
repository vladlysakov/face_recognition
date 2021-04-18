import os

from face.common.constants import ErrorHandlersVariables


class ErrorHandlersKeyConfig:
    HANDLER500 = os.getenv(ErrorHandlersVariables.HANDLER500, ErrorHandlersVariables.HANDLER500_VALUE)
    HANDLER400 = os.getenv(ErrorHandlersVariables.HANDLER400, ErrorHandlersVariables.HANDLER400_VALUE)
