import csv

def add_data(out):
    my_dict = {
        'ID':'',
        'Head':'',
        'Body':'',
        'Date':''
    }
    my_list = out.split(';')
    j = 0
    for i in my_dict:
        my_dict[i] = my_list[j]
        j += 1
    with open("Data.csv", mode="a", encoding='utf-8') as w_file:
        names = []
        for i in my_dict.keys():
            names.append(i)
        file_writer = csv.DictWriter(w_file, delimiter = ";", 
                                 lineterminator="\r", fieldnames=names)
        file_writer.writerow(my_dict)