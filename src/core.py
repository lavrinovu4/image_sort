import os, datetime
import sys
from shutil import copy
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
    if not os.path.exists(name):
        os.makedirs(name)

def sortImgs(sourceDir, dstDir, parameters):
    sortListJpg = []
    numberCp = 0
    numberRm = 0
    prefix = parameters['prefix']
    dYear = parameters['year']
    dMonth = parameters['month']

    if(dstDir[-1] == pathDelim):
        dstDir = dstDir[:-1]

    if(sourceDir[-1] == pathDelim):
        sourceDir = sourceDir[:-1]

    if(sourceDir != dstDir):
        cDstDir = dstDir

        # get list of jpg
        treeSrc = getTree(sourceDir)
        jpgList = findJpg(treeSrc[1])

        # analyze jpg - time of creation
        for jpg in jpgList:
            # only name of file for this function - delete dirs
            res = parseName(jpg.split(pathDelim)[-1])
            if(res == 0):
                res = getTimeFromFile(jpg)

            sortListJpg.append(dict(filename=jpg, date=res))


        # copied jpg files
        for jpg in sortListJpg:
            src = jpg['filename']

            if(dYear == ""):
                dYear = jpg['date']['year']

            if(dMonth == ""):
                dMonth = jpg['date']['month']

            dstDir = cDstDir + pathDelim + dYear + pathDelim + dMonth

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

