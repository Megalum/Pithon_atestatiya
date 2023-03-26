import csv

def file_list():
    my_dict = []
    with open("Data.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter = ";")
        for i in file_reader:
            my_dict.append(i)
        return my_dict

def write(my_dict):
    s = ''
    my_dict.sort(key=lambda r: r['Date'])
    for i in my_dict:
        for j in i.values():
            s += f'{j}\t'
        s += '\n'
    return s
