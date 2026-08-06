class ApiException(Exception):
    """
    Exceção lançada quando ocorre um erro durante a comunicação
    com uma API externa.
    """

    def __init__(self, message: str):
        super().__init__(message)