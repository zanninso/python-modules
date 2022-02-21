from csvreader import CsvReader

with CsvReader('good.csv', ',', header=True, skip_top=0, skip_bottom=1) as file:
    if file is not None:
        print(file.getdata())
        print(file.getheader())

with CsvReader('bad.csv') as file:
    if file is None:
        print("File is corrupted")
