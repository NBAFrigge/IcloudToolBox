import pandas
from seleniumbase import Driver
from time import sleep
import requests
import warnings 
warnings.filterwarnings(action='ignore', category=DeprecationWarning)
import os
import datetime

r = requests.session()
driver = Driver(wire=True)

def login():
    driver.get("https://www.icloud.com/?s=Iseo")
    sleep(2)
    input("Press Enter after the login \n")

    for cookie in driver.get_cookies():
            c = {cookie['name']: cookie['value']}
            r.cookies.update(c)
    for req in driver.requests:
        if "clientBuildNumber" in req.url and "clientMasteringNumber" in req.url and "clientId" in req.url and "dsid" in req.url:
            params = req.params
            break
    f = open("cookies.txt", "w")
    f.write(str(r.cookies))
    f.close()
    driver.close()
    return params

def Emailist(params:dict):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Accept': '*/*',
        'Accept-Language': 'it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'text/plain',
        'Origin': 'https://www.icloud.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.icloud.com/',
        # 'Cookie': 'X_APPLE_WEB_KB-N-X6N6YENQGHN9K21GZFFZB2WFM="v=1:t=AQ==BST_IAAAAAAABLwIAAAAAGXnFucRDmdzLmljbG91ZC5hdXRovQBgNVSRroEF8MKFxZjIYTNJzQW67HUj3ChTRmLYlUsK1SyRV2kvecLuTIE2xdNjlu8WPaKjoidVJLYPcyHChEn-rx-ywEwAmIsWfN-kP9nFuqYGIaXBkHwI_Vzk3isYs9kPoSSsx4T7RPgm6JZSsdyEnpeO2Q~~"; X-APPLE-WEBAUTH-HSA-TRUST="8292fe6845bebf11217ffe6fc478a3b2a21b9cea7cea2f9465951c3d12c797e8_HSARMTKNSRVXWFlaqn0WcEo0xbiR/H29cieugk1kz3RyCXot6IFteTpWKmaOlsLiBSe/S9ae3ns7j7qaAjeNerVk1QHf9WmnalRJPttP1cYXJv63nko8aZRE/XUZyTgK5mjD15Hr0ReTQFDEwPeVRFCI0yOxJXUwI8Ay0D5R2GYb3z8iOCdDamKBtrLeJPd3mYwhGFco+UnDnJuGVInkqATpGPC1omHTXMBL4siUSRVX"; X-APPLE-WEBAUTH-PCS-Documents="TGlzdEFwcGw6MTpBcHBsOjE6AejREwcalVBdvyeVN90yJLK6bbzXW+PifEvL4GjZv75P/EYiAiJrJpNYfwz6a1JuoWqP3uEg2DfMMvvikLTkKcPHjRS2zsvGsiFg/nfk0hJVba0f/FsHabR/1Ht/B0wzXeDumTD7XeW3MvUFJa7Z7ZAGbeptnhW+518JWUW9CJlOB6pvStFnwQ=="; X-APPLE-WEBAUTH-PCS-Photos="TGlzdEFwcGw6MTpBcHBsOjE6AcoYhz1cIb81FR4oOudy1QwAkIJn81GRmGC1Vaqlz4tHkf2971XziiyF/rwlvL5VzT6hyxe+m/Y2lRJSKS1J/pC+L1Bi8y1EMJoGcnceoe+4tHu3Tjw5RuS6f7C8jWcfidAjDirLK7SwMpfpE+oPXKWjkTw3UXUQp75Q1j/xkG7XsG3do8CY9A=="; X-APPLE-WEBAUTH-PCS-Cloudkit="TGlzdEFwcGw6MTpBcHBsOjE6AVYhCMGIoWrsqyoAQNGTwu/MALTkcsqS01/YrLAKNlC5BHvTB0mew817YVh4HlCmbmz+jGn84SVfeTvSbi0KYijX3OO7oKEv85XDhraIDwLKMgzQfSUy34qmju+kqX/8cOD/9t2nBrGwQ4F9u/t2z9nxzTujv/1M53l1vLchv4LyrhF2YK9TZQ=="; X-APPLE-WEBAUTH-PCS-Safari="TGlzdEFwcGw6MTpBcHBsOjE6AeSaQKC0Zr2SIBKiqiTVMznOdJ/Otxz7vxfyDM9XLTwyIzd3+Ok4mzSH5RdKpvxnR7Lw/kV7pMGa61PETVcSlHCL/X4w1Kgf82ltoOPHkiOqltRHvI1zh1oF/F5Cyde2j9j4fuaKOazCw2OewIiqZy7lAD0+U3x44hQkqplUYuUd4rRfP5zP1g=="; X-APPLE-WEBAUTH-PCS-Mail="TGlzdEFwcGw6MTpBcHBsOjE6ASM5MVBkMgEqNUF3/Kxmdj2NE9dUxy58dfUZ2TnB9J88S0cuhUJR0etnIXr38FUXaDOts5bzdlDemoLv6cldj0o9GBBaqhztGrBOVPMwMLMMBqgMyhmsD4zo0ct2CNhK927PXjpJW9TEw3QLMarmsttRK5Souom6M1VOr6aO7U4TziHANiiQ2A=="; X-APPLE-WEBAUTH-PCS-Notes="TGlzdEFwcGw6MTpBcHBsOjE6AXfMpU77JE3p3s+OOxkQwkxAOHatRBZaHpQCNhRZncvGsPek5tIL95j7CgXf2MMbg28HSXqUgJ9OH9NDKiIxmvXSu6aUzV7p5warVIZw8O0voX1+292Wz6aNOHdKLk8sR1BHx3kpEh4ZAPTA+G4fkPilQtf6+6glEm1ZcUiM2tldpGgMeP2vkw=="; X-APPLE-WEBAUTH-PCS-News="TGlzdEFwcGw6MTpBcHBsOjE6AaSVjJZcR/Dr6o4cdrB1SGbKK3j+ktSX9OjOtv4IrXXxEuAVhbV2c0AADwSpznKV7XJ4KNbePQV2LhM1AOHXOZYt2g9zBXXJ3Vr1yZmbr5KKR3hkbVHVe2DGTfyoXBgMqtmchqlzzM8r0TBaFDPhuzIn9Ga6pcKw7Ganqary8cEDxz/ZQWTfSA=="; X-APPLE-WEBAUTH-PCS-Sharing="TGlzdEFwcGw6MTpBcHBsOjE6ATyuYpQcy6j80RuocvgST4/Ser6nXguP258daEV1mN7BkpCjFsKYcm/gGuSmRMa8nomJP15WI5+swRILfOpVsYMVzaqCenb/cqjkepKBiaEKxJy7Rk0LgKKaF4AOomYScKbQ+NYHk/ifIwaa0NxIZA3NtSL+IqM2pMesZuXEeHzdwR8nWDRyiQ=="; X-APPLE-UNIQUE-CLIENT-ID="Ag=="; X-APPLE-WEBAUTH-LOGIN="v=1:t=Ag==BST_IAAAAAAABLwIAAAAAGXnS6ERDmdzLmljbG91ZC5hdXRovQA1PfWvzWNVnuPyVfZpGeW4AAxiU7wDLcewEdRXU0jsDJ5RWE9IZJ0hGPpHcL2Ywn1PQ1TDfv043pYTe_4tWwIRiJ26QBgh5_Sb3qPs5CRUbeePGBW3ypNYJBXlLAt7EzAikQLOjdZhTjQgC8ymxzKH8H_LGw~~"; X-APPLE-WEBAUTH-VALIDATE="v=1:t=Ag==BST_IAAAAAAABLwIAAAAAGXnVskRDmdzLmljbG91ZC5hdXRovQA-BgoJ-CJzRKnC_I5T5tuiJwkqfm4NlvZF-Ts6SS38jzDNpToEEPDNkrLawTh1J9OYBpUAh5rUk6VAeo4kyQfBEeTlYGS5qe56uU4iM58ddIFI6s-2usSpVaAFSvkQt7HbqTZENlKksyszznyKknYmn5zyag~~"; X-APPLE-WEBAUTH-TOKEN="v=2:t=Ag==BST_IAAAAAAABLwIAAAAAGXnVs4RDmdzLmljbG91ZC5hdXRovQDs-wrC5FWaz8UIMgiuuV8JaUPsfMStBtA9AZCPBuTa5MzBRSYq6jnyGCXtHA0WRt18Hfz6dv0EQbxCig4yDPbEpp3sOXXX6SNAXvUtKTE3T2CaEG4NhF_wT--ELbf9idPnOX71iaB4mXXhNjP05NxJMBR_fw~~"; X-APPLE-WEBAUTH-USER="v=1:s=1:d=10292339061"; X-APPLE-DS-WEB-SESSION-TOKEN="AQEv29Jw1SGcynOTz6XpY3hRh4EJruccRHj4XjcV6sgb/7S6oTOG/7+OAqv8lAxS6G+Erh6alPpI3MY8YvCIIYwIp8tyyqWPBsiD0vPUqL6+3o6wNk8wBa+ycurRbGFqxmLx06tpqNlEyUEpIsjUSOxPlLP5Zns/eR5kV1x0bvZlRM+KcaJRnmSJz+C01+DourbyOPuAOcdfdM8wqE9CLUx94UM0NzrBZffcGeRAK22Ld5KvRLlqDdxhitfRXdqLHesEJC65V/qEyxjatgBV/2S27DhwrprW7+VJrBOc3o0u9vLzkVBrQSQcpTmuBrKJLLqIbhCxwN9hLWEydCW8cSsgOPY3oLVWOg+YGeeXDHhP4KzxF2Zes3v1nbqesMlCxut8YxfqTwVnUbm9VLhLGG8wrRGh9mzXmtzpBVjAvPepDuZ44dnXXetKCu4kThovp6M1MESex0UY4pDV5/ELosW8hhocGMfdYxUHRjxlB50bUwJ+UyVTyVhN+a4mHbagKZhM8m0f0NI/D7yFRMEPp9dqC7cIVRPmvy2HVHWjvo4aGHBbf2wwJuiLigB1QEAJVJaD5eJbOPfal/gJAi7zMXVHEwSF1LQnCHBqVtsE5E8Ja5d2ovnmEuoSkSOnloWe/Ai8qirBQN6+xKKniKALFZyfoixLcMzv0h1uQCD8v6RdPeQrh7h54C6XM0idVKe7gFfZejr1xnA/ts09iOMWLbNcjpQhvRdO/NthaoLXJa182XUQAVqRV3QfjOZ8EtrkJ7vyxcvDNwFyquVobTq8nbuf+v04pxXl1Pd4FQ=="; X-APPLE-WEB-ID=9178A1A3A0AB62BFE9B6D5A372E4878E377CE729',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    response = r.get('https://p49-maildomainws.icloud.com/v2/hme/list', params=params, headers=headers)
    ListToCSV(response.json()["result"]["hmeEmails"])
    print("Emails list saved in ICloudEmails.csv")

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

def genmail(params:dict):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': '*/*',
        'Accept-Language': 'it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'text/plain',
        'Origin': 'https://www.icloud.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.icloud.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    data = '{"langCode":"it-it"}'

    response = r.post('https://p49-maildomainws.icloud.com/v1/hme/generate',params=params, headers=headers,data=data,)
    if response.json()["success"] == True:
        
        data = '{"hme":"'+ response.json()["result"]["hme"] +'","label":"Generated","note":""}'

        response = r.post('https://p49-maildomainws.icloud.com/v1/hme/reserve',params=params,headers=headers,data=data,)
        if response.json()["success"] == True:
            print(response.json()["result"]["hme"]["hme"] + " : Email Successfully created!")
            return True
    else:
        if response.json()["error"]["errorCode"] == -41012:
            print("Max reached")
            return False


if __name__ == "__main__":
    while True:
        print("Welcome to ICloud Email Generator")
        print("1. Generate Email")
        print("2. Get Emails List")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            cookies()
            params = login()
            print("How many mails do you want to generate?")
            n = int(input())
            for x in range(0, n):
                Max = genmail(params)
                if not Max:
                    break
                sleep(1)
        elif choice == "2":
            cookies()
            params = login()
            Emailist(params)
        elif choice == "3":
            exit()
        else:
            print("Invalid choice")