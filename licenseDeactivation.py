#06-16-22 Finished script and implemented on server.

import os
import shutil
import subprocess

#saves list of licenses
licenseList = [] #list with duplicates
licenseList2 = [] #list without duplicates
localLocation = r'x' 
newFileName = r'x'
successFlag = True #determines writing to file was a success

#does all read/write for files
def fileIO(fileName,file_exists):
    licenseLine = ''
    
    if file_exists == False:
        #file doesnt exist
        print("Issue creating file with script. Please delete %s" %newFileName)    
        return False
    else:
        #file exists so open the file
        licenseFile = open(fileName,'r')
            
    #infinite loop if file exists    
    while file_exists == True: 
        #get next line from file
        line = licenseFile.readline()
#        print(line)
        

        #if line is empty / end of file is reached
        if not line:
            #gives a new line between each file
            break
        #if line starts with TS indicates Tableau Server License Key
        if line[0] == 'T':
            if line[1] == 'S':
                licenseLine = ''
                
                for j in range(24): #length of the keys
                    licenseLine = licenseLine + line[j]
                #parse thru and save the licenses
                licenseList.append(licenseLine)
                #check to see if any duplicates in list
                [licenseList2.append(licenseLine) for x in licenseList if x not in licenseList2]

        print(licenseList2) #display no duplicate list
        
    return True

#change local directory to localLocation
os.chdir(localLocation)

#create text file if it does not exist
if os.path.exists(newFileName):
    successFlag = False
    print("File exists already. Please delete %s" %newFileName)

else:
    #send license output to newFileName location
    os.system('tsm licenses list > %s' %newFileName)

#Parse thru tsm licenses list command
successFlag=fileIO(newFileName,successFlag)
 
for i in range(len(licenseList2)):
    os.system('tsm licenses deactivate --license-key %s' %licenseList2[i])
 
#delete file if creation was successful
if successFlag == True:
    #if file exists
    if os.path.exists(newFileName):
        os.remove(newFileName) 

#if something failed within script
if successFlag == False:
    print("Script failed. Please check status of script")