# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from DaisyXMusic.helpers.decorators import authorized_users_only
from DaisyXMusic.helpers.decorators import errors
from DaisyXMusic.services.callsmusic import client as USER
from DaisyXMusic.config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>𝐀𝐝𝐝 𝐌𝐞 𝐀𝐬 𝐀𝐝𝐦𝐢𝐧 𝐨𝐅 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐅𝐢𝐫𝐬𝐭</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "𝐀𝐥𝐢𝐳𝐚 𝐌𝐮𝐬𝐢𝐜 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐉𝐨𝐢𝐧𝐞𝐝 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 [★ᴄᴏʙʀᴀ](t.me/Xd_Lif)")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your chat</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>👻 𝐅𝐥𝐨𝐨𝐝 𝐖𝐚𝐢𝐭 𝐄𝐫𝐫𝐨𝐫 👻 \n 𝐔𝐬𝐞𝐫 {user.first_name} 𝐂𝐨𝐮𝐥𝐝𝐧'𝐓 𝐉𝐨𝐢𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐃𝐮𝐞 𝐓𝐨 𝐇𝐞𝐚𝐯𝐲 𝐉𝐨𝐢𝐧 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐅𝐨𝐫 𝐔𝐬𝐞𝐫𝐁𝐨𝐭! 𝐌𝐚𝐤𝐞 𝐒𝐮𝐫𝐞 𝐔𝐬𝐞𝐫 𝐈𝐬 𝐍𝐨𝐭 𝐁𝐚𝐧𝐧𝐞𝐝 𝐈𝐧 𝐆𝐫𝐨𝐮𝐩."
            "\n\nOr 𝐌𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐀𝐝𝐝 @AlizaProBot 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐓𝐫𝐲 𝐀𝐠𝐢𝐧</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your chat</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>𝐔𝐬𝐞𝐫 𝐂𝐨𝐮𝐥𝐝𝐧'𝐭 𝐋𝐞𝐚𝐯𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩! 𝐌𝐚𝐲 𝐁𝐞 𝐅𝐥𝐨𝐨𝐝𝐖𝐚𝐢𝐭𝐬."
            "\n\nOr 𝐌𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐊𝐢𝐜𝐤 𝐌𝐞 𝐅𝐫𝐨𝐦 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐀𝐥𝐥 𝐋𝐞𝐚𝐯𝐢𝐧𝐠 𝐀𝐥𝐥 𝐂𝐡𝐚𝐭𝐬")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>𝐀𝐝𝐝 𝐌𝐞 𝐀𝐬 𝐀𝐝𝐦𝐢𝐧 𝐨𝐅 𝐘𝐨𝐮𝐫 Channel 𝐅𝐢𝐫𝐬𝐭</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your channel</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your channel due to heavy join requests for userbot! Make sure user is not banned in channel."
            "\n\nOr manually add @DaisyXhelper to your Group and try again</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your channel</b>",
    )
    
