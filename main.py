from pred.exception import PredException
import os 
import sys
from pred.logger import logging 

def test_exception():
    try:
        logging.info("Error occured which is division by zero")
        a=1/0
    except Exception as e:
        raise PredException(e,sys)

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)