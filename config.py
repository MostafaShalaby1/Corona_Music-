# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_USERNAME = getenv("OWNER_USERNAME", "cute_arnavsingh")
BOT_USERNAME = getenv("BOT_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "link_copied")
BOT_NAME = getenv("BOT_NAME", "ᴄᴏʀᴏɴᴀ ᴍᴜsɪᴄ🥀")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/4ef1c176779bf097f8a20.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5547586019").split()))
