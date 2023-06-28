class LoadErrorException(Exception):
    """Exception raised when unable to load due to reaching maximum load capacity.

    Attributes:
        message (str): The error message indicating the reason for the exception.

    """
    message = "Unable to load, reach maximum load capacity."

    def __init__(self):
        """
        Initializes a LoadError instance.

        """
        super().__init__(self.message)
