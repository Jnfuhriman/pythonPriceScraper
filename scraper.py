import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.com/Arcturus-Heavy-Duty-Survival-Blanket/dp/B01H6NC8XU/ref=sr_1_5?crid=25CDWAUZ17485&dchild=1&keywords=arcturus+heavy+duty+survival+blanket&qid=1596495721&sprefix=arcturus%2Caps%2C208&sr=8-5'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

def checkPrice():
    page = requests.get(url, headers = headers)
    soup1 = BeautifulSoup(page.content,'html.parser')
    soup = BeautifulSoup(soup1.prettify(), "html.parser")

    price = soup.find(id='priceblock_saleprice').get_text().strip()
    converted_price = float(price[1:3])
    if (converted_price < 20):
        print("price is acceptable")
        sendNotification()

def sendNotification():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('jfscrapeacc@gmail.com','onzojnjnandrovlk')
    subject = 'Price check'
    body = 'Time to buy https://www.amazon.com/Arcturus-Heavy-Duty-Survival-Blanket/dp/B01H6NC8XU/ref=sr_1_5?crid=25CDWAUZ17485&dchild=1&keywords=arcturus+heavy+duty+survival+blanket&qid=1596495721&sprefix=arcturus%2Caps%2C208&sr=8-5' 
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'jfscrapeacc@gmail.com',
        'jnfuhriman@gmail.com',
        msg
    )
    print('notification sent')
    server.quit()

    checkPrice()

