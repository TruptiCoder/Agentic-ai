from logger import logging

def add(a, b):
    logging.debug("The addition operating is taking place")
    return a + b

logging.debug("The addition fuction is called")
add(3, 5)