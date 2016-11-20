# -*- coding: utf-8 -*-
import argparse
import core
import interface

def main():

    parser = argparse.ArgumentParser(description="Sort image in folders")
    parser.add_argument("-s", "--source")
    parser.add_argument("-d", "--destination")
    parser.add_argument("-x", "--delete", action="store_true")
    parser.add_argument("-p", "--prefix")
    parser.add_argument("-y", "--year")
    parser.add_argument("-m", "--month")
    parser.add_argument("-r", "--rename", action="store_true")
    parser.add_argument("-c", "--count", action="store_true", help="Print number of copied/moved jpg files")
    parser.add_argument("-g","--gui", action="store_true")
    args = parser.parse_args()

    if(args.gui == 0):
        if((args.source != None) and (args.destination != None)):
            parameters = {
                          'delete': args.delete,
                          'rename': args.rename,
                         }

            if(args.prefix == None):
                parameters['prefix'] = ""

            if(args.year == None):
                parameters['year'] = ""

            if(args.month == None):
                parameters['month'] = ""

            (numberCp, numberRm) = core.sortImgs(args.source, args.destination, parameters)

            if(args.count != None):
                print("Number of copied files: %d" % numberCp)
                print("Number of removed files: %d" % numberRm)
        else:
            print('Error, args -s and -d are required')
    else:
        interface.interface()

if __name__ == "__main__":
    """
        Сортування картинок, програма, яка надіюсь допоможе комусь для сортування 
        великої кількості фото.
        Написав: lavr
        Надихнула: volowka
    """
    main()

