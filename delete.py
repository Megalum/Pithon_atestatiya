import csv

def dell_data(out, id):
    out.pop(id)
    with open("Data.csv", mode="w", encoding='utf-8') as w_file:
        names = []
        for i in out[0].keys():
            names.append(i)
        file_writer = csv.DictWriter(w_file, delimiter = ";", 
                                    lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for i in out:
            file_writer.writerow(i)
