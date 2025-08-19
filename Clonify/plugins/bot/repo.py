from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Clonify import app
from config import BOT_USERNAME
from Clonify.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
<blockquote>**ʜʙ-ᴄʟᴏɴᴇ** - Tʜᴇ Uʟᴛɪᴍᴀᴛᴇ Tᴇʟᴇɢʀᴀᴍ Mᴜsɪᴄ Sᴏʟᴜᴛɪᴏɴ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇs.</blockquote>
<blockquote>┏━━━━━━━━━━━━━━━━━⧫
┠ ◆ **sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ:** [ᴄʟɪᴄᴋ-ʜᴇʀᴇ](https://t.me/HeartBeat_Fam)  
┠ ◆ **ᴅᴇᴠᴇʟᴏᴘᴇʀ:** [ɢʜᴏ𝗌ᴛ-ʙᴀᴛ](https://t.me/GhosttBatt)
┠ ◆ **ʀᴇʟᴇᴀsᴇᴅ ʙʏ:** [ʜᴇᴀʀᴛ-ʙᴇᴀᴛ](https://t.me/HeartBeat_Offi)
┗━━━━━━━━━━━━━━━━━⧫</blockquote>
<blockquote>__Fᴏʀᴋ ɪᴛ, ᴄᴜsᴛᴏᴍɪᴢᴇ ɪᴛ, ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ʏᴏᴜʀ ᴏᴡɴ!__</blockquote>
"""





@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
                InlineKeyboardButton("𝗌ᴜᴘᴘᴏʀᴛ", url="https://t.me/HeartBeat_Fam"),
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/HeartBeat_Offi")
        ],
        [ 
          InlineKeyboardButton("𝗌ᴏᴜʀᴄᴇ-ᴄᴏᴅᴇ", url=f"https://t.me/GhosttBatt")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://i.ibb.co/gFm6VW52/source-code.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://t.me/GhosttBatt")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/HeartBeat_Offi) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/HeartBeat_Fam)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
