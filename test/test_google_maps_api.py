import allure

from util.checking import Checking
from util.my_api import GoogleMapsApi
from util.schemas import Schemas


@allure.epic("End-to-end test: Creating, Updating and Deleting new location")
class TestCreatePlace:

    @allure.title("Create new location by POST request")
    @allure.description("Creating new location")
    def test_create_new_location(self, new_location):
        """Create new location by POST request"""

        result_get = GoogleMapsApi.get_new_place(new_location)
        Checking.check_status_code(result_get, 200)
        Checking.validation_field(result_get, Schemas.schema_get_location)
        Checking.check_json_keys_value(result_get, 'address', '29, side layout, cohen 09')

    @allure.title("Updating new location by PUT request")
    @allure.description("Updating new location")
    def test_update_new_location(self, new_location):
        """Update new location address by PUT request"""

        result_put = GoogleMapsApi.update_for_address_new_place(new_location)
        Checking.check_status_code(result_put, 200)
        Checking.validation_field(result_put, Schemas.schema_msg)
        Checking.check_json_keys_value(result_put, 'msg', 'Address successfully updated')

        """Verify updating new location's address by GET request"""

        result_get = GoogleMapsApi.get_new_place(new_location)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_keys_value(result_get, 'address', '100 Mickiewicz street, PL')
        Checking.validation_field(result_get, Schemas.schema_get_location)

    @allure.title("Deleting new location by DELETE request")
    @allure.description("Deleting new location")
    def test_delete_new_location(self, new_location):
        """Delete new location by DELETE request"""

        result_del = GoogleMapsApi.delete_new_place(new_location)
        Checking.check_status_code(result_del, 200)
        Checking.check_json_keys_value(result_del, 'status', 'OK')
        Checking.validation_field(result_del, Schemas.schema_delete)

        """Verify location deleted by GET request"""

        result_get = GoogleMapsApi.get_new_place(new_location)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_keys_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        Checking.validation_field(result_get, Schemas.schema_msg)
