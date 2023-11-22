from cerberus import Validator
import allure

"""Check response methods"""


class Checking:

    @staticmethod
    def check_status_code(response, status_code):
        """Check response's status code method"""
        with allure.step(f"Check response's status code {status_code}"):
            assert status_code == response.status_code

    @staticmethod
    def check_json_keys_value(response, key_name, expected_value):
        """Check response key's values method"""
        with allure.step(f"Check response key's values {key_name}: {expected_value}"):
            check = response.json()
            check_info = check.get(key_name)
            assert check_info == expected_value

    @staticmethod
    def validation_field(response, schema):
        """Verify schema's response"""
        data = response.json()
        validator = Validator(schema)
        assert validator.validate(data) is True
        if validator.validate(data) is False:
            errors = validator.errors
            return False, errors
