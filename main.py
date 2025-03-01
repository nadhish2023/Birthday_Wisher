import smtplib
import random
import datetime as dt
import pandas as pd

mail_id="nadhish.sn@gmail.com"
password="bfvgkwpopsvgmiiq"

birthdays=pd.read_csv("birthdays.csv")
now=dt.datetime.now()
day=now.day
month=now.month
for data in birthdays.values:
    if month==data[-2] and day==data[-1]:
        mail=data[1]
        name=data[0]
        with open(f"letter_{random.randint(1,5)}.txt","r") as fileobj:
            message=fileobj.read()
        message=message.replace("[Recipient_Name]",name)
        with open("quotes.txt") as fileobj:
            k = fileobj.read()
            ans = k.split("\n")
            quote=random.choice(ans)
        message=message.replace("[Motivational_Quote]",quote)
        print("--------->>>>>>>>>>>>")
        print("Birthday for ",name)
        print("--------->>>>>>>>>>>>")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=mail_id, password=password)
            connection.sendmail(from_addr=mail_id, to_addrs=mail,msg=message)
            connection.close()
        print("Message Sent:\n")
        print(message)