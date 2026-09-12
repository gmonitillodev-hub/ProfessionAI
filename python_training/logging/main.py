import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


def setup_logging():
    logger = logging.getLogger("myLogger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formator = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formator)
    console_handler.setFormatter(formator)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    live_logger = setup_logging()

    live_logger.debug("Test log di debug - visibile solo file")
    live_logger.info("Test log di info - visibile ovunque")
    live_logger.warning("Test log di warning - visibile solo file")
    live_logger.error("Test log di error - visibile solo file")
    live_logger.critical("Test log di critical - visibile solo file")


def setup_rotating_log():
    logger = logging.getLogger("myRotatingLogger")
    logger.setLevel(logging.DEBUG)

    rotating_handler = RotatingFileHandler('app_rotating.log', maxBytes=500_000, backupCount=10)

    formato = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    rotating_handler.setFormatter(formato)
    logger.addHandler(rotating_handler)

    time_handler = TimedRotatingFileHandler(
        filename='app_rotating_time.log',
        when='h',
        interval=1,
    )

    time_handler.setFormatter(formato)
    logger.addHandler(time_handler)

    return logger


if __name__ == '__main__':
    logger = setup_rotating_log()

    logger.debug("Test log di debug - visibile solo file")
    for i in range(1, 25000):
        logger.info(str(i) + "Messaggio niumero")
        logger.debug("Test log di info - visibile solo file")
        logger.error("Test log di error - visibile solo file")
