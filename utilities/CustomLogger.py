import inspect
import logging


class LogGeneration:

    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("C:\\Users\\HP\\PycharmProjects\\nopCommerce application\\Logs\\automation.log")
        logger.addHandler(fileHandler)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger

        # logging.basicConfig(filename="C:\\Users\\HP\\PycharmProjects\\nopCommerce application\\Logs\\automation.log",
        #                 format='%(asctime)s: %(levelname)s: %(message)s',
        #                 datefmt='%m/%d/%y %I:%M:%S $P')
        # logger= logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logger