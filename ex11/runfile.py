from myfile import Myfile

filea = Myfile("country.txt")
print(filea)

print(filea.get_filename(), "is", len(filea), "bytes")