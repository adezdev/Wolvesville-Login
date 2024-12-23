import os
from datetime import datetime
import pytz
import requests
import time
from colorama import init, Fore, Style

init()

def getTime():
    return datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%H:%M:%S')

def getUtcTime():
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

red = Style.BRIGHT + Fore.RED
green = Style.BRIGHT + Fore.GREEN
yellow = Style.BRIGHT + Fore.YELLOW
magenta = Style.BRIGHT + Fore.MAGENTA

class Login:
    def __init__(self, key):
        self.session = requests.Session()
        self.key = key
        self.jwtToken = None
        self.idToken = None
        
    def turnstile(self):
        params = {
            "key": self.key,
            "method": "turnstile",
            "pageurl": "https://www.wolvesville.com/",
            "sitekey": "0x4AAAAAAATLZS5RyqlMGxsL",
            "json": "1"
        }
        response = requests.post('https://api.sctg.xyz/in.php', data=params)
        if response.status_code != 200:
            print(f"{red}Error: {response.status_code}")
            print(response.text)
            exit()

        result = response.json()
        if result.get("status") != 1:
            print(f"{red}API Error:", result)
            exit()

        taskId = result["request"]
        print(f"{green}Task ID:", taskId)

        while True:
            url = f"https://api.sctg.xyz/res.php?key={self.key}&id={taskId}&json=1"
            checkResponse = requests.get(url)
            
            if checkResponse.status_code != 200:
                print(f"{red}Check Error:", checkResponse.status_code)
                print(checkResponse.text)
                break

            checkResult = checkResponse.json()
            if checkResult.get("status") == 1:
                self.turnstileToken = checkResult["request"]
                print(f"{magenta}[{getTime()}] {red}➩ {green}Bypass Turnstile Done!", end='\r')
                break
            elif checkResult.get("status") == 0:
                print(f"{magenta}[{getTime()}] {red}➩ {yellow}Bypassing Turnstile", end='\r')
                time.sleep(1)
            else:
                print(f"{red}Error:", checkResult)
                break
                
    def getToken(self):
        headers = {
            "origin": "https://www.wolvesville.com",
            "referer": "https://www.wolvesville.com/",
            "user-agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
            "Content-Type": "application/json"
        }
        payload = {
            "token": self.turnstileToken,
            "siteKey": "0x4AAAAAAATLZS5RyqlMGxsL"
        }
        res = self.session.post(
            'https://auth.api-wolvesville.com/cloudflareTurnstile/verify',
            headers=headers,
            json=payload
        )
        response_data = res.json()
        if "jwt" in response_data:
            self.jwtToken = response_data["jwt"]
            print(f"{magenta}[{getTime()}] {red}➩ {green}JWT Token obtained!")
        else:
            print(f"{red}JWT not found: {response_data}")
            exit()
        
        self.login()
        
    def login(self):
        headers = {
            'cf-jwt': self.jwtToken,
            'content-type': 'application/json',
            'origin': 'https://www.wolvesville.com',
            'referer': 'https://www.wolvesville.com/',
            'user-agent': "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
        }
        data = {
            'email': 'example@gmail.com',
            'password': 'qwerty@123',
        }
        res = self.session.post(
            'https://auth.api-wolvesville.com/players/signInWithEmailAndPassword',
            headers=headers,
            json=data
        )
        
        try:
            response_data = res.json()
            print(f"{magenta}[{getTime()}] {red}➩ {green}Login response: {response_data}")
            if 'idToken' in response_data:
                self.idToken = response_data['idToken']
                print(f"{magenta}[{getTime()}] {red}➩ {green}Login successful!")
            else:
                print(f"{red}Login failed! Response:", response_data)
        except Exception as e:
            print(f"{red}Error parsing response:", str(e))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # key get in xevil | https://t.me/Xevil_check_bot?start=5566449246
    key = 'paste your key'
    print(f"{magenta}[{getTime()}] {red}➩ {green}Starting process...")
    print(f"{magenta}[{getTime()}] {red}➩ {green}UTC Time: {getUtcTime()}")
    
    login = Login(key)
    login.turnstile()
    login.getToken()

if __name__ == "__main__":
    main()
