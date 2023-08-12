import unittest
from unittest.mock import patch, Mock
from Flask_api.map import MapRequests


class TestMapRequests(unittest.TestCase):

    @patch('Flask_api.map.googlemaps.Client')  # We mock the Client class
    def test_get_position_valid_response(self, MockClient):
        # Creating a mock response, similar to what Google Maps API might return
        mock_response = [{
            "formatted_address": "Place d'Armes, 78000 Versailles, France",
            "geometry": {
                "location": {
                    "lat": 48.8048649,
                    "lng": 2.1203554
                }
            }
        }]

        # Setting the mock to return the mock response when the geocode method is called
        mock_instance = MockClient.return_value
        mock_instance.geocode.return_value = mock_response

        # Executing the method to test
        map_request = MapRequests("le chateau versailles")
        result = map_request.get_position()

        # Verifying that the method processes the mock response correctly
        expected_result = {
            "address": "Place d'Armes, 78000 Versailles, France",
            "latitude": 48.8048649,
            "longitude": 2.1203554
        }
        self.assertEqual(result, expected_result)

    @patch('Flask_api.map.googlemaps.Client')
    def test_get_position_no_result(self, MockClient):
        # Setting the mock to return an empty list (which would simulate a response with no results)
        mock_instance = MockClient.return_value
        mock_instance.geocode.return_value = []

        # Executing the method to test
        map_request = MapRequests("nonexistent address")
        result = map_request.get_position()

        # Verifying that the method returns "no result" if the response is empty
        self.assertEqual(result, "no result")


if __name__ == "__main__":
    unittest.main()
