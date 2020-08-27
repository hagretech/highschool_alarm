import csv, smtplib, ssl

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