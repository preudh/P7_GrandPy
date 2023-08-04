# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch  # import of patch decorator from unittest module

from Flask_api.wiki import WikiSummary


# address = self.wikipedia.search(self.msg_parsed)

class TestWikiSummary(TestCase):
    @patch('Flask_api.wiki.WikiSummary.get_address')  # We set up the decorator that takes the object to mock as
    # argument
    def test_get_address(self, mock_get_address_from_api):  # The decorator injects the mocker object into the
        # function as an argument to the method. The argument name is free of choice. return_value method is used to
        # associate the desired return value with the mock.
        expected_result=['Château de Versailles', 'Versailles', 'Traité de Versailles',
                         'Orangerie du château de Versailles', 'Jardin de Versailles',
                         'Parc de Versailles', 'Versailles (série télévisée)',
                         'Chronologie du château de Versailles', 'Chapelle royale de Versailles',
                         'Opéra royal du château de Versailles']

        mock_get_address_from_api.return_value = expected_result

        address_proposed=WikiSummary(self, "le chateau versailles")  # class WikiSummary is instantiated
        # We use the assertEqual method of the TestCase class to compare the value returned by the method we are
        # testing with the expected result
        self.assertEqual(address_proposed.get_address(), expected_result)


class TestWikiSummary_2(TestCase):
    @patch('Flask_api.wiki.WikiSummary.get_place_summary')
    def test_get_place_summary(self, mock_get_summary):
        expected_result="La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est " \
                        "en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue " \
                        "d'Hauteville et la troisième en impasse. "

        mock_get_summary.return_value=expected_result
        # class WikiSummary is instantiated
        summary_proposed = WikiSummary(self, ['7 cité Paradis, 75010 Paris.'])
        # We use the assertEqual method of the TestCase class to compare the value returned by the method we are
        # testing with the expected result
        self.assertEqual(summary_proposed.get_place_summary("7 cité Paradis, 75010 Paris."), expected_result)
