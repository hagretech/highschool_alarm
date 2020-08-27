import csv, smtplib, ssl
import datetime
message = """Subject: time to have fun

Hi {name}, we have done your first school round"""

from_address = "kirubelformnaletest@gmail.com"
password = 'kirubel@2020mn'

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("students.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )


### the alarm
            
first_alarm = 6
second_alarm = 7

while (True):
    if(first_alarm == datetime.datetime.now().hour ):
        pass
        
while (True):
    if(second_alarm == datetime.datetime.now().hour ):
        pass
