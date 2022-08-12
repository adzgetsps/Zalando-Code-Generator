import requests
import json
import random, string
from pyfiglet import Figlet
from colorama import Fore

catchall = ('[@catchall.com]')
amount = int(input('How many Codes do you want?\n'))

def random_char(y):
            return ''.join(random.choice(string.ascii_letters) for x in range(y))

for i in range(amount):
      i = 0
while i < amount:  
    email = (random_char(5) + catchall)   
    url = "https://www.zalando.co.uk/api/graphql/"
    payload = json.dumps([
      {
        "id": "f321f59294a4ffd369951dc5d8f92b801cb7c3c7302de9e5118b3569416c844f",
        "variables": {
          "input": {
            "email": email,
            "preference": {
              "category": "MEN",
              "topics": [
                {
                  "id": "recommendations",
                  "isEnabled": True
                },
                {
                  "id": "item_alerts",
                  "isEnabled": True
                },
                {
                  "id": "fashion_fix",
                  "isEnabled": True
                },
                {
                  "id": "follow_brand",
                  "isEnabled": True
                },
                {
                  "id": "subscription_confirmations",
                  "isEnabled": True
                },
                {
                  "id": "offers_sales",
                  "isEnabled": True
                },
                {
                  "id": "survey",
                  "isEnabled": True
                }
              ]
            },
            "referrer": "nl_subscription_page",
            "clientMutationId": "1657967595139"
          }
        }
      }
    ])
    headers = {
      'authority': 'www.zalando.co.uk',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/json',
      'cookie': 'frsx=AAAAAE0Z_Hr15lwMolei9JdbRIhx7-ciGyuqe-h40zxxnd5Xz1MgDzB0Kq0nie4oxIcc5l-wrMpUNaIBo6COlgDh_EYtoo2biWHvCMpE3dHq2MewnTi_iXv-vXSaPIwHrQnJ9DJU6vC0p7JYXPK-aA==; Zalando-Client-Id=bf366852-1d40-4664-a075-a78bf7914fe1; mpulseinject=false; bm_sz=094627AC6268CE8C08E78E6A7FE01196~YAAQqFozuGK4//yBAQAAsGSRBhA2AuTiHl6sGnXH8XwuGqNmU1McZiQeKFSxP/wT0jVkjFdG2RlXbCZ8YtCJe3t9iwGA+oaEj/IQejWvjdcNrI3R1m5LL1eLWdJj0AIG3dggIi9MTtojz5zoUSdn5JUWa4LgDH5uzJUQJK82+qoWVZSr3MkzFLGWQrxTBgCGjd3JawEHrEqdZ5sIrjPbA0zm6HBxjfBC7yly/4kDa5xEdR8FkRAJlxp2hligAzmXeNPjLqF/C3zcIMY3/8HlAVU2tp+RhH/0+qKLD8h77iKqaUi8dJarM+kr2hu/3s7mNtnRFeUEAynGM7TSwnKc3GSxYaPeztdlzFh3dGV1WN/P+14b/skyyfz/xPCV96SUGjZiN++dkAq6mdxS+O8sFt8q~4468806~3619123; ak_bmsc=23421B8605A0037D1E76DE64424612E0~000000000000000000000000000000~YAAQqFozuPS4//yBAQAAr2iRBhDxWJubUOZA8rPm3nI1m0xF3gcoLR4Jjg5IefGsyFkpR38E9LN7PYNzNPa75EyHEaCW0m7D3TaThsQCyqG9id/hsCJHJ8PI3eUiEW1ITZRJdXaKE1tQUgBqv7PG15ki7LXaUt9jWUWFK57Yt8pW08BJXBC/ssPiu2BveloME031MVWpyd4KFFBdhQEdMibVAccr2H7XFOGf47C4A6v5H9VFH3vUxtlVpqJ+Qic+Lp39Swi7dFftSUmZU4RQlZ4f8X2f+V0IIhcCvxpCkhuLQIrPCwdjK6ebBYILk4fCUbW0A1r8tnHzOSz28bOs2SnicSq9tNcYFSNEcx+vJnFgKIFCgSNXHvtxyGlmiW7+t9VA7G4nZt388oVfLTV2hceHN/P2adxqLCKUG4j5cfqwfJeTjvortEJ8BcmWwxYM1mcqnbhT00PntNZCOt8BgWezXXEVWB8NJfLMhG1A6r6Cjm1slwasbVq4t8g9; _gcl_au=1.1.954718820.1657967572; sqt_cap=1657967568154; _ga=GA1.3.1514171283.1657967572; _gid=GA1.3.1583449661.1657967572; _gat_zalga=1; _abck=1BA76FDA00ABC9C28902F0F0B162E845~-1~YAAQqFozuGfF//yBAQAADcCRBgjTmVpwEB3FVtdZO4Mfduirc1EY8JhEDRPGG9gBEBoSBPRRWjhZtsXIipT79lY9iF3ZFYhZJWuG26s8aq4qqnGI9d8nv5fkVbPs7NKpQ+DdZRjrvU1efMCCyabiP7CBp6Z0LrX6mD0FYL9cJ/mRynulDI8f3Mavz4ZDTJDAIKGvIserTvVDZuqH9KUYo5YS318TZXGZoryh5o/92yN5NkEU/kAbjMgaKmgHeuR1AqUhCnx++gzfRPeFDwqm8ApKYoTdNT3Qhr61woGi7C6dxs77j+i7E0B9UNUoqCqTUIBLCPzgusl8NZ7/GzDlFyw6n1STJjfTac1v9YooZ/S93k7t4JPjoZ1mE27idwFRx4uM6zfmQYzrtWIkmAVgaOlxMM5Q7OpFWW3zT2JulAuE/NCgiY86UsLjEDsNOaU1PaFClGRIZXnER1SIk4Bo2psJiQOa3zJiuBD0rijv5BXYmlSfCMawKNBeNqt6yCfv+SmZjhpy+XbJalJ0VoE=~-1~-1~-1; bm_sv=20C43C8B27E95A2F93592D4528655108~YAAQqFozuHLF//yBAQAAT8CRBhDkBIQfGYM05vmeM2MeWz4RwX3ZKJmG+8SBftayJgaSTccm90zs8Q0SmCXcPSZ7HgIk/QQ+Xu/58ZXSkKMdcMBaEEh7eoLM4kVXvW6D+9v+aj8HMGh5Td2Z4+qRXvBBw580Azt3t3lZQJHL3xKZfjpagbD5BdZ91PAifkiUHljTeMKAv4ry/WKw48OYrWpnJ/hwzAmGxQ08LrdjeRQbhlyp71YDT0n5U8oe45KFSIBSjA==~1',
      'dpr': '1.25',
      'origin': 'https://www.zalando.co.uk',
      'referer': 'https://www.zalando.co.uk/zalando-newsletter/',
      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'viewport-width': '982',
      'x-xsrf-token': 'AAAAAE0Z_Hr15lwMolei9JdbRIhx7-ciGyuqe-h40zxxnd5Xz1MgDzB0Kq0nie4oxIcc5l-wrMpUNaIBo6COlgDh_EYtoo2biWHvCMpE3dHq2MewnTi_iXv-vXSaPIwHrQnJ9DJU6vC0p7JYXPK-aA==',
      'x-zalando-experiments': 'b891eec6-b3d5-4760-b685-fe1fbe3ce330=THE_LABEL_IS_ENABLED;07fb3627-d56d-4909-954d-d58607a2abd6=AD_PROXY_CATALOG_ENTITIES;90aa955b-d7f6-4fe1-a14f-2522788af1bb=fdbe-release1-disabled;b951ad11-ec05-4c78-9772-1eb1100c5c96=ABB_DISABLED;cb304bd0-53f9-4d2c-9817-3fdd9e388aaa=sephora_garden_disabled;163908b6-4ba9-4442-981f-b340d4b4e9fe=experience_theme_disabled;e807ff13-5638-4b31-ad55-92c5d41fd3ba=experience_full_disabled',
      'x-zalando-intent-context': 'navigationTargetGroup=ALL',
      'x-zalando-request-uri': '/zalando-newsletter/'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    i += 1
    print(Fore.GREEN + '[ZalandoGen] Generated ' + (str(i)) + ' / ' + (str(amount)))
  

    if i == amount:
            print(Fore.BLUE + '[ZalandoGen] Codes Finished Genning, Check Email')
    else:
        pass
    


