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

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**𝐇𝐞𝐥𝐥𝐨 👋 [{}](tg://user?id={})!**\n\n🤖 𝐈 𝐀𝐦 𝐀𝐧 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐁𝐨𝐭 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲 [ᴄᴏʙʀᴀ](t.me/Xd_Lif)  𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐌𝐮𝐬𝐢𝐜 𝐈𝐧 𝐓𝐡𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭'𝐬 𝐎𝐅 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐆𝐫𝐨𝐮𝐩'𝐬 & 𝐂𝐡𝐚𝐧𝐧𝐞𝐥'𝐬.\n\n✅ 𝐒𝐞𝐧𝐝 𝐌𝐞 /help 𝐅𝐨𝐫𝐞 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨."
      HELP_MSG = [
        ".",
f"""
**𝐇𝐞𝐲 👋 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐁𝐚𝐜𝐤 𝐓𝐨 {PROJECT_NAME}

👻 {PROJECT_NAME} 𝐂𝐀𝐍 𝐏𝐋𝐀𝐘 𝐌𝐔𝐒𝐈𝐂 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏'𝐒 𝐕𝐎𝐈𝐂𝐄 𝐂𝐇𝐀𝐓 𝐀𝐒 𝐖𝐄𝐋𝐋 𝐀𝐒 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐕𝐎𝐈𝐂𝐄 𝐂𝐇𝐀𝐓𝐒

👻 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 𝐍𝐀𝐌𝐄 >> @{ASSISTANT_NAME}\n\n𝐂𝐋𝐈𝐂𝐊 𝐍𝐄𝐗𝐓 𝐅𝐎𝐑 𝐈𝐍𝐒𝐓𝐑𝐔𝐂𝐓𝐈𝐎𝐍𝐒**
""",

f"""
**𝐒𝐄𝐓𝐓𝐈𝐍𝐆 𝐔𝐏**

1) 𝐌𝐀𝐊𝐄 𝐁𝐎𝐓 𝐀𝐃𝐌𝐈𝐍 (𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐈𝐅 𝐔𝐒𝐄 𝐂𝐏𝐋𝐀𝐘)
2) 𝐒𝐓𝐀𝐑𝐓 𝐀 𝐕𝐎𝐈𝐂𝐄 𝐂𝐇𝐀𝐓 
3) 𝐓𝐑𝐘 /play [𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄] 𝐅𝐎𝐑 𝐓𝐇𝐄 𝐅𝐈𝐑𝐒𝐓 𝐓𝐈𝐌𝐄 𝐁𝐘 𝐀𝐍 𝐀𝐃𝐌𝐈𝐍 
*) 𝐈𝐅 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐉𝐎𝐈𝐍𝐄𝐃 𝐄𝐍𝐉𝐎𝐘 𝐌𝐔𝐒𝐔𝐂, 𝐈𝐅 𝐍𝐎𝐓 𝐀𝐃𝐃  @{ASSISTANT_NAME} 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐑𝐄𝐓𝐑𝐘 

**𝐅𝐎𝐑 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐌𝐔𝐒𝐈𝐂 𝐏𝐋𝐀𝐘**
1) 𝐌𝐀𝐊𝐄 𝐌𝐄 𝐀𝐃𝐌𝐈𝐍 𝐎𝐅 𝐘𝐎𝐔𝐑 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 
2) 𝐒𝐄𝐍𝐃 /userbotjoinchannel 𝐈𝐍 𝐋𝐈𝐍𝐊𝐄𝐃 𝐆𝐑𝐎𝐔𝐏 
3) 𝐍𝐎𝐖 𝐒𝐄𝐍𝐃 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐈𝐍 𝐋𝐈𝐍𝐊𝐄𝐃 𝐆𝐑𝐎𝐔𝐏
""",
f"""
**𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒**

**=>> 𝐒𝐎𝐍𝐆 𝐏𝐋𝐀𝐘𝐈𝐍𝐆 🎧**

- /play: 𝐏𝐋𝐀𝐘 𝐓𝐇𝐄 𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐃 𝐓𝐇𝐄 𝐒𝐎𝐍𝐆 
- /play [𝐘𝐓 𝐔𝐑𝐋] : 𝐏𝐋𝐀𝐘 𝐓𝐇𝐄 𝐆𝐈𝐕𝐄𝐍 𝐘𝐓 𝐔𝐑𝐋 
- /play [𝐑𝐄𝐏𝐋𝐀𝐘 𝐓𝐎 𝐘𝐎 𝐀𝐔𝐃𝐈𝐎]: 𝐏𝐋𝐀𝐘 𝐑𝐄𝐏𝐋𝐈𝐄𝐃 𝐀𝐔𝐃𝐈𝐎
- /splay: 𝐏𝐋𝐀𝐘 𝐒𝐎𝐍𝐆 𝐕𝐈𝐀 𝐉𝐈𝐎 𝐒𝐀𝐀𝐕𝐍 
- /ytplay: 𝐃𝐈𝐑𝐄𝐂𝐓𝐋𝐘 𝐏𝐋𝐀𝐘 𝐒𝐎𝐍𝐆 𝐕𝐈𝐀 𝐘𝐎𝐔𝐓𝐔𝐁𝐄 𝐌𝐔𝐒𝐈𝐂

**=>> 𝐏𝐋𝐀𝐘𝐁𝐀𝐂𝐊 ⏯**

- /player: 𝐎𝐏𝐍𝐄 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒 𝐌𝐄𝐍𝐔 𝐎𝐅 𝐏𝐋𝐀𝐘𝐄𝐑 
- /skip: 𝐒𝐊𝐈𝐏𝐒 𝐓𝐇𝐄 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐓𝐑𝐀𝐂𝐊
- /pause: 𝐏𝐀𝐔𝐒𝐄 𝐓𝐑𝐀𝐂𝐊
- /resume: 𝐑𝐄𝐒𝐔𝐌𝐄𝐒 𝐓𝐇𝐄 𝐏𝐀𝐔𝐒𝐄𝐃 𝐓𝐑𝐀𝐂𝐊 
- /end: 𝐒𝐓𝐎𝐏𝐒 𝐌𝐄𝐃𝐈𝐀 𝐏𝐋𝐀𝐘𝐁𝐀𝐂𝐊 
- /current: 𝐒𝐇𝐎𝐖𝐒 𝐓𝐇𝐄 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐏𝐋𝐀𝐘𝐈𝐍𝐆 𝐓𝐑𝐀𝐂𝐊 
- /playlist: 𝐒𝐇𝐎𝐖𝐒 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓 playlist

*𝐏𝐋𝐀𝐘𝐄𝐑 𝐂𝐌𝐃 𝐀𝐍𝐃 𝐀𝐋𝐋 𝐎𝐓𝐇𝐄𝐑 𝐂𝐌𝐃𝐒 𝐄𝐗𝐂𝐄𝐏𝐓 /play, /current  𝐀𝐍𝐃 /playlist  𝐀𝐑𝐄 𝐎𝐍𝐋𝐘 𝐅𝐎𝐑 𝐀𝐃𝐌𝐈𝐍 𝐎𝐅 𝐓𝐇𝐄 𝐆𝐑𝐎𝐔𝐏.
""",

f"""
**=>> 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐌𝐔𝐒𝐈𝐂 𝐏𝐋𝐀𝐘 🛠**

⚪️ 𝐅𝐎𝐑 𝐋𝐈𝐍𝐊𝐄𝐃 𝐆𝐑𝐎𝐔𝐏 𝐀𝐃𝐌𝐈𝐍 𝐎𝐍𝐋𝐘:

- /cplay [𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄] - 𝐏𝐋𝐀𝐘 𝐒𝐎𝐍𝐆 𝐘𝐎𝐔 𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃
- /csplay [𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄 ] - 𝐏𝐋𝐀𝐘 𝐒𝐈𝐍𝐆 𝐑𝐄𝐐𝐔𝐄𝐒𝐓𝐄𝐃 𝐕𝐈𝐀 𝐉𝐈𝐎 𝐒𝐀𝐀𝐕𝐍
- /cplaylist - 𝐒𝐇𝐎𝐖 𝐍𝐎𝐖 𝐏𝐋𝐀𝐘𝐈𝐍𝐆 𝐋𝐈𝐒𝐓 
- /cccurrent - 𝐒𝐇𝐎𝐖 𝐍𝐎𝐖 𝐏𝐋𝐀𝐘𝐈𝐍𝐆 
- /cplayer - 𝐎𝐏𝐄𝐍 𝐌𝐔𝐒𝐈𝐂 𝐏𝐋𝐀𝐘𝐄𝐑 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒 𝐏𝐀𝐍𝐄𝐋
- /cpause - 𝐏𝐀𝐔𝐒𝐄 𝐒𝐎𝐍𝐆 𝐏𝐋𝐀𝐘 
- /cresume - 𝐑𝐄𝐒𝐔𝐌𝐄 𝐒𝐎𝐍𝐆 𝐏𝐋𝐀𝐘
- /cskip - 𝐏𝐋𝐀𝐘 𝐍𝐄𝐗𝐓 𝐒𝐎𝐍𝐆
- /cend - 𝐒𝐓𝐎𝐏 𝐌𝐔𝐒𝐈𝐂 𝐏𝐋𝐀𝐘
- /userbotjoinchannel - 𝐈𝐍𝐕𝐈𝐓𝐄 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐂𝐇𝐀𝐓 

𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐈𝐒 𝐀𝐋𝐒𝐎 𝐂𝐀𝐍 𝐁𝐄 𝐔𝐒𝐄𝐃 𝐈𝐍𝐒𝐓𝐄𝐀𝐃 𝐎𝐅 𝐂 ( /cplay = /channelplay )

👻 𝐈𝐅 𝐘𝐎𝐔 𝐃𝐎𝐍𝐋𝐓 𝐋𝐈𝐊𝐄 𝐓𝐎 𝐏𝐋𝐀𝐘 𝐈𝐍 𝐋𝐈𝐍𝐊𝐄𝐃 𝐈𝐍 𝐆𝐑𝐎𝐔𝐏:

1) 𝐆𝐄𝐓 𝐘𝐎𝐔𝐑 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐈𝐃.
2) 𝐂𝐑𝐄𝐀𝐓𝐄 𝐀 𝐆𝐑𝐎𝐔𝐏 𝐖𝐈𝐓𝐇 𝐓𝐈𝐓𝐓𝐋𝐄: 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐌𝐔𝐒𝐈𝐂: 𝐘𝐎𝐔𝐑_𝐂𝐇𝐀𝐍𝐍𝐄𝐋_𝐈𝐃
3) 𝐀𝐃𝐃 𝐁𝐎𝐓 𝐀𝐒 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐀𝐃𝐌𝐈𝐍 𝐖𝐈𝐓𝐇 𝐅𝐔𝐋𝐋 𝐏𝐄𝐑𝐌𝐒
4) 𝐀𝐃𝐃 @{ASSISTANT_NAME} 𝐓𝐎 𝐓𝐇𝐑 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐀𝐒 𝐀𝐍 𝐀𝐃𝐌𝐈𝐍.
5) 𝐒𝐈𝐌𝐏𝐋𝐘 𝐒𝐄𝐍𝐃 𝐂𝐊𝐌𝐌𝐀𝐍𝐃𝐒 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏. (𝐑𝐄𝐌𝐄𝐌𝐁𝐄𝐑 𝐓𝐎 𝐔𝐒𝐄 /ytplay 𝐈𝐍𝐒𝐓𝐄𝐀𝐃 /play)
""",

f"""
**=>> 𝐌𝐎𝐑𝐄 𝐓𝐎𝐎𝐋𝐒  🧑‍🔧**

- /musicplayer [𝐎𝐍/𝐎𝐅𝐅]: 𝐄𝐍𝐀𝐁𝐋𝐄/𝐃𝐈𝐒𝐀𝐁𝐋𝐄 𝐌𝐔𝐒𝐈𝐂 𝐏𝐋𝐀𝐘𝐄𝐑
- /admincache:𝐔𝐏𝐃𝐀𝐓𝐄𝐒 𝐀𝐃𝐌𝐈𝐍 𝐈𝐍𝐅𝐎 𝐎𝐅 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏. 𝐓𝐑𝐘 𝐈𝐅 𝐁𝐎𝐓 𝐈𝐒𝐍'𝐓 𝐑𝐄𝐂𝐎𝐆𝐍𝐈𝐙𝐄 𝐀𝐃𝐌𝐈𝐍
- /userbotjoin: 𝐈𝐍𝐕𝐈𝐓𝐄 @{ASSISTANT_NAME} 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐂𝐇𝐀𝐓 
""",
f"""
**=>> 𝐒𝐎𝐍𝐆 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃  🎸**

- /video [𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄]: 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 𝐕𝐈𝐃𝐎 𝐒𝐎𝐍𝐆 𝐅𝐑𝐎𝐌 𝐘𝐎𝐔𝐓𝐔𝐁𝐄
- /song [𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄]: 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 𝐀𝐔𝐃𝐈𝐎 𝐒𝐎𝐍𝐆 𝐅𝐑𝐎𝐌 𝐘𝐎𝐔𝐓𝐔𝐁𝐄 
- /saavn [𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄]: 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 𝐒𝐎𝐍𝐆 𝐅𝐑𝐎𝐌 𝐒𝐀𝐀𝐕𝐍 
- /deezer [𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄]: 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃 𝐒𝐎𝐍𝐆 𝐅𝐑𝐎𝐌 𝐃𝐄𝐄𝐙𝐄𝐑 

**=>> 𝐒𝐄𝐀𝐑𝐂𝐇 𝐓𝐎𝐎𝐋𝐒 📄**

- /search [𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄]: 𝐒𝐄𝐀𝐑𝐂𝐇 𝐘𝐎𝐔𝐓𝐔𝐁𝐄 𝐅𝐎𝐑 𝐒𝐎𝐍𝐆𝐒
- /lyrics [𝐒𝐎𝐍𝐆 𝐍𝐀𝐌𝐄]: 𝐆𝐄𝐓 𝐒𝐎𝐍𝐆 𝐋𝐘𝐑𝐈𝐂𝐄 
""",

f"""
**=>> 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐅𝐎𝐑 𝐒𝐔𝐃𝐎 𝐔𝐒𝐄𝐑𝐒 ⚔️**

 - /userbotleaveall - 𝐑𝐄𝐌𝐎𝐕𝐄 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓 𝐅𝐑𝐎𝐌 𝐀𝐋𝐋 𝐂𝐇𝐀𝐓𝐒 
 - /broadcast <reply to message> - 𝐆𝐋𝐎𝐁𝐀𝐋𝐋𝐘 𝐁𝐑𝐎𝐃𝐂𝐀𝐒𝐓 𝐑𝐄𝐏𝐋𝐈𝐄𝐃 𝐌𝐀𝐒𝐒𝐄𝐒𝐃 𝐓𝐎 𝐀𝐋𝐋 𝐂𝐇𝐀𝐓𝐒
 - /pmpermit [𝐎𝐍/𝐎𝐅𝐅] - 𝐄𝐍𝐀𝐁𝐋𝐄/𝐃𝐈𝐒𝐀𝐁𝐋𝐄 𝐏𝐌𝐏𝐄𝐑𝐌𝐈𝐓 𝐌𝐄𝐒𝐒𝐀𝐆𝐄
*𝐒𝐔𝐃𝐎 𝐔𝐒𝐄𝐑𝐒 𝐂𝐀𝐍 𝐄𝐗𝐄𝐂𝐔𝐓𝐄 𝐀𝐍𝐘 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐈𝐍 𝐀𝐍𝐘 𝐆𝐑𝐎𝐔𝐏𝐒

"""
      ]
