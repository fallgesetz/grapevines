import urllib
import csv

URL_GETPRICES = "http://www.google.com/finance/getprices?%s"

class Getter(object):
    def __init__(self, params):
        f = urllib.urlopen(URL_GETPRICES % params)
        # first n lines will be reiteration of params.
        n = len(params.keys())
        # these must be called in sequence
        header_lines = []
        for i in xrange(n):
            header_lines.append(f.next())
        self.header = self.parse_headers(header_lines)
        self.body = self.parse_body(f)


    def parse_headers(self, headers):
        header_dict = {}
        for line in headers:
            try:
                k, v = line.strip().split('=')
                header_dict[k] = v
            except Exception:
                header_dict[line] = ""
        return header_dict


    def parse_body(self, body):
        reader = csv.DictReader(body, fieldnames=self.header['COLUMNS'])
        pass
