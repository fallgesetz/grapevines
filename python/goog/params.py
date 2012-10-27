import datetime

class Params(object):
    """
    Build params using the Builder Pattern -- every method returns self!
    """

    def __init__(self, symbol):
        self.params_dict = {}
        # fields to show in the csv
        self.fields = {}
        self.symbol(symbol)

    def symbol(self, symbol):
        self.params_dict['q'] = symbol
        return self

    def time(self, d):
        """
        @d is a unix timestamp
        """
        self.params_dict['ts'] = d
        return self

    def exchange(self, x):
        self.params_dict['x'] = x
        return self

    def interval(self, i):
        self.params_dict['i'] = i
        return self

    def range(self, range):
        self.params_dict['p'] = range
        return self

    def fields(self, date=True, close=True, high=True, low=True, open=True, volume=True):
        pass


