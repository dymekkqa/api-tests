import requests
import allure
from app.logger import Logger

""" HTTP method's list """


class HttpMethods:
    headers = {'content-type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("Send GET request"):
            Logger.add_request(url, method="GET")
            response = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(response)
            return response

    @staticmethod
    def post(url, body):
        with allure.step("Send POST request"):
            Logger.add_request_with_json(url, method="POST", json=body)
            response = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(response)
            return response

    @staticmethod
    def put(url, body):
        with allure.step("Send PUT request"):
            Logger.add_request_with_json(url, method="PUT", json=body)
            response = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(response)
            return response

    @staticmethod
    def delete(url, body):
        with allure.step("Send DELETE request"):
            Logger.add_request_with_json(url, method="DELETE", json=body)
            response = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(response)
            return response
