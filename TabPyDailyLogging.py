#11-12-21 Finished script and implemented on server.

import os
import time
import shutil
import subprocess
import smtplib

#does all read/write for files
def fileIO(fileName,file_exists):
        #file doesnt exist
    if file_exists == False:
        #restart for loop and increment
        print("File doesnt exist tabpy_log.txt%s" %i)    
        return
    else:
        #file exists so open the file
        logFile = open(fileName,'r')
            
    #infinite loop if file exists    
    while file_exists == True: 
        #get next line from file
        line = logFile.readline()
            
        #if line is empty / end of file is reached
        if not line:
            #gives a new line between each file
            dailyLogFile.write('\n') 
            logFile.close()
            return successFlag #returns true if it wrote anything, false if it wrote nothing
            break
            
        #write to new log file each line
        successFlag = True
        dailyLogFile.write(line)

timestr = time.strftime("%m%d%Y") #current date and time
newLogFileName = '%sTabPyLogs.txt'%timestr #newly created log
localLocation = r'C'
networkLocation = r'C'
successFlag = False #determines writing to file was a success
sender = 'tabpy@x.com' #smtp sender
receivers = ['garrett@x.com'] #smtp receivers

#stop TabPy task scheduler job via powershell
subprocess.run("powershell -Command \"Stop-ScheduledTask -TaskName 'Task Scheduler Job Name'\"")

with open(localLocation,'a') as dailyLogFile:
    for i in range(5,0,-1): #counts from 5 to 1
        file_exists = os.path.exists(r'C')
        
        successFlag = fileIO(r'C',file_exists)
    
    #check to see if textfile.txt exists and calls fileIO for last log file
    file_exists = os.path.exists(r'C')
    successFlag = fileIO(r'C',file_exists)       
    
    #once everything is copied close the new log file
    dailyLogFile.close()
    
#check to make sure content is in new log file

#move new log file to network location
shutil.move(localLocation,networkLocation)   

#delete all old log files if log write was successful
if successFlag == True:
    for i in range(5,0,-1):
        #if file exists
        if os.path.exists(r'C'):
            os.remove(r'C') 
            
    os.remove(r'C')


#start tabpy task scheduler job via powershell
subprocess.run("powershell -Command \"Start-ScheduledTask -TaskName 'Task Scheduler Job Name'\"")    

if successFlag == True: #if successful send happy message
    message = """From: TabPy Server <tabpy@x>
To: <garrett@x>
Subject: TabPy Nightly Logging + Restart successful

Script ran successful
"""
elif successFlag == False: #if failed send unhappy message
    message = """From: TabPy Server <tabpy@x>
To: <garrett@x>
Subject: TabPy Nightly Logging + Restart FAILED

Script ran UNSUCCESSFUL. PLEASE CHECK TABPY STATUS!!
"""

try: #email receivers from sender
   smtpObj = smtplib.SMTP('x.com')
   smtpObj.starttls()
   
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
   
smtpObj.quit()