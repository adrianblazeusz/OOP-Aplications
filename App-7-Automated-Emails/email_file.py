import yagmail
import pandas as pd

df = pd.read_excel("people.xlsx")

for index, row in df.iterrows():
    print(row)
    email = yagmail.SMTP(user="pythovtest@gmail.com", password="wbcdivlhdxlihrtt")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on about {row['interest']} today.",
               attachments="design.txt")

print(df)