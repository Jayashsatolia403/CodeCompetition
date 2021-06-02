import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


import requests
import secrets
import string

url = "http://127.0.0.1:8000/user/register/"
loginUrl = "http://127.0.0.1:8000/user/login/"

isBugFree = False

for i in range(1000):
    N = 20
    res = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(N))

    PARAMETERS = {
        'username': "{}".format(res),
        'email': "user@{}.com".format(res),
        'password': "Jayash@403",
        'password2': "Jayash@403"
    }


    r = requests.post(url, PARAMETERS)

    LOGINPARAMETERS = {
        'username': "{}".format(res),
        'password': "Jayash@403"
    }

    r = requests.post(loginUrl, PARAMETERS)


    if not str(r.text).startswith('{"token"'):
        isBugFree = True
        print(r.text)

if isBugFree:
    print("Passed All Test Cases!")