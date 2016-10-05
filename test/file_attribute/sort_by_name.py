#!/usr/bin/python3

import os

# format name: "YYYYMMDD_XXXXXX"
def parse(file_split_name):

    if (file_split_name[1] == "jpg"):
        print("Parsing...")
        
        field_name = file_split_name[0].split("_")
        date = field_name[0]

        if (len(date) == 8):
            year = date[0:4]
            month = date[5:6]
            day = date[7:8]
        
            return (day, month, year)
        else:
            return 0

for filename in os.listdir('.'):
    print(filename)

    if(len(filename) == 19):
        file_split_name = filename.split('.')

        # is file?
        if (len(file_split_name) > 1):
                res = parse(file_split_name)

                if (res != 0):
                    print(res)


