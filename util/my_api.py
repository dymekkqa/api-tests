from util.http_methods import HttpMethods
import os
from dotenv import load_dotenv

load_dotenv()

"""Google maps api's test methods"""

base_url = os.getenv('base_url')
key = os.getenv('key')


class GoogleMapsApi:

    @staticmethod
    def create_new_place():
        """Create new location's method"""

        json_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resource = '/maps/api/place/add/json'  # address for create new place on Google maps
        post_url = f"{base_url}{post_resource}{key}"
        result_new_place = HttpMethods.post(post_url, json_create_new_place)
        return result_new_place

    @staticmethod
    def get_new_place(place_id):
        """Create new location's method"""

        get_resource = '/maps/api/place/get/json'  # address for get info about new place on Google maps
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
        result_get = HttpMethods.get(get_url)
        return result_get

    @staticmethod
    def update_for_address_new_place(place_id):
        """Update address for new location's method"""

        put_resource = '/maps/api/place/update/json'  # address for update new location's object
        json_update_new_place = {
            "place_id": f"{place_id}",
            "address": "100 Mickiewicz street, PL",  # new address for new location
            "key": "qaclick123"
        }
        put_url = f"{base_url}{put_resource}{key}"
        result_put = HttpMethods.put(put_url, json_update_new_place)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """Delete new location's method"""

        del_resource = '/maps/api/place/delete/json'  # address for update new location's object
        json_delete = {
            "place_id": f"{place_id}"
        }
        del_url = f"{base_url}{del_resource}{key}"
        result = HttpMethods.delete(del_url, json_delete)
        return result
