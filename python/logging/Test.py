from LoggingPython import logging
def add(a, b):
    logging.debug("The addition take place")
    return a + b;

logging.debug("The addition function is called")
add(10, 20)
