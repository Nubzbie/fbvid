#Coded by Nubzbie
# -*- coding: utf-8 -*-

import sys
import os
import re
import requests as r
import wget

t = '\x1b[0m'
m = '\x1b[1;91m'
p = '\x1b[1;97m'
garis_dw = '\x1b[2K'

os.system('clear')
print ("""{}
    ________        _    ___     __         
   / ____/ /_      | |  / (_)___/ /__  ____ 
  / /_  / __ \_____| | / / / __  / _ \/ __ \
{}                 / __/ / /_/ /_____/ |/ / / /_/ /  __/ /_/ /
/_/   /_.___/      |___/_/\__,_/\___/\____/ 
                                            
Author : Nubzbie

1. Download dengan resolusi Normal
2. Download dengan resolusi Tinggi
{}""".format(m,p,t))
pilih = input("Masukkan nomor : ")

if pilih == "1":
    try:
        LINK = input("[?]Link video : ")
        html = r.get(LINK)
        sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
    except r.ConnectionError as e:
        print("Cek koneksi anda")
    except r.RequestException as e:
        print("Invalid link")
    except (KeyboardInterrupt, SystemExit):
        print("Dibatalkan")
        sys.exit(1)
    except TypeError:
        print("Private video")
    else:
        sd_url = sdvideo_url.replace('sd_src:"', '')
        print("\n")
        print("Kualitas Normal: " + sd_url)
        filemu = raw_input('(Ex: /sdcard/namapenyimpanan : ')
        print("[+] Download start")
        wget.download(sd_url, filemu)
        sys.stdout.write(garis_dw)
        print("\n")
        print("Finish Download")

elif pilih == "2":
    try:
        LINK = input("[?]Link video : ")
        html = r.get(LINK)
        sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
    except r.ConnectionError as e:
        print("Cek koneksi anda")
    except r.RequestException as e:
        print("Invalid link")
    except (KeyboardInterrupt, SystemExit):
        print("Dibatalkan")
        sys.exit(1)
    except TypeError:
        print("Private video")
    else:
        sd_url = sdvideo_url.replace('hd_src:"', '')
        print("\n")
        print("Kualitas HD: " + sd_url)
        filemu = raw_input('(Ex: /sdcard/namapenyimpanan : ')
        print("[+] Download start")
        wget.download(sd_url, filemu)
        sys.stdout.write(garis_dw)
        print("\n")
        print("Finish Download")

else:
    print("[]!]Silahkan pilih kakak")
