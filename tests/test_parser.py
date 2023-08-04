# -*- coding: utf-8 -*-

import unittest  # import in local variable TestCase Class from module unittest

from Flask_api.constant import control_characters
from Flask_api.constant import stopwords
from Flask_api.parser import Parser  # import in local variable Parser class in order to be used in test

# used as message received for TestParser_1
msg_received_1="@ afin Je cherche! absolument, Absolument afin le@ Chateau de+ versailles [!*'();:@&=+$,/?%#[] je"
# used as message received for TestParser_2, used because need a string into the parsing
msg_received_2=['afin', 'je', 'cherche', 'absolument', 'absolument', 'afin', 'le', 'chateau', 'de', 'versailles',
                'je']


class TestParser_1(unittest.TestCase):
    """TestCase is a class from the module unittest, group all tests needed, inherit from the unittest.TestCase"""

    def setUp(self):
        """Method called to prepare the test fixture"""
        self.p=Parser(msg_received_1, stopwords, control_characters)  # class Parser is instantiated

    def test_lower_character(self):
        """check upper characters are lowered; method assertEqual is used from TestCase class
        to compare expected result with result from lower_character method"""
        self.p.lower_character()
        self.assertEqual(self.p.msg_received, "@ afin je cherche! absolument, absolument afin le@ chateau"
                                              " de+ versailles [!*'();:@&=+$,/?%#[] je")

    def test_reserved_character(self):
        """check that reserved characters are take off for google map api"""
        self.p.reserved_character()
        self.assertEqual(self.p.msg_received, " afin Je cherche absolument Absolument afin le Chateau de "
                                              "versailles  je")

    def test_split_words(self):
        """check split string words and convert into a list"""
        self.p.split_words()
        self.assertEqual(self.p.msg_received,
                         ['@',
                          'afin',
                          'Je',
                          'cherche!',
                          'absolument,',
                          'Absolument',
                          'afin',
                          'le@',
                          'Chateau',
                          'de+',
                          'versailles',
                          "[!*'();:@&=+$,/?%#[]",
                          'je'])


class TestParser_2(unittest.TestCase):  # TestCase 2 uses msg_received_2 as a string
    """TestCase is a class from the module unittest, group all tests needed, inherit from the unittest.TestCase"""

    def setUp(self):
        """Method called to prepare the test fixture"""
        self.p=Parser(msg_received_2, stopwords, control_characters)

    def test_stop_words(self):
        """check that stop words are taking off from the  list message to keep key words"""
        self.p.stop_words()
        self.assertEqual(self.p.msg_received, ['le', 'chateau', 'versailles'])

    def test_join_msg(self):
        """check that all words are join into one string"""
        self.p.join_msg()
        self.assertEqual(self.p.msg_received, "afin je cherche absolument absolument afin le chateau de versailles je")


if __name__ == '__main__':  # run this test module directly
    unittest.main()
