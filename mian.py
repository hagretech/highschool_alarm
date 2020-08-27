import csv, smtplib, ssl
import datetime
message = """Subject: time to have fun

Hi {name}, we have done your first school round"""

from_address = "kirubelformnaletest@gmail.com"
password = 'kirubel@2020mn'



# the alarm        
first_alarm = 25  # it is in hour
second_alarm = 26 # it is in hour

# while loop for 10th and 9th graders
while (True):
    if(first_alarm == datetime.datetime.now().minute ):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(from_address, password)
            with open("students.csv") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for name, email, grade in reader:
                    if(int(grade) == 9 or int(grade) == 10):
                        server.sendmail(
                            from_address,
                            email,
                            message.format(name=name,grade=grade),
                        )
                        print('sent')
                break
      
# while loop for 10th and 9th graders
while (True):
    if(second_alarm == datetime.datetime.now().minute ):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(from_address, password)
            with open("students.csv") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for name, email, grade in reader:
                    if(int(grade) == 11 or int(grade) == 12):
                        server.sendmail(
                            from_address,
                            email,
                            message.format(name=name,grade=grade),
                        )
                        print('sent')
                break
                
print('program is now disactivated run it again for activate toworrows alarm')