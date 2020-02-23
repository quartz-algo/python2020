#DATA-SECURITY ASSIGNMENT To block user entered websites on all weekdays from 8am to 4.30pm
#change the permission of host file to use this code
import time as t
from datetime import datetime as dt

s=dt.now().weekday()
weblist=[]
hostpath=r'/etc/hosts'
#hosttmp=r'hosts'
redirect='127.0.0.1'
y = dt.now().year
m = dt.now().month
d = dt.now().day

while True:
    w = input("Enter the website you want blocked (as website_name.com)::")
    weblist.append(('www.'+w))
    weblist.append(w)
    c = input("Anymore? (y/n)::")
    if c=='y' or c=='Y':
        pass
    else:
        break

print(s)

print("\tThe following websites will be blocked from 8:00 to 16:30 (except on Sat/Sun) ::\n")
while True:
    if (s!=5 and s!=6 and dt(y,m,d,8) < dt.now() < dt(y,m,d,16,30)):
        with open(hostpath,'r+') as f:
            content=f.read()
            for web in weblist:
                if web not in content:
                    f.write(redirect+' '+web+'\n')
                    print(web)
    else :
        with open(hostpath,'r+') as f:
            lines=f.readlines()
            f.seek(0)
            for l in lines:
                if not any(web in l for web in weblist):
                    f.write(l)
                f.truncate()
        break