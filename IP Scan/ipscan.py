import os
import platform
import socket
import threading
import time

import requests
from colored import fg

webhook = ""
show = "_"
class NetscanThread(threading.Thread):
    def __init__(self, address):
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        self.lookup(self.address)

    def lookup(self, address):
        global show
        try:
            hostname, alias, _ = socket.gethostbyaddr(address)
            with open('ip.txt', 'a') as f:
                f.write(f'>> {address} => {hostname}\n')
            self.send(address, hostname)
        except socket.herror:
            if show in ["true", "yes"]:
                with open('ip.txt', 'a') as f:
                    f.write(f'- {address} => None\n')

    def send(self, address, hostname):
        global webhook
        alive = True
        while alive:
            try:
                embed = {
                    "description": f"IP Adress: `{address}`\nHostname: `{hostname}`",
                    "title": 'IP Found!',
                    "color": 0xFF0000,
                }

                data = {
                    "username": "IP Scanner",
                    "embeds": [
                        embed
                        ],
                }
                headers = {
                    "Content-Type": "application/json"
                }
                response = requests.post(webhook, json=data, headers=headers)
                if response.status_code == 429:
                    timeout = int(str(response.json()['retry_after'])[2:])
                    time.sleep(timeout)
                else:
                    alive = False
                    break
            except:
                pass

