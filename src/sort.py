import os, datetime
import sys
from shutil import copy
import argparse
import platform

if (platform.system() == 'Linux'):
    path_delim = '/'
else:
    path_delim = '\\'

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

    if(path[-1] == path_delim):
        path = path[:-1]

    for r, d, f in os.walk(path):
        dirs += [r + path_delim + x for x in d]
        files += [r + path_delim + x for x in f]

    return [dirs, files]

def find_jpg(file_list):
    file_jpg = []
    for f in file_list:
        if(f.endswith('.jpg')):
            file_jpg.append(f)

    return file_jpg

def create_dir_tree(name):
    cur = os.getcwd()
    for folder in name.split(path_delim):
        if(os.path.isdir(folder) == 0):
            os.mkdir(folder)
        os.chdir(folder)

    os.chdir(cur)

def main():

    parser = argparse.ArgumentParser(description="Sort image in folders")
    parser.add_argument("-s", "--source", required="true")
    parser.add_argument("-d", "--destination", required="true")
    parser.add_argument("-x", "--delete", action="store_true")
    parser.add_argument("-p", "--prefix")
    parser.add_argument("-y", "--year")
    parser.add_argument("-m", "--month")
    parser.add_argument("-r", "--rename", action="store_true")
    parser.add_argument("-c", "--count", action="store_true", help="Print number of copied/moved jpg files")
    args = parser.parse_args()

    if(args.prefix != None):
        prefix = args.prefix
    else:
        prefix = ""

    if(args.year != None):
        dYear = args.year
    else:
        dYear = 0

    if(args.month != None):
        dMonh = args.month
    else:
        dMonth = 0

    sort_list_jpg = []
    number_cp = 0
    number_rm = 0

    # get list of jpg
    tree_src = get_tree(args.source)
    jpg_list = find_jpg(tree_src[1])

    # analyze jpg - time of creation
    for jpg in jpg_list:
        # only name of file for this function - delete dirs
        res = parse_name(jpg.split('/')[-1])
        if(res == 0):
            res = get_time_from_file(jpg)

        sort_list_jpg.append(dict(filename=jpg, date=res))

    # copied jpg files
    for jpg in sort_list_jpg:
        src = jpg['filename']

        if(dYear == 0):
            dYear = jpg['date']['year']

        if(dMonth == 0):
            dMonth = jpg['date']['month']

        dst_dir = args.destination + path_delim + dYear + path_delim + dMonth

        if(args.rename != 0):
            dst_file_name = dYear + dMonth + jpg['date']['day'] + ".jpg"
        else:
            dst_file_name = src.split(path_delim)[-1]

        dst = dst_dir + path_delim + prefix + dst_file_name

        if(os.path.exists(dst) == 0):
            print("cp " + src + " " + dst)
            create_dir_tree(dst_dir)
            copy(src, dst)
            number_cp += 1

    # removed jpg files
    if(args.delete != 0):
        for jpg in sort_list_jpg:
            jpg_file = jpg['filename']
            print("rm " + jpg_file)
            os.remove(jpg_file)
            number_rm += 1

    if(args.count != 0):
        print("Number of copied files: %d" % number_cp)
        print("Number of removed files: %d" % number_rm)

main()

