# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚


import asyncio
from pyrogram.types import Message
from pyrogram import Client, filters
from helpers.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import authorized_users_only
from callsmusic.callsmusic import client as user

STR_ID = "CAACAgUAAxkBAAEBo-ZjyuZWn49WUo_mVDyMwHNAxIhXnwAC2AcAAq0O2VVIUc9d3v4gPy0E"

@Client.on_message(
    command("mjoinub") & ~filters.bot
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invite_link = await m.chat.export_invite_link()
        if "+" in invite_link:
            link_hash = (invite_link.replace("+", "")).split("t.me/")[1]
            await user.join_chat(f"https://t.me/joinchat/{link_hash}")
        await m.chat.promote_member(
            (await user.get_me()).id,
            can_manage_voice_chats=True
        )
        return await user.send_message(chat_id, "ᴏᴋᴋ, ᴀssɪsᴛᴀɴᴛ ᴊᴏɪɴᴇᴅ ᴛʜɪs ɢʀᴏᴜᴘ ɴᴏᴡ ᴇɴᴊᴏʏ sɪʟᴇɴᴛ ᴍᴜsɪᴄ💫")
    except UserAlreadyParticipant:
        admin = await m.chat.get_member((await user.get_me()).id)
        if not admin.can_manage_voice_chats:
            await m.chat.promote_member(
                (await user.get_me()).id,
                can_manage_voice_chats=True
            )
            return await user.send_message(chat_id, "ʜᴜʜ, ᴡʜʏ ʙᴜʟʟʏ ᴜɴᴋɪʟ🙄, ᴀssɪsᴛᴀɴᴛ ɪᴢ sᴛɪʟʟ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ")
        return await user.send_message(chat_id, "ʜᴜʜ, ᴡʜʏ ʙᴜʟʟʏ ᴜɴᴋɪʟ🙄, ᴀssɪsᴛᴀɴᴛ ɪᴢ sᴛɪʟʟ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ")
