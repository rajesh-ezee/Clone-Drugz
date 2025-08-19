from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="↻", callback_data="replay_cb),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
    [
            InlineKeyboardButton(
                text="ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/HeartBeat_Offi"
            ),
            InlineKeyboardButton(
                text="ᴄʜᴀᴛ", url=f"https://t.me/HeartBeat_Fam"
            ),
        ],
)

