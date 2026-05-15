class NotFoundError(Exception):
    def __init__(self, message="Not Found"):
        self.message = message


class ConflictError(Exception):
    def __init__(self, message="Conflict"):
        self.message = message


class PermissionDenied(Exception):
    def __init__(self, message="Permission Denied"):
        self.message = message

