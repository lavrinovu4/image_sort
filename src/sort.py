#!/usr/bin/python

import os, datetime
import sys
from shutil import copy
import argparse
import platform

if (platform.system() == 'Linux'):
    pathDelim = '/'
else:
    pathDelim = '\\'

# format name: "YYYYMMDDxXXXXX"
def parseName(fileSplitName):

    fieldName = fileSplitName.split("_")
    date = fieldName[0]

    if (len(date) == 8) and (date.isdigit() == True) and (len(fieldName) == 2):
        return dict(year=date[0:4], month=date[4:6], day=date[6:8])
    else:
        return 0

# on Windows should work OK, but linux - it is wrong
def getTimeFromFile(filename):
    strTime = str(datetime.datetime.fromtimestamp(os.path.getctime(filename)))
    date = strTime.split(' ')[0].split('-')
    return dict(year=date[0], month=date[1], day=date[2])

def getTree(path):
    dirs = []
    files = []

    if(path[-1] == pathDelim):
        path = path[:-1]

    for r, d, f in os.walk(path):
        dirs += [r + pathDelim + x for x in d]
        files += [r + pathDelim + x for x in f]

    return [dirs, files]

def findJpg(fileList):
    fileJpg = []
    for f in fileList:
        if(f.endswith('.jpg')):
            fileJpg.append(f)

    return fileJpg

def createDirTree(name):
    cur = os.getcwd()
    for folder in name.split(pathDelim):
        if(os.path.isdir(folder) == 0):
            os.mkdir(folder)
        os.chdir(folder)

    os.chdir(cur)

def sortImgs(sourceDir, dstDir, sortListJpg, parameters):
    numberCp = 0
    numberRm = 0
    prefix = parameters['prefix']
    dYear = parameters['year']
    dMonth = parameters['month']

    if(prefix == None):
        prefix = ""

    if(dYear == None):
        dYear = 0

    if(dMonth == None):
        dMonth = 0

    # get list of jpg
    treeSrc = getTree(sourceDir)
    jpgList = findJpg(treeSrc[1])

    # analyze jpg - time of creation
    for jpg in jpgList:
        # only name of file for this function - delete dirs
        res = parseName(jpg.split('/')[-1])
        if(res == 0):
            res = getTimeFromFile(jpg)

        sortListJpg.append(dict(filename=jpg, date=res))

    # copied jpg files
    for jpg in sortListJpg:
        src = jpg['filename']

        if(dYear == 0):
            dYear = jpg['date']['year']

        if(dMonth == 0):
            dMonth = jpg['date']['month']

        dstDir = dstDir + pathDelim + dYear + pathDelim + dMonth

        if(parameters['rename'] != 0):
            dstFileName = dYear + dMonth + jpg['date']['day'] + ".jpg"
        else:
            dstFileName = src.split(pathDelim)[-1]

        dst = dstDir + pathDelim + prefix + dstFileName

        if(os.path.exists(dst) == 0):
            print("cp " + src + " " + dst)
            createDirTree(dstDir)
            copy(src, dst)
            numberCp += 1

    # removed jpg files
    if(parameters['delete'] != 0):
        for jpg in sortListJpg:
            jpgFile = jpg['filename']
            print("rm " + jpgFile)
            os.remove(jpgFile)
            numberRm += 1

    return (numberCp, numberRm)

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

    parameters = {'delete': args.delete,
                  'rename': args.rename,
                  'prefix': args.prefix,
                  'year': args.year,
                  'month': args.month
                  }

    sortListJpg = []

    (numberCp, numberRm) = sortImgs(args.source, args.destination, sortListJpg, parameters)

    if(args.count != None):
        print("Number of copied files: %d" % numberCp)
        print("Number of removed files: %d" % numberRm)

main()

