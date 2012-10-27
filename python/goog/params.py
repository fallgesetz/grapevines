import urllib

class Params(object):
    """
    Build params using the Builder Pattern -- every method returns self!
    """

    def __init__(self, symbol):
        self.params_dict = {}
        # fields to show in the csv
        self.symbol(symbol).fields('d','c','v','o','h','l')

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

    def fields(self, *args):
        """
        Fields we've discovered
        @d -- date
        @c -- close
        @h -- high
        @l -- low
        @o -- open
        @v -- volume

        e.g.
        params.fields('d','c','v','o','h','l')
        """
        self.params_dict['f'] = ','.join(args)
        return self

    def sessions(self):
        """
        not entirely sure how to get this
        """
        self.params_dict['sessions'] = 'ext_hours'
        return self

    def __str__(self):
        return urllib.urlencode(self.params_dict)

def SmartParams(Params):
    """
    fills in sane default values
    """
    pass



