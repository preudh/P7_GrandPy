"""get message from user and parses it"""

# -*- coding: utf-8 -*-


class Parser:
    """ class cleaning & extracting relevant words from query submitted by user"""

    def __init__(self, msg_received, stopwords, control_characters):
        """
        :type stopwords: string

        """
        self.msg_received = msg_received  # user message inputs
        self.stopwords = stopwords  # words to get rid off - list type
        self.control_characters = control_characters  # characters to get rid off - string type

    def process_parser(self, ):

        self.lower_character()
        self.reserved_character()
        self.split_words()
        self.stop_words()
        self.join_msg()
        return self.msg_received

    def lower_character(self, ):
        """ upper characters in the string"""
        self.msg_received = self.msg_received.lower()
        print(self.msg_received)

    def reserved_character(self, ):
        """remove special characters in the string"""
        for e in self.msg_received:
            for i in self.control_characters:
                if e == i:
                    self.msg_received = self.msg_received.replace(e, "")  # Control characters and/or Text Strings
                    print(self.msg_received)
                    # according google api

    def split_words(self, ):
        """split string words and convert into a list"""
        self.msg_received = self.msg_received.split()
        print(self.msg_received)

    def stop_words(self, ):
        """ remove word not necessary"""
        for word in self.msg_received:
            for stop_word in self.stopwords:
                if word == stop_word:
                    while self.msg_received.count(stop_word) > 0:  # allow removing all occurrences of stop_word in List
                        self.msg_received.remove(stop_word)
                        print(self.msg_received)

    def join_msg(self, ):
        """ join words in the list and get final parsed string """
        self.msg_received = " ".join(self.msg_received)
        print(self.msg_received)





