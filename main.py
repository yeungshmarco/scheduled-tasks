import os
import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = os.environ.get("MY_EMAIL")
PWD = os.environ.get("PWD")

df = pd.read_csv("birthdays.csv")
data = df.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day
for datapoint in data:
    if datapoint["month"] == month and datapoint["day"] == day:
        file_chosen = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_chosen, "r") as template:
            contents = template.read()
            contents = contents.replace("[NAME]", datapoint["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PWD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=datapoint["email"],
                                msg=f"Subject:Happy Birthday!\n\n{contents}")
    
