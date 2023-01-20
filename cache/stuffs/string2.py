from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


button1 = [
    [
        InlineKeyboardButton(text="🥀𝚄𝙿𝙳𝙰𝚃𝙴𝚂🥀", url=f"https://t.me/KING_COBRA_NETWORK"),
        InlineKeyboardButton(text="💥𝙰𝙳𝙳 𝙼𝙴 𝙱𝙰𝙱𝚈💥", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="🤍𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁🤍", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="❣️𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴❣️", callback_data="repo_k"),
    ],                
    [                    
        InlineKeyboardButton(text="✨𝙷𝙴𝙻𝙿 𝙰𝙽𝙳 𝙲𝙼𝙳(𝚜)✨!", callback_data="help_"),
    ],
]


button2 = [
    [
        InlineKeyboardButton(text="✨𝙱𝙰𝚂𝙸𝙲✨", callback_data="basic_"),
        InlineKeyboardButton(text="✨𝙰𝙳𝙼𝙸𝙽✨", callback_data="admin_cmd"),
    ],
    [
        InlineKeyboardButton(text="✨𝙲𝙻𝙾𝚂𝙴✨", callback_data="close_"),
        InlineKeyboardButton(text="« 𝙱𝙰𝙲𝙺 «", callback_data="HOME"),
    ],
]



button3 = [
    [
        InlineKeyboardButton(text="💥𝚂𝙾𝚄𝚁𝙲𝙴💥", url="https://telegra.ph/file/9b0455dae14d5639f936d.mp4"),
        InlineKeyboardButton(text="« 𝙱𝙰𝙲𝙺 «", callback_data="HOME"),
    ],
]


button4 = [
    [
        InlineKeyboardButton(text="✨𝙲𝙻𝙾𝚂𝙴✨", callback_data="close_"),
        InlineKeyboardButton(text="« 𝙱𝙰𝙲𝙺 «", callback_data="help_"),
    ],
]





