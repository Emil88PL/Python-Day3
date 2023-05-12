import struct
from myfile import Myfile

class TextFile(Myfile):
    def contents(self):
        return open(self.get_filename(), 'rt').read()
    def contents(self, value):
        if not value.endswith('\n'):
            value += '\n'
            open(self.get_filename(), 'at').write(value)
        else:
            open(self.get_filename(), 'ab ').write(value.encode())

class BinFile(Myfile):
    def contents(self):
        return open(self.get_filename(), "rt").read()
    def contents(self, value):
        if isinstance(value, int):
            out =struct.pack("i", value)
            open(self.get_filename(), 'ab').write(out)
        else:
            open(self.get_filename(), 'ab ').write(value.encode())

if __name__ == '__main__':
    file1 = TextFile("file1.txt")
    print(file1, len(file1))

    file1.contents = "Hello"
    file1.contents = "World"

    file2 = BinFile("file2.dat")
    print(file2, len(file2))

    file2.contents = 42
    file2.contents = 23
    file2.contents = "EOD"

    print(file2.contents)
    print("Size of file2:", len(file2))
