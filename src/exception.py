#  For acccessing exception traceback info
import sys
# from src.logger import logging

def error_message_detail(error, error_detail : sys) :
    """
    Constructs a detailed error message including:
        - the filename where the error occurred
        - the line number of the error
        - the error message itself
    """
    # Unpacking type, value, traceback object
    _, _, exc_tb = error_detail.exc_info()
    # Get the file name
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Construct the error message with file_name, exact lineno and error message in string
    error_message = "Error has been occured in python script name [{0}], line number [{1}], and error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception) :
    """
    A custom exception class that overrides the base Exception by
    including detailed error context (filename, line number, message).
    """
    def __init__(self, error_message, error_detail : sys) :
        # Call the base class constructor with the initial message
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
        
    def __str__(self) :
        """
        When the exception is printed or converted to string, return the custom detailed message.
        """
        return self.error_message

# Testing logger.py and exception.py
# if __name__ == "__main__" :
#     try :
#         a = 1/0
    
#     except Exception as e :
#         logging.info("Divide  by zero")
#         raise CustomException(e, sys)