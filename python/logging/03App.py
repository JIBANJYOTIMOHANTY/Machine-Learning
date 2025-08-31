import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")
def add(a, b):
    result =a + b
    logger.debug(f"Adding {a} and {b} to get {result}")
    return result
def substract(a, b):
    result =a - b
    logger.debug(f"Substracting {a} and {b} to get {result}")
    return result
def mult(a, b):
    result =a * b
    logger.debug(f"Multiplying {a} and {b} to get {result}")
    return result
def div(a, b):
    result =a / b
    logger.debug(f"Dividing {a} and {b} to get {result}")
    return result

add(10, 20)
substract(20, 10)
mult(10, 20)
div(20, 10)
