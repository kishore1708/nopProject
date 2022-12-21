import inspect
import logging

# @staticmethod
# def loggen():
#     logging.basicConfig(filename="../logs/automation.log",
#                         format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%y %I:%M:%S %p')
#     logger=logging.getLogger()
#     logger.setLevel(logging.INFO)
#     return logger


def loggen():
    loggername=inspect.stack()[1][3]
    logger=logging.getLogger(loggername)
    filhandler=logging.FileHandler(filename="../logs/automation.log")
    formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s',datefmt='%m/%d/%y %I:%M:%S %p')
    filhandler.setFormatter(formatter)
    logger.addHandler(filhandler)
    logger.setLevel(logging.INFO)
    return logger