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
# on Windows should work OK, but linux - it is wrong
def get_time_from_file(filename):
    str_time = str(datetime.datetime.fromtimestamp(os.path.getctime(filename)))
    return str_time.split(' ')[0].split('-')

def get_tree(path):
    dirs = []
    files = []

    for r, d, f in os.walk(path):
        dirs += [r + '/' + x for x in d]
        files += [r + '/' + x for x in f]

    return [dirs, files]

def find_jpg(file_list):
    file_jpg = []
    for f in file_list:
        if(f.endswith('.jpg')):
            file_jpg.append(f)

    return file_jpg

def main():
    sort_list_jpg = []

    tree_src = get_tree('..')
    jpg_list = find_jpg(tree_src[1])

    for jpg in jpg_list:
        # only name of file for this function - delete dirs
        res = parse_name(jpg.split('/')[-1])
        if(res == 0):
            res = get_time_from_file(jpg)

        sort_list_jpg.append((jpg, res))

    print(sort_list_jpg)

main()