class Netscan():
    def __init__(self, mode:str="20", show:str="false"):
        self.mode = mode
        self.show = show
        self.addresses = self.addresses()
        self.threads = []
        self.current = 1

    def addresses(self):
        addresses = []
        #########################################
        #try 16-bit	                        #
        #########################################
        if self.mode in ["16", "all", "tens"]:
            for ping in range(256):
                for ping_ in range(256):
                    addresses.append(f"192.168.{ping}.{ping_}")
        #########################################
        #try 20-bit	                        #
        #########################################
        if self.mode in ["20", "all", "twenties"]:
            for ping in range(16, 32):
                for ping_ in range(256):
                    for ping__ in range(256):
                        addresses.append(f"172.{ping}.{ping_}.{ping__}")
        #########################################
        #try 24-bit	                        #
        #########################################
        if self.mode in ["24", "all", "twenties"]:
            for ping in range(256):
                for ping_ in range(256):
                    for ping__ in range(256):
                        addresses.append(f"172.{ping}.{ping_}.{ping__}")
        self.size=int(len(addresses))
        with open('ip.txt', 'w') as f:
            f.write(
                '###########################################################################################\x1f#                                                                                         #\x1f#  IP SCANNER  #\x1f#                                                                                         #\x1f###########################################################################################\x1fIP LIST:\x1f'
            )

        return addresses
            
    def scan(self):
        self.start=time.time()
        netscanthreads = [NetscanThread(address) for address in self.addresses]
        for thread in netscanthreads :
            self.bar(self.current, self.size, str(thread.address))
            thread.start()
            self.threads.append(thread)
            self.current+=1

        for t in self.threads:
            t.join()

        print(f"Took: {time.time()-self.start} seconds!")

        exit_=None
        while exit_ is None:
            exit_ = str(input(f'{fg(15)}[{fg(127)}>{fg(15)}] Exit: '))
                
    def bar(self, current, total, address):
        length = 70
        percent = ("{0:." + str(1) + "f}").format(100 * (current / float(total)))
        filledLength = int(length * current // total)
        bar = f'{fg(44)}■' * filledLength + f'{fg(250)}■' * (length - filledLength)
        Menu().msg_(f" {fg(124)}Don't LEFT CLICK! If you LEFT CLICK or don't see anything: RIGHT CLICK !\n")
        print(f"{fg(10)} IP: {address}\n {fg(255)}{percent}% {fg(238)}|{bar}{fg(238)}| {fg(255)}{current:,d} / {total:,d}")
        
class Menu():
    def __init__(self):
        self.title()
        self.webhooks=['help', '', 'none']
        self.modes=['all', 'twenties', 'tens', '16', '20', '24', 'none', '']
        self.shows=['no', 'yes', 'true', 'false', 'none', '']
        self.sub_menu_colour=13
        self.mode="_"

    def title(self):
        os.system('cls && title IP Scanner' if os.name == 'nt' else 'clear')
        return print(f'''
            {fg(124)}██╗██████╗    ██████╗ █████╗  █████╗ ███╗  ██╗███╗  ██╗███████╗██████╗ 
            {fg(125)}██║██╔══██╗  ██╔════╝██╔══██╗██╔══██╗████╗ ██║████╗ ██║██╔════╝██╔══██╗
            {fg(126)}██║██████╔╝  ╚█████╗ ██║  ╚═╝███████║██╔██╗██║██╔██╗██║█████╗  ██████╔╝
            {fg(127)}██║██╔═══╝    ╚═══██╗██║  ██╗██╔══██║██║╚████║██║╚████║██╔══╝  ██╔══██╗
            {fg(128)}██║██║       ██████╔╝╚█████╔╝██║  ██║██║ ╚███║██║ ╚███║███████╗██║  ██║
            {fg(129)}╚═╝╚═╝       ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚══╝╚══════╝╚═╝  ╚═╝ 
        ''')
        
    def webhook_(self):
        global webhook
        self.msg_(f" {fg(238)}If you need Help just type 'Help'\n")
        while webhook in self.webhooks:
            web = str(input(f'{fg(15)}[{fg(127)}>{fg(15)}] Webhook: '))
            if web.lower()=='help':
                print(f'''
{fg(129)}Local Network IP Scanner - Webhook
{fg(124)}A Discord Webhook        
                ''')
            else:
                uname = platform.uname()
                embed = {
                    "description": f"System: `{uname.system}`\nNode Name: `{uname.node}`\nRelease: `{uname.release}`\nVersion: `{uname.version}`\nMachine: `{uname.machine}`\nProcessor: `{uname.processor}`",
                    "title": "IP Scanner Webhook Test",
                    "color": 0x008000
                    }
                data = {
                    "username": "IP Scanner",
                    "embeds": [
                        embed
                        ],
                }
                headers = {
                    "Content-Type": "application/json"
                }
                try:
                    result = requests.post(web, json=data, headers=headers)
                    if 200 <= result.status_code < 300:
                        webhook=web
                except:
                    webhook=''
                    self.msg_(f" {fg(238)}INVALID WEBHOOK\n")
                
    def mode_(self):
        self.title()
        self.msg_(f" {fg(238)}If you need Help just type 'Help'")
        print(f'''
{fg(self.sub_menu_colour)} Modes:
    • all
    • twenties
    • tens
    • 16
    • 20
    • 24
        ''')
        while self.mode not in self.modes:
            self.mode = str(input(f'{fg(15)}[{fg(127)}>{fg(15)}] Mode: ').lower())
            if self.mode=='help':
                print(f'''
{fg(129)}Local Network IP Scanner - Mode
{fg(124)}Ip:
    {fg(200)}• 16-bit block    [192.168.0.0 – 192.168.255.255]
    • 20-bit block    [172.16.0.0 – 172.31.255.255]
    • 24-bit block    [10.0.0.0 – 10.255.255.255]
                
{fg(124)}Mode:
    {fg(200)}• all 	   -> all ip addresses will be pinged.               [17 891 328 IP]
    • twenties 	   -> 20-bit and 24-bit ip addresses will be pinged. [17 825 792 IP]
    • tens 	   -> 16-bit and 20-bit ip addresses will be pinged. [1 114 112 IP]
    • 16 	   -> 16-bit ip addresses will be pinged.            [65 536 IP]
    • 20 	   -> 20-bit ip addresses will be pinged.            [1 048 576 IP]
    • 24 	   -> 24-bit ip addresses will be pinged.            [16 777 216 IP]
    -> Default: '20'
            ''')

    def show_(self):
        global show
        self.title()
        self.msg_(f" {fg(238)}If you need Help just type 'Help'")
        print(f'''
{fg(self.sub_menu_colour)} Show Unknown IP ? {fg(124)}[THIS CAN SLOW DOWN THE PROGRAM!]
{fg(self.sub_menu_colour)}    • Yes
    • No
        ''')
        while show not in self.shows:
            show = str(input(f'{fg(15)}[{fg(127)}>{fg(15)}] Show: ').lower())
            if show=='help':
                print(f'''
{fg(129)}Local Network IP Scanner - Show
{fg(124)}Show IP which didn't answer to the ping in the log File ?:
    {fg(200)}• Yes
    • No
    -> Default: 'no'
                ''')
        if show in ["", "none"]:
            show='false'

    def msg_(self, msg):
        print(msg)

    def start(self):
        self.webhook_()
        self.mode_()
        self.show_()
        mode = '20' if self.mode in ["", "none"] else self.mode
        self.title()
        self.msg_(f" {fg(238)}Launching Scan...")
        Netscan(mode=mode, show=show).scan()

Menu().start()
