from unittest import TestCase
from unittest.mock import patch  # import of patch decorator from unittest module

from config import API_KEY

from Flask_api.map import MapRequests


class TestMapRequests(TestCase):
    @patch('Flask_api.map.MapRequests.get_position')  # We set up the decorator that takes the object
    # to mock as argument
    def test_get_position(self, mock_get_position_from_api):
        # The decorator injects the mocker object into the
        # function as an argument to the method. The argument name is free of choice. return_value method is used to
        # associate the desired return value with the mock.
        expected_result = {
            "address": "Place d'Armes, 78000 Versailles, France",
            "latitude": 48.8048649,
            "longitude": 2.1203554
        }

        print(type(expected_result))
        mock_get_position_from_api.return_value = expected_result
        position_proposed = MapRequests(API_KEY, "le chateau versailles")
        # We use the assertEqual method of the TestCase class to compare the value returned by the method we are
        # testing with the expected result
        self.assertEqual(position_proposed.get_position(), expected_result)
