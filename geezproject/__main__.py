""" geezproject start point """


import sys
import requests
from importlib import import_module

from pytgcalls import idle

from geezproject import BOT_TOKEN, BOT_VER, blacklistgeez
from geezproject import DEVS, LOGS, LOOP, bot, call_py, BOTLOG_CHATID
from geezproject.clients import geez_userbot_on, multigeez
from geezproject.modules import ALL_MODULES
from geezproject.utils import autobot, autocreategroup

try:
    client = multigeez()
    total = 5 - client
    bot.start()
    call_py.start()
    user = bot.get_me()
    blacklistgeez = requests.get(
        "https://raw.githubusercontent.com/vckyou/Reforestation/master/blacklistgeez.json"
    ).json()
    if user.id in blacklistgeez:
        LOGS.warning(
            "NAMPAKNYA 𝗛𝗘𝗥𝗢𝗜𝗡𝗙𝗔𝗧𝗛𝗘𝗥 TIDAK DAPAT BEKERJA, MUNGKIN ANDA TELAH DI BLACKLIST OLEH PEMILIK 𝗛𝗘𝗥𝗢𝗜𝗡𝗙𝗔𝗧𝗛𝗘𝗥."        )
        sys.exit(1)
    if 874946835 not in DEVS:
        LOGS.warning(
            f"EOL\𝗛𝗘𝗥𝗢𝗜𝗡𝗙𝗔𝗧𝗛𝗘𝗥 v{BOT_VER}."
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("geezproject.modules." + module_name)

LOGS.info(f"Total Clients = {total} User")
LOGS.info(f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/worstpartyinc")
LOGS.info(f"🕷 𝗛𝗘𝗥𝗢𝗜𝗡𝗙𝗔𝗧𝗛𝗘𝗥 Berhasil Diaktfikan 🕷")


LOOP.run_until_complete(geez_userbot_on())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(autocreategroup())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
