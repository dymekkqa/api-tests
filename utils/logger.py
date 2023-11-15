import allure
import datetime
import logging
import os


class Logger:
    file_name = f"logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    @classmethod
    def add_step(cls, message: str):
        allure.attach(message, name="Step")
        cls.write_log_to_file(message)
        cls.logger.info(message)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        message = f"\n-----\nTest: {test_name}\nTime: {str(datetime.datetime.now())}\nRequest method: {method}\nRequest URL: {url}\n\n"
        cls.add_step(message)

    @classmethod
    def add_request_with_json(cls, url: str, method: str, json: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        message = f"\n-----\nTest: {test_name}\nTime: {str(datetime.datetime.now())}\nRequest method: {method}\nRequest URL: {url}\nRequest body: {json}\n\n "
        cls.add_step(message)

    @classmethod
    def add_response(cls, response):
        cookie_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)
        message = f"Response code: {response.status_code}\nText response: {response.text}\nResponse headers: {headers_as_dict}\nResponse cookies: {cookie_as_dict}\n\n-----\n"
        cls.add_step(message)

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)
