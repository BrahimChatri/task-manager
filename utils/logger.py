"""Module for logging handling"""
import logging

logging_format = logging.Formatter("[%(asctime)s | %(name)s] %(message)s")
second_format = logging.Formatter("%(message)s")
Log_handler = logging.FileHandler("logs.log")
Stream_handler = logging.StreamHandler()
Stream_handler.setFormatter(second_format)
Log_handler.setFormatter(logging_format)
Info_logger = logging.getLogger("INFO")
Info_logger.setLevel(20)
Info_logger.addHandler(Log_handler)
Info_logger.addHandler(Stream_handler)
Error_logger = logging.getLogger("ERROR")
Error_logger.setLevel(40)
Error_logger.addHandler(Log_handler)
Error_logger.addHandler(Stream_handler)