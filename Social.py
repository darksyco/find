import json
import requests
import time
import os
from sys import stderr




Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper





@is_option
def TrackLu():
    try:
        username = input(f"\n {Ye}Enter Username : >>> {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"}
           ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Username not found {Ye}!")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Gr}+ {Wh}] {site} : {Gr}{url}")
        
        
        
        
        
options = [
    {
        'num': 1,
        'text': 'Username Tracker',
        'func': TrackLu
    },
     {
        'num': 0,
        'text': 'Exit',
        'func': exit
    }
] 
    
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # BANNER TOOLS
    clear()
    stderr.writelines(f"""{Blu}
      
██████╗    █████╗   ██████╗   ██╗  ██╗       ██████╗  ██╗  ██╗   █████╗    █████╗ 
██╔══██╗  ██╔══██╗  ██╔══██╗  ██║  ██╔╝     ██╔════╝  ╚██╗ ██╔╝  ██╔══██╗  ██╔══██╗
██║  ██║  ███████║  ██████╔╝  █████═╝       ╚█████╗    ╚████╔╝   ██║  ╚═╝  ██║  ██║
██║  ██║  ██╔══██║  ██╔══██╗  ██╔═██╗        ╚═══██╗    ╚██╔╝    ██║  ██╗  ██║  ██║
██████╔╝  ██║  ██║  ██║  ██║  ██║ ╚██╗      ██████╔╝     ██║     ╚█████╔╝  ╚█████╔╝
╚═════╝   ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝      ╚═════╝      ╚═╝      ╚════╝    ╚════╝
     
                            
              {Blu}[ - ]  C O D E   B Y  D A R K               [ - ]
              {Blu}[ - ]  GITHUB > github.com/darksyco         [ - ]
              {Blu}[ - ]  WHATSAPP GROUP > shorturl.at/bzIWY   [ - ]

    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Blu}
   
   
███████╗ ██╗ ███╗  ██╗ ██████╗
██╔════  ██║ ████╗ ██║ ██╔══██╗      {Blu}--------------------------------
█████╗   ██║ ██╔██╗██║ ██║  ██║      {Blu}| {Gr}DARK - TRACKER - FIND ADDRESS {Blu}|
██╔══    ██║ ██║╚████║ ██║  ██║      {Blu}|          {Gr}@DARK    {Blu}|
██║      ██║ ██║ ╚███║ ██████╔╝      {Blu}--------------------------------
╚═╝      ╚═╝ ╚═╝  ╚══╝ ╚═════╝               
           ██╗  ███╗  ██╗  ███████╗   █████╗
           ██║  ████╗ ██║  ██╔════╝  ██╔══██╗
           ██║  ██╔██╗██║  █████╗    ██║  ██║
           ██║  ██║╚████║  ██╔══╝    ██║  ██║
           ██║  ██║ ╚███║  ██║       ╚█████╔╝
           ╚═╝  ╚═╝  ╚══╝  ╚═╝        ╚════╝

        
        
        
       

        """)
    time.sleep(0.5)


def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Gr}Select Option :>>> {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()
    
    
