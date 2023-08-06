import os
from dotenv import load_dotenv

"""Gets maps from google API with user message parsed"""
from pprint import pprint  # function to facilitate reading of geocode response (json format)

import googlemaps  # Python client library for Google Maps Platform


# """Performs requests to the Google Maps Geocoding API."""
# from googlemaps import convert


class MapRequests :
    """Class to acces API Google Maps.
    return a dictionnary
    exemple
    {'address': "Place d'Armes, 78000 Versailles, France", "latitude": 48.8048649, "longitude": 2.1203554}
    """

    # API from environment variables
    def __init__(self, msg_parsed):
        self.api_key = os.environ.get('API_KEY_BACK')
        self.msg_parsed = msg_parsed

    def get_position(self):
        """Return the geographical coordinates of the parsed user input and the formatted address"""
        # map_client is an instance of Class Client which is in the library.module googlemaps.client
        map_client=googlemaps.Client(key=self.api_key)
        # Geocoding is the process of converting addresses into geographic coordinates (like latitude and longitude )
        # A Geocoding request with region="fr" (France) will return a french city.
        response = map_client.geocode(self.msg_parsed, region='fr')
        pprint(response)

        try:
            # formatted_address is a string containing the human-readable address of this location.
            # return results[0].formatted_address is inside the callback function
            address=response[0]["formatted_address"]
            print(response[0])
            # pprint(address) # to erase
            # Get latitude & longitude from address
            lat=response[0]["geometry"]["location"]["lat"]
            # pprint(lat) # to erase
            lng=response[0]["geometry"]["location"]["lng"]
            # pprint(lng) # to erase

            return {
                "address": address,
                "latitude": lat,
                "longitude": lng
            }

        except IndexError:  # Raised when an index of a sequence does not exist
            return "no result"

        except KeyError:  # raised when try to access a key that isn’t in a dictionary
            return "no result"





