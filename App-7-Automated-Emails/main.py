import yagmail
import pandas as pd
from news import NewsFeed

df = pd.read_excel("people.xlsx")

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], from_date='2023-06-22', to_date='2023-06-23')

    email = yagmail.SMTP(user="email", password="password")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today. \n{news_feed.get()}\nAdrian.")