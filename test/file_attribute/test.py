
import os, datetime

def get_time_from_file(filename):
    str_time = str(datetime.datetime.fromtimestamp(os.path.getctime(filename)))
    return str_time.split(' ')[0].split('-')

for filename in os.listdir('.'):
    print (filename)
    print(get_time_from_file(filename))

