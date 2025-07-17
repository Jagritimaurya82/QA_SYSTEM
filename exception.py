import sys

# Define a custom exception class that extends the built-in Exception class
class customexception(Exception):

    def __init__(self, error_message, error_details: sys):
        """
        Constructor to initialize the custom exception with error message and details.

        Parameters:
        - error_message: The actual error/exception message.
        - error_details: The sys module used to get exception info.
        """
        self.error_message = error_message

        # Extract traceback information from the exception
        _, _, exc_tb = error_details.exc_info()  # exc_tb: traceback object

        # Print the traceback object (for debug purposes)
        print(exc_tb)

        # Get the line number where the exception occurred
        self.lineno = exc_tb.tb_lineno

        # Get the filename in which the exception occurred
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        """
        Return a formatted error message when the exception is printed.
        """
        return "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )

# This block demonstrates how to raise the custom exception
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        # Instead of printing the error directly, raise the custom exception with additional info
        raise customexception(e, sys)
