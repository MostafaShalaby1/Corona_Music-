from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


button1 = [
    [
        InlineKeyboardButton(text="π₯ππΏπ³π°ππ΄ππ₯", url=f"https://t.me/KING_COBRA_NETWORK"),
        InlineKeyboardButton(text="π₯π°π³π³ πΌπ΄ π±π°π±ππ₯", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="π€π³π΄ππ΄π»πΎπΏπ΄ππ€", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="β£οΈππΎπππ²π΄ π²πΎπ³π΄β£οΈ", callback_data="repo_k"),
    ],                
    [                    
        InlineKeyboardButton(text="β¨π·π΄π»πΏ π°π½π³ π²πΌπ³(π)β¨!", callback_data="help_"),
    ],
]


button2 = [
    [
        InlineKeyboardButton(text="β¨π±π°ππΈπ²β¨", callback_data="basic_"),
        InlineKeyboardButton(text="β¨π°π³πΌπΈπ½β¨", callback_data="admin_cmd"),
    ],
    [
        InlineKeyboardButton(text="β¨π²π»πΎππ΄β¨", callback_data="close_"),
        InlineKeyboardButton(text="Β« π±π°π²πΊ Β«", callback_data="HOME"),
    ],
]



button3 = [
    [
        InlineKeyboardButton(text="π₯ππΎπππ²π΄π₯", url="https://telegra.ph/file/9b0455dae14d5639f936d.mp4"),
        InlineKeyboardButton(text="Β« π±π°π²πΊ Β«", callback_data="HOME"),
    ],
]


button4 = [
    [
        InlineKeyboardButton(text="β¨π²π»πΎππ΄β¨", callback_data="close_"),
        InlineKeyboardButton(text="Β« π±π°π²πΊ Β«", callback_data="help_"),
    ],
]





