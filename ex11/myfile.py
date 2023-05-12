import os.path

class Myfile(object):
    def __init__(self, filename):
        self._filename = filename

    def __str__(self):
        s = open(self._filename).read()
        return s
    
    def __len__(self):
        return os.path.getsize(self._filename)
    def get_filename(self):
        return self._filename
    