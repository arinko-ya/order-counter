from enum import Enum


class Status(Enum):
    SUCCEEDED = 0
    FAILED = 1


class Result:
    def __init__(self, status: Status, message: str):
        self.status = status
        self.message = message
        self.category = ''

        self._convert_to_category(status)

    def _convert_to_category(self, status: Status):
        if status == Status.SUCCEEDED:
            self.category = 'info'

        if status == Status.FAILED:
            self.category = 'danger'
