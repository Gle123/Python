#06-16-22 Finished script and implemented on server.

import os
import shutil
import subprocess
import sys

licenses = []
fName1 = ''

if len(sys.argv) != 2:
    print("Make sure to provide 1 arguments")
#    return 2
else:
    fName1 = sys.argv[1] #name of license text file
      
try: #opening text file 1
    with open(fName1) as txtFile1:
        for line in txtFile1:
            licenses.append(line.rstrip())
        #save license keys to list w/o whitespace
        txtFile1.close()
except IOError:
    print("Could not read file:",fName1)
#    return 1
    
#activate licenses one by one
for i in range(len(licenses)):
    os.system('tsm licenses activate --license-key %s' %licenses[i])
 
