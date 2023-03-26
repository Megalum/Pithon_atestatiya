import datetime
import csv

def rewrite(my_dict, id, head, boby):
    now = datetime.datetime.now()
    dict = {    'Head': head, 
                'Body': boby,
                'Date': str(now)
    }
    my_dict[id].update(dict)

    with open("Data.csv", mode="w", encoding='utf-8') as w_file:
        names = []
        for i in my_dict[0].keys():
            names.append(i)
        file_writer = csv.DictWriter(w_file, delimiter = ";", 
                                    lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for i in my_dict:
            file_writer.writerow(i)
    