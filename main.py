import requests
import smtplib
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

smtp_address = os.environ["SMTP_ADDRESS"]
test_email = os.environ["EMAIL_ADDRESS"]
app_password = os.environ["EMAIL_PASSWORD"]
to_email = "TO_EMAIL_ID"

URL = "LINK_FOR_AMAZON_PRODUCT_PAGE
lowest_price = "LOWEST_PRICE"

response = requests.get(url=URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

#Searching for the Price
price_raw = soup.select("h5 div div span")[2].getText()
pt1 = price_raw.split(",")[0]
pt2 = price_raw.split(",")[1]
price = float(pt1 + pt2)
print(price)

#Searching for the title
title = soup.select("div h1 span")[0].getText()
print(title)

#Sending the mail
if price > lowest_price:
    with smtplib.SMTP(smtp_address, port=587) as connection:
        connection.starttls()
        connection.login(test_email, app_password)
        connection.sendmail(
            from_addr=test_email,
            to_addrs=to_email,
            msg=f"Subject: Amazon Price Alert!\n\nYou can buy {title} at the low price of INR {price}"
        )
