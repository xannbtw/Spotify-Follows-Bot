
# DISCORD: xann wrld#9953
# GITHUB: https://github.com/xannbtw/
#This script was made for educational purposes, I am not responsible for your actions using this script.

import threading, os, time, sys, random, string, requests, colorama
from colorama import Fore


if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")




def menu():
    print(Fore.GREEN  + """\n\n


███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝   
╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝    
███████║██║     ╚██████╔╝   ██║   ██║██║        ██║      
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝       
                                  By: xann wrld#9953
                                                        
> https://github.com/xannbtw/ ~ https://discord.gg/Ww4kgVdJ
\n\n
""" + Fore.RESET)


clear()

correct_password = "MQnpyKDVWwtcC96Ut4jJURp4y4ngCh"

password = input('Enter password: ')

if password == correct_password:
    clear()
    menu()
    time.sleep(3)
else:
    exit()
    


lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
spotify_profile = str(input("[>] Spotify Link: "))
threads = int(input("\n[>] Threads: "))


    
class spotify:

    def __init__(self, profile, proxy = None):
        self.session = requests.Session()
        self.profile = profile
        self.proxy = proxy
    
    def register_account(self):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.spotify.com/"
        }
        email = ("").join(random.choices(string.ascii_letters + string.digits, k = 8)) + "@gmail.com"
        password = ("").join(random.choices(string.ascii_letters + string.digits, k = 8))
        proxies = None
        if self.proxy != None:
            proxies = {"https": f"http://{self.proxy}"}
        data = f"birth_day=1&birth_month=01&birth_year=1970&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/uk/&displayname=github.com/xannbtw&email={email}&gender=neutral&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={password}&password_repeat={password}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0"
        try:
            create = self.session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers = headers, data = data, proxies = proxies)
            if "login_token" in create.text:
                login_token = create.json()['login_token']
                with open("Created.txt", "a") as f:
                    f.write(f'{email}:{password}:{login_token}\n')
                return login_token
            else:
                return None
        except:
            return False

    def get_csrf_token(self):
        try:
            r = self.session.get("https://www.spotify.com/uk/signup/?forward_url=https://accounts.spotify.com/en/status&sp_t_counter=1")
            return r.text.split('csrfToken":"')[1].split('"')[0]
        except:
            return None
        
    def get_token(self, login_token):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRF-Token": self.get_csrf_token(),
            "Host": "www.spotify.com"
        }
        self.session.post("https://www.spotify.com/api/signup/authenticate", headers = headers, data = "splot=" + login_token)
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "app-platform": "WebPlayer",
            "Host": "open.spotify.com",
            "Referer": "https://open.spotify.com/"
        }
        try:
            r = self.session.get(
                "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                headers = headers
            )
            return r.json()["accessToken"]
        except:
            return None

    def follow(self):
        if "/user/" in self.profile:
            self.profile = self.profile.split("/user/")[1]
        if "?" in self.profile:
            self.profile = self.profile.split("?")[0]
        login_token = self.register_account()
        if login_token == None:
            return None, "while registering, ratelimit"
        elif login_token == False:
            return None, f"bad proxy on register {self.proxy}"
        auth_token = self.get_token(login_token)
        if auth_token == None:
            return None, "while getting auth token"
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "app-platform": "WebPlayer",
            "Referer": "https://open.spotify.com/",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "authorization": "Bearer {}".format(auth_token),
        }
        try:
            self.session.put(
                "https://api.spotify.com/v1/me/following?type=user&ids=" + self.profile,
                headers = headers
            )
            return True, None
        except:
            return False, "while following"


def load_proxies():
    if not os.path.exists("proxies.txt"):
        print("\nFile proxies.txt not found")
        time.sleep(10)
        os._exit(0)
    with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print("\nNo proxies loaded in proxies.txt")
            time.sleep(10)
            os._exit(0)

print("\n[1] Load Proxies\n")
option = int(input("\n> "))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print(Fore.GREEN + "[>] Follow {}".format(counter))
    else:
        safe_print(Fore.RESET + f"[>] Error {error}")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: 
            proxy_counter = 0