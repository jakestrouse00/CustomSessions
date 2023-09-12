class RetriesExceeded(Exception):
    def __init__(self, message, retries_attempted: int):
        super().__init__(message)
        self.retries_attempted = retries_attempted
