import requests


url = "http://127.0.0.1:8000/8/solution/"
loginUrl = "http://127.0.0.1:8000/user/login/"

isBugFree = False

for i in range(1):
    with open('testCode.py', 'r') as file:
        data = file.read()


    code = data
    PARAMETERS = {
        'playerSolution': code
    }
    r = requests.post(url,  headers={'Authorization': 'Token daf2b921df8ae6ffd59c1c51dc716681e28b086e'}, data=PARAMETERS)

    print(r.text)