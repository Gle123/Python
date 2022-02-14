#Script to automatically run logshark at night.
#Copies nightly log file to local location. Runs Logshark. 

import os
import time
import shutil
import smtplib
import subprocess

directory = r'\\fake\path'
timestr = time.strftime("%Y%m%d") #current date and time
logFileName = 'tablogs_%s.zip'%timestr #newly created log
transferDirectory = r'\\fake\path' 
logFileDirectoryPath = r'\\fake\path'
newLogsharkName = r'\\fake\path'
universalDirectory = r'\\fake\path'
sender = 'tabpy@veteransunited.com' #smtp sender
receivers = ['garrett.le@veteransunited.com'] #smtp receivers
successFlag = True #currently no error testing

#move file from network location to local location.
shutil.copy(transferDirectory,directory)

os.chdir('\\fake\path')
print(os.getcwd())

#runs logshark process
subprocess.run('powershell -Command \"logshark %s %slogshark --force-run-id"' %(logFileDirectoryPath, timestr)) 

#after process is done. Move new folder to Universal Drive
shutil.copytree(newLogsharkName,universalDirectory) 

#Delete logs on local
os.remove(logFileDirectoryPath)

#email
if successFlag == True: #if successful send happy message
    message = """From: TabPy Server <x@x.com>
To: <x@x.com>
Subject: Logshark ran successful

Script ran successful
"""
elif successFlag == False: #if failed send unhappy message
    message = """From: TabPy Server <x@x.com>
To: <x@x.com>
Subject: Logshark unsuccessful

Script ran UNSUCCESSFUL. PLEASE CHECK Logshark status!!
"""

try: #email receivers from sender
   smtpObj = smtplib.SMTP('smtp server')
   smtpObj.starttls()
   
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
   
smtpObj.quit()