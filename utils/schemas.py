class Schemas:
    schema_msg = {'msg': {"type": "string"}}
    schema_create = {
            "status": {"type": "string"},
            "place_id": {"type": "string"},
            "scope": {"type": "string"},
            "reference": {"type": "string"},
            "id": {"type": "string"}
            }
    schema_get_location = {
            "location": {
                "type": "dict",
                "schema": {
                    "latitude": {"type": "string"},
                    "longitude": {"type": "string"}
                },

            },
            "accuracy": {"type": "string"},
            "name": {"type": "string"},
            "phone_number": {"type": "string"},
            "address": {"type": "string"},
            "types": {"type": "string"},
            "website": {"type": "string"},
            "language": {"type": "string"}
        }
    schema_delete = {"status": {"type": "string"}}


