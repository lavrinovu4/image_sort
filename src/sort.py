import os, datetime
import sys
from shutil import copy

# format name: "YYYYMMDD_XXXXXX"
def parse_name(file_split_name):

    field_name = file_split_name.split("_")
    date = field_name[0]

    if (len(date) == 8) and (date.isdigit() == True) and (len(field_name) == 2):
        return dict(year=date[0:4], month=date[4:6], day=date[6:8])
    else:
        return 0

# on Windows should work OK, but linux - it is wrong
def get_time_from_file(filename):
    str_time = str(datetime.datetime.fromtimestamp(os.path.getctime(filename)))
    date = str_time.split(' ')[0].split('-')
    return dict(year=date[0], month=date[1], day=date[2])

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

def create_dir_tree(name):
    cur = os.getcwd()
    for folder in name.split('/'):
        if(os.path.isdir(folder) == 0):
            os.mkdir(folder)
        os.chdir(folder)

    os.chdir(cur)

def main():
    sort_list_jpg = []
    src_path = ''

    if(len(sys.argv) <= 1):
        src_path = '..'
    else:
        src_path = sys.argv[1]

    tree_src = get_tree(src_path)
    jpg_list = find_jpg(tree_src[1])

    for jpg in jpg_list:
        # only name of file for this function - delete dirs
        res = parse_name(jpg.split('/')[-1])
        if(res == 0):
            res = get_time_from_file(jpg)

        sort_list_jpg.append(dict(filename=jpg, date=res))

    for jpg in sort_list_jpg:
        src = jpg['filename']
        dst = "dst/" + jpg['date']['year'] + "/" + jpg['date']['month']
        if(os.path.exists(dst + "/" + src.split('/')[-1]) == 0):
            print("cp " + src + " " + dst)
            create_dir_tree(dst)
            copy(src, dst)

main()

