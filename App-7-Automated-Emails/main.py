import yagmail
import pandas as pd
from news import NewsFeed

df = pd.read_excel("people.xlsx")

for index, row in df.iterrows():
<<<<<<< HEAD:App-7-Automated-Emails/main.py
    news_feed = NewsFeed(interest=row['interest'], from_date='2023-06-22', to_date='2023-06-23')

    email = yagmail.SMTP(user="email", password="password")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today. \n{news_feed.get()}\nAdrian.")
=======
    print(row)
    email = yagmail.SMTP(user="mail", password="password")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today.",
               attachments="design.txt")

print(df)
>>>>>>> 3d9b93b4c3375ec5e7c50f79c111d311663bdb44:App-7-Automated-Emails/email_file.py
