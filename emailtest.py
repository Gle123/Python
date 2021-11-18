import smtplib

sender = 'tabpy@x.com'
receivers = ['garrett@x.com']

message = """From: TabPy Server <tabpy@x>
To: <garrett@x.com>
Subject: TabPy Nightly Logging + Restart

Script ran successful
"""

try:
   smtpObj = smtplib.SMTP('x.com')
   smtpObj.starttls()
   
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
   
smtpObj.quit()