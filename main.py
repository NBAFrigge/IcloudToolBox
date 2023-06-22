import pandas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests
import warnings 
warnings.filterwarnings(action='ignore', category=DeprecationWarning)
import os
import datetime

r = requests.session()

def login():
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
  
    driver.get("https://www.icloud.com/?s=Iseo")
    sleep(2)
    input("Press Enter after the login")

    for cookie in driver.get_cookies():
            c = {cookie['name']: cookie['value']}
            r.cookies.update(c)
    f = open("cookies.txt", "w")
    f.write(str(r.cookies))
    f.close()

def genmail():
    try:
        headers={
                    "Connection": "keep-alive",
                    "Pragma": "no-cache",
                    "Cache-Control": "no-cache",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
                    "Content-Type": "text/plain",
                    "Accept": "*/*",
                    "Origin": "https://www.icloud.com",
                    "Referer": "https://www.icloud.com/",
                    "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8,cs;q=0.7",
                }
        payload = 'langCode:it-it'
        data = r.post(url = "https://p32-maildomainws.icloud.com/v1/hme/generate", headers=headers, cookies=r.cookies, data = payload).json()
        payload = {
                    "hme": (data["result"]["hme"])[0:len(data["result"]["hme"])],
                    "label": "TooManyTools",
                    "note": "",
                }
        data = r.post(url = "https://p32-maildomainws.icloud.com/v1/hme/reserve", headers=headers, cookies=r.cookies, json = payload).json()

        if data["success"] == True:
            print("[" + data["result"]["hme"]["hme"] + "] : Email Successfully created!")
        elif "error" in data: 
            print(data["error"]["errorMessage"])
            return "ratelimited" 
        else: 
            print("Something went wrong!")
    except KeyError: 
        print("Something went wrong, problaby ratelimited")
    except Exception as e: 
        print("Something went wrong!") 
    return "ok"

def Emailist():
    headers={
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
            "Content-Type": "text/plain",
            "Accept": "*/*",
            "Origin": "https://www.icloud.com",
            "Referer": "https://www.icloud.com/",
            "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8,cs;q=0.7",
        }
    data = eval((r.get(url = "https://p32-maildomainws.icloud.com/v1/hme/list", headers=headers, cookies=r.cookies).text).replace('true', 'True').replace('false', 'False'))
    return(data["result"]["hmeEmails"])

def cookies():
    cookies = open('cookies.txt', 'r')
    cookies = cookies.read()
    cookies = cookies.replace("<RequestsCookieJar[", "")
    cookies = cookies.replace(" for />]>", "")
    cookies = cookies.split(",")
    for x in range(0, len(cookies)):
        cookies[x] = cookies[x].replace("<Cookie ", "")
        cookies[x] = cookies[x].replace(" for />", "")
        cookies[x] = cookies[x].strip()
        if cookies[x].__contains__('="'):
            cookies[x] = cookies[x].split('="')
            cookies[x][1] = cookies[x][1].replace('"', "")
        else: cookies[x].split("=")
        r.cookies.set(cookies[x][0], cookies[x][1], domain = "icloud.com")
        
def ListToCSV(data:list):
    for d in data:
        del d['origin']
        del d['anonymousId']
        del d['domain']
        del d['label']
        del d['note']
        del d['createTimestamp']
        del d['isActive']
        del d['recipientMailId']

    df = pandas.DataFrame(data)
    df.columns = ["Main", "Email"]
    df.to_csv("ICloudEmails.csv", index=False)


if os.path.getsize('cookies.txt') == 0:
    login()
cookies()
MailNow = Emailist()
ListToCSV(MailNow)
tot = len(MailNow)
while(tot != 750):
    if 750 - tot <= 20:
        for x in range(0, 750 - tot):
            result = genmail()
            if result == "ratelimited":
                break
            sleep(5)
    else:
        for x in range(0, 20):
            result = genmail()
            if result == "ratelimited":
                break
            sleep(5)
            
    tot = Emailist()
    now = datetime.datetime.now()
    now = now.time()
    print(now.strftime("%H:%M:%S") +" " + str(tot))
    sleep(1800)

ListToCSV(Emailist())