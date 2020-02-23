import time as t
from datetime import datetime as dt

s=dt.now().weekday()
weblist=['www.youtube.com','youtube.com','www.facebook.com','facebook.com','www.instagram.com','instagram.com']
hostpath=r'/etc/hosts'
hosttmp=r'hosts'
redirect='127.0.0.1'
y = dt.now().year
m = dt.now().month
d = dt.now().day

while True:
    if (s==5 or s==6 or dt(y,m,d,8) < dt.now() < dt(y,m,d,1)):
        with open(hostpath,'r+') as f:
            content=f.read()
            print(content)
            for web in weblist:
                if web not in content:
                    f.write(redirect+' '+web+'\n')
    else :
        with open(hostpath,'r+') as f:
            lines=f.readlines()
            f.seek(0)
            for l in lines:
                if not any(web in l for web in weblist):
                    f.write(l)
                f.truncate()
        break