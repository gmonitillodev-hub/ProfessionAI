import logging
from logging.handlers import RotatingFileHandler


def setup_logger(logger_name, log_file):

    COLORS = {

    }

    app_logger = logging.getLogger(logger_name)
    app_logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(
        log_file,
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    rotating_handler = RotatingFileHandler(
        f"rotating_{logger_name}",
        maxBytes=5000,
    )
    rotating_handler.setLevel(logging.INFO)
    rotating_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    app_logger.addHandler(file_handler)
    app_logger.addHandler(console_handler)
    app_logger.addHandler(rotating_handler)

    return app_logger


class EcommerceApp:
    def __init__(self, app_name):
        self.logger = logging.getLogger(app_name)
        self.logger.info("App initialized")

    def login_user(self, username):
        self.logger.info(f"Logging user {username}")
        pass

    def add_to_cart(self, username, product, quantity):
        self.logger.info(f"Adding {product} to cart with {quantity} - {username}")
        pass

    def checkout(self, username, total_amount):
        self.logger.info(f"Checking out {username} for {total_amount}")
        pass

    def process_payment(self, amount):
        self.logger.info(f"Processing payment for {amount}")
        pass


if __name__ == "__main__":
    logger = setup_logger("myEcommerce", "log.txt")

    logger.debug("Logger initialized")

    ecommerce_app = EcommerceApp("myEcommerce")
    ecommerce_app.login_user("Nicola")

    for i in range(1, 5000):
        ecommerce_app.add_to_cart("Nicola", "Milk", 10)

    ecommerce_app.add_to_cart("Nicola", "Milk", 20)
    ecommerce_app.add_to_cart("Nicola", "Milk", 30)
    ecommerce_app.checkout(username="Nicola", total_amount=100)
    ecommerce_app.process_payment(amount=100)
