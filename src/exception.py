import sys
import logging

def error_message_detail(error , error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = f"\nerror occured in python scribt name: {file_name} \nline number: {exc_tb.tb_lineno} \nerror messasge is: {str(error)}"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message ,error_detail:sys ):
        super().__init__(error_message)
        self.error_message =error_message_detail(error_message , error_detail)
        
    def __str__(self):
        return self.error_message
    
    
# if __name__ == "__main__":
#     try:
#         2/0
#     except Exception as e:   
#         logging.info("Devide by zero")
#         raise CustomException(e ,sys)