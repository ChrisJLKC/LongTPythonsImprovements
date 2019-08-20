import csv
from datetime import datetime


class Data_Handling:

    def write_to_csv(self, data):
        sensordata = (data[0][0], data[0][2], data[0][1])
        row = [datetime.now(), *sensordata, data[1]]
        with open('data.csv', 'a') as data_file:
            csv_writer = csv.writer(data_file)
            csv_writer.writerow(row)
