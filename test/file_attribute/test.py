# added.sort(key=lambda x: os.stat(os.path.join(path_to_watch, x)).st_mtime)
#
#
#
#
# import os, time
# path_to_watch = 'c://Users//seplema//Documents//arvuti'
# before = dict([(f, None) for f in os.listdir (path_to_watch)])
# while 1:
#     after = dict([(f, None) for f in os.listdir (path_to_watch)])
#     added = [f for f in after if not f in before]
#     if before == after:
#         1==1
#     else:
#         if len(added)==1:
#             print added[0]
#         else:
#             for i in range (0,len(added)):
#                 print added[i]
#     time.sleep(10)
#     before = after
#
#
#
#
#
#
#
#
#
#
# import os
#
# search_dir = "/mydir/"
# os.chdir(search_dir)
# files = filter(os.path.isfile, os.listdir(search_dir))
# files = [os.path.join(search_dir, f) for f in files] # add path to each file
# files.sort(key=lambda x: os.path.getmtime(x))
#
#
#
#
# http://effbot.org/zone/python-fileinfo.htm
#
#

import os
for filename in os.listdir('.'):
    print (filename)
    info = os.stat(filename)
    print(info.st_mtime)

