""" module that used wikipedia API"""

# Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
# https://pypi.org/project/wikipedia/

import wikipedia

wikipedia.set_lang("fr")  # to change the language of the Wikipedia you are accessing


class WikiSummary:
    """wiki api to find place data and summary"""

    def __init__(self, wiki, msg_parsed):
        self.address = []  # list of places proposed by Wikipedia
        self.wikipedia = wiki  #
        self.msg_parsed = msg_parsed  # user input message parsed
        self.summary = []  # place summary from wikipedia

    def get_address(self):
        """Get a panel of result from wikipedia API"""
        try:
            address = self.wikipedia.search(self.msg_parsed)
            print(type(address))  # to erase
            print(address)  # to erase
            if len(address) == 0:
                return 'no result'
            return address
        except wikipedia.exceptions.DisambiguationError:  # Exception raised when a page resolves to a Disambiguation
            # page
            print("reformulez votre demande")
            return "no result"
        except wikipedia.exceptions.PageError:  # wikipedia.exceptions.WikipediaException(error)
            print("La page n'existe pas")
            return "no result"
        except wikipedia.exceptions.HTTPTimeoutError:  # Exception raised if request to the Mediawiki servers times out
            print("Expiration serveur")
            return "no result"
        except wikipedia.exceptions.RedirectError:  # Exception raised when no Wikipedia matched a query
            print("Source non disponible")
            return "no result"

    def get_place_summary(self, address):
        """ Get the summary of the related place."""
        try:
            self.wikipedia.summary(address[0])  # choose first proposition of the list
            self.summary = self.wikipedia.summary(address[0])
            print(address[0])  # to erase
            print(self.summary)  # to erase
            print(type(self.summary))  # to erase
            return self.summary  # plain text summary of the page
        except Exception:
            return 'no result'
