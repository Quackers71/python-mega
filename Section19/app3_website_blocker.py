import time
from datetime import datetime as dt

hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.purple.com","purple.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,16) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("Working hours...")
    else:
        print("Fun hours...")
        time.sleep(5)