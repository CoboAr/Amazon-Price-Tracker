import requests, os
import lxml
from bs4 import BeautifulSoup
import smtplib

# Email address data with environment variables
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECIPIENT_EMAIL = os.environ.get("MY_EMAIL")

# Amazon product endpoint
url = "https://www.amazon.ca/Fantasylab-Computer-Ergonomic-Adjustable-Support/dp/B0BS144MG4/ref=sr_1_3_sspa?crid=S120KFDEUK4U&keywords=coding%2Bchair&qid=1703652479&sprefix=coding%2Bchari%2Caps%2C133&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# Test current price with buy price and notify the user via email if current price < buy price
title = soup.find(id="productTitle").get_text().strip()
print(title)
BUY_PRICE = 350

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )