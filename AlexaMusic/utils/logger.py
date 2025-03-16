# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from pyrogram.enums import ParseMode

from config import LOG_GROUP_ID
from AlexaMusic.utils.database import is_on_off
from AlexaMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} 𝖯𝗅𝖺𝗒 𝖫𝗈𝗀</b>

<b>kimlik id :</b> <code>{message.chat.id}</code>
<b>grup adı :</b> {message.chat.title}
<b>kullanıcı adı:</b> @{message.chat.username}

<b>kullanıcı id :</b> <code>{message.from_user.id}</code>
<b>isim :</b> {message.from_user.mention}
<b>kullanıcı adı:</b> @{message.from_user.username}

<b>kuyru :</b> {message.text.split(None, 1)[1]}
<b>𝖲𝗍𝗋𝖾𝖺𝗆-𝖳𝗒𝗉𝖾 :</b> {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=-1002629977112,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
