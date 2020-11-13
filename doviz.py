import requests
import threading
import time
from bs4 import BeautifulSoup

class Doviz:
    goldhook = ""
    eurohook = ""
    dollarhook = ""
    
    @classmethod
    def dollar(cmd):
        r = requests.get('https://bloomberght.com/')
        soup = BeautifulSoup(r.content, 'html.parser')
        veri = soup.find_all('small',attrs={'class':'value LastPrice'})
        dolar= veri[1].text

        return dolar
    
    @classmethod
    def euro(cmd):
        r = requests.get('https://bloomberght.com/')
        soup = BeautifulSoup(r.content, 'html.parser')
        veri = soup.find_all('small',attrs={'class':'value LastPrice'})
        euro = veri[2].text

        return euro

    @classmethod
    def gold(cmd):
        r = requests.get('https://bloomberght.com/')
        soup = BeautifulSoup(r.content, 'html.parser')
        veri = soup.find_all('small',attrs={'class':'value LastPrice'})
        gold = veri[5].text

        return gold

    @classmethod
    def log(cmd,message,hookk):
        response = True

        r = requests.post(hookk,data={
            'content':message
        })

        if str(r) != '<Response [204]>':
            response = False

        return response


def dolar():
    temp = 0
    while True:
        kur = Doviz.dollar()
        kur = kur.replace(',','.')
        kur  = float(kur)
        if temp >kur:
            mesaj = f'🔴 Güncel Dolar Fiyatı {kur:.4f} ・ {temp-kur:.5f} kadar düşüşte '
        elif temp == kur:
            mesaj = f'🟡 Güncel Dolar Fiyatı {kur:.4f} ・ Aynı fiyatta '
        else:
            mesaj = f'🟢 Güncel Dolar Fiyatı {kur:.4f} ・ {kur-temp:.5f} kadar yükselişte '
        temp = float(f'{kur:.4f}')

        Doviz.log(mesaj,Doviz.dollarhook)

        time.sleep(60)

def euro():
    temp = 0
    while True:
        kur = Doviz.euro()
        kur = kur.replace(',','.')
        kur  = float(kur)
        if temp >kur:
            mesaj = f'🔴 Güncel Euro Fiyatı {kur:.4f} ・ {temp-kur:.5f} kadar düşüşte '
        elif temp == kur:
            mesaj = f'🟡 Güncel Euro Fiyatı {kur:.4f} ・ Aynı fiyatta '
        else:
            mesaj = f'🟢 Güncel Euro Fiyatı {kur:.4f} ・ {kur-temp:.5f} kadar yükselişte '
        temp = float(f'{kur:.4f}')
        
        Doviz.log(mesaj,Doviz.eurohook)

        time.sleep(60)

def altin():
    temp = 0
    while True:
        kur = Doviz.gold()
        kur = kur.replace('.','').replace(',','.')
        kur  = float(kur)
        if temp >kur:
            mesaj = f'🔴 Güncel Altın/Ons Fiyatı {kur:.2f} ・ {temp-kur:.4f} kadar düşüşte '
        elif temp == kur:
            mesaj = f'🟡 Güncel Altın/Ons {kur:.2f} ・ Aynı fiyatta '
        else:
            mesaj = f'🟢 Güncel Altın/Ons {kur:.2f} ・ {kur-temp:.4f} kadar yükselişte '
        temp = f'{kur:.2f}'

        Doviz.log(mesaj,Doviz.goldhook)

        time.sleep(60)

z = threading.Thread(target=altin, args=())
z.start()

x = threading.Thread(target=euro, args=())
x.start()

y = threading.Thread(target=dolar, args=())
y.start()
