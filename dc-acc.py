print("[ ! ] Loading Modules...\n")
#Holly Secret Project
import os
try: os.system("pip install -r ./data/requirements.txt")
except: pass
try: os.system("py -m pip install -r ./data/requirements.txt")
except: os.system("python -m pip install -r ./data/requirements.txt")

from modules.console import Console
from modules.session import HttpSession
from modules.discord import DiscordApi, DiscordWs
from modules.captcha import CaptchaSolver
import random, threading, httpx, time, json, itertools, os
os.system('cls')

num = "115427" 
print(num)
proxies = open("./data/proxies.txt", 'r+').read().splitlines() 
config = json.load(open("./data/config.json"))

#Console.debug(DiscordApi.verify_mail(session.http_client, token['token']) 

class Discord:
    def __init__(self) -> None:
        try:
            with open("./discord_usernamesd.txt", encoding="utf-8") as f: 
                self.users = [i.strip() for i in f]
        except: self.users = ["i love vast", "vast is cute", "vtg"]
    
    def GEN(self):
        Console._cap_worker += 1
        try:
            self._username = random.choice(self.users)
            proxy = 'http://' + random.choice(proxies)

            session = HttpSession(proxy)
            Console.debug("[*] Created Session (\x1b[38;5;147m%s\x1b[0m)" % (session.http_client.get("https://wtfismyip.com/text").text.strip("\n")))
            api = DiscordApi()

            start_time = time.time()
            capkey = CaptchaSolver().get_captcha_by_ai(proxy.split('://')[1]) 

            if capkey == 'ERROR' or capkey is None:
                Console._proxy_err += 1
                Console.debug(f'[-] Proxy Error (Captcha) | Retrying...')
                return self.GEN()
            
            solve_time = round(time.time() - start_time, 3)
            Console.info(f'[+] Captcha solved: {capkey[:20]} (time taken: {solve_time})')
            Console._hcap_solved += 1

            session.get_cookies()
            token = api.register(session.http_client, capkey, num, self._username)  
            
            if 'token' in str(token):
                Console.info(f'[/] Generated token: {token["token"]}')
                Console._generated += 1
                tokens_file = open("tkns.txt", "a"); tokens_file.write(f'{str(token["token"])}\n'); tokens_file.close()
                flags = DiscordApi.check_flag(session.http_client, token['token'])
               
                Console.info(flags)
                    
                DiscordWs(token).start()
            else:
                Console.debug(f'[-] Register Error: {token}')
                
        except Exception as e:
            
            Console._cap_worker -= 1
            return self.GEN()

        Console._cap_worker -= 1
        
         #Console.debug(DiscordApi.verify_mail(session.http_client, token['token']) 
    def __start__(self):
        threading.Thread(target=Console.title_thread).start()
        while True:
            if threading.active_count() < int(config['threads']):
                threading.Thread(target=self.GEN).start()
                time.sleep(0.1)


if __name__ == '__main__':
    Console.print_logo()
    Discord().__start__()