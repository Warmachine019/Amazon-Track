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

URL = ("https://www.amazon.in/Google-Pixel-Watch-Smartwatch-Stainless/dp/B0BGX1CSRY/ref=sr_1_1?crid=3TYU2Q18JO2C4&dib"
       "=eyJ2IjoiMSJ9.jBogAUyW-VMN-1ZzI9R4ZQXgNMnyjq1NFX1Y14gN9tahQnwb56Z-94TU7z7h2hoAI-8"
       "-6Pm7BtpjoBhStdd8vzGN_oO8mk44iVBW8ncsFPjYt6x36GYIa52HEVjAwB8sTbX7J"
       "-bTC5K18Mu6qOsodWs_LevL65oB92PhBmnahYAG77MT97nIL7-iTRmTlieaXqDvq-KdMjjePc_6UAxnOhDtzTzq95As0PBYnj8VXAM"
       ".rWhXBcXbn1DDZj0-3EvocNYe3tPqqF4eoSCVjQQ35WM&dib_tag=se&keywords=pixel+watch&qid=1735807315&sprefix=pixel"
       "+watc%2Caps%2C245&sr=8-1")
lowest_price = 17000

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
