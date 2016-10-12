import os, datetime

# format name: "YYYYMMDD_XXXXXX"
def parse_name(file_split_name):

    field_name = file_split_name.split("_")
    date = field_name[0]

    if (len(date) == 8) and (date.isdigit() == True):
        year = date[0:4]
        month = date[4:6]
        day = date[6:8]
    
        return [year, month, day]
    else:
        return 0

def get_time_from_file(filename):
    str_time = str(datetime.datetime.fromtimestamp(os.path.getctime(filename)))
    return str_time.split(' ')[0].split('-')

def main():
    for filename in os.listdir('.'):
        print(filename)
        print(parse_name(filename))

        # if(len(filename) == 19):
        #     file_split_name = filename.split('.')
        #
        #     # is file?
        #     if (len(file_split_name) > 1):
        #             res = parse(file_split_name)
        #
        #             if (res != 0):
        #                 print(res)

    for filename in os.listdir('.'):
        print (filename)
        print(get_time_from_file(filename))

main()

