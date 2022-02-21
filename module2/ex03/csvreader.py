import sys


class CsvReader():

    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.file = None
        self.filename = filename
        self.sep = sep
        self.has_header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.header = None
        self.data = []
        self.fields_count = -1
        self.record_len = -1

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
            if (self.has_header):
                self.header = self.parse_header()
                if not self.header:
                    return None
            for line in self.file:
                line_data = self.parse_line(line)
                if (line_data):
                    self.data.append(line_data)
                else:
                    return None
            return self
        except Exception as e:
            print(e, file=sys.stderr)
            return None

    def __exit__(self, exc_type, exc_value, exc_traceback):
        try:
            self.file.close()
        except Exception:
            return

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        if self.skip_bottom == 0:
            self.skip_bottom = len(self.data)
        return self.data[self.skip_top:self.skip_bottom]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.header

    def parse_header(self):
        line = self.file.readline()
        fields = line.split(self.sep)
        if (line):
            self.fields_count = len(fields)
            return ([field.strip() for field in fields])
        print('header error', file=sys.stderr)
        return None

    def parse_line(self, line):
        if self.record_len == -1:
            self.record_len = len(line)

        if len(line) != self.record_len:
            print('records with different length.', file=sys.stderr)
            return None

        fields = line.split(self.sep)

        if self.fields_count == -1:
            self.fields_count = len(fields)

        if (len(fields) != self.fields_count):
            print('mistmatch between number of fields and number of records',
                  file=sys.stderr)
            return None

        return [field.strip() for field in fields]
