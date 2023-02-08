filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']

filenames_new = []
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    filenames_new.append(filename)

print(filenames_new)