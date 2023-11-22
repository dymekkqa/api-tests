import pytest
from util.my_api import GoogleMapsApi


@pytest.fixture
def new_location():
    """Fixture to create a new location and return its place_id."""
    result_post = GoogleMapsApi.create_new_place()
    result_post_body = result_post.json()
    place_id = result_post_body.get("place_id")
    return place_id
