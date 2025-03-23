from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
from pyrogram.enums import ChatAction
import random
import os
import asyncio
import time
from datetime import datetime

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", "") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "mr_sukkun")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "legend_coder")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "the_support_chat")
BOT_NAME = os.environ.get("BOT_NAME", "CHATBOT")
START_IMG = os.environ.get("START_IMG", "")

STKR = os.environ.get("STKR", "")

StartTime = time.time()

Tanjiro = Client(
    "chat-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START = f"""
**๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}**
**➻ ᴀɴ ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**
**──────────────────**
**➻ ᴜsᴀɢᴇ /chatbot [on/off]**
**๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help**
"""

MAIN = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍᴅs ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text=" ᴜᴘᴅᴀᴛᴇs ", url=f"https://t.me/{UPDATE_CHNL}"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
]

HELP_READ = "**ᴜsᴀɢᴇ ☟︎︎︎**\n**➻ ᴜsᴇ** `/chatbot on` **ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ.**\n**➻ ᴜsᴇ** `/chatbot off` **ᴛᴏ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.**\n**๏ ɴᴏᴛᴇ ➻ ʙᴏᴛʜ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴄʜᴀᴛ-ʙᴏᴛ ᴏɴ/ᴏғғ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!!**\n\n**➻ ᴜsᴇ** `/ping` **ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**"

HELP_BACK = [[InlineKeyboardButton(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK")]]

@Tanjiro.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    accha = await m.reply_text(text="Starting...")
    await asyncio.sleep(1)
    await accha.delete()
    umm = await m.reply_sticker(sticker=STKR)
    await asyncio.sleep(1)
    await umm.delete()
    await m.reply_photo(photo=START_IMG, caption=START, reply_markup=InlineKeyboardMarkup(MAIN))

@Tanjiro.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
        await query.message.edit_text(text=HELP_READ, reply_markup=InlineKeyboardMarkup(HELP_BACK))
    elif query.data == "HELP_BACK":
        await query.message.edit(text=START, reply_markup=InlineKeyboardMarkup(MAIN))

@Tanjiro.on_message(filters.command(["help", f"help@{BOT_USERNAME}"]))
async def restart(client, message):
    await message.reply_photo(START_IMG, caption=HELP_READ, reply_markup=InlineKeyboardMarkup(HELP_BACK))

@Tanjiro.on_message(filters.command(["ping", "alive"]))
async def ping(client, message: Message):
    start = datetime.now()
    txxt = await message.reply("__ριиgιиg...__")
    await asyncio.sleep(0.5)
    await txxt.delete()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await message.reply_photo(
        photo=START_IMG,
        caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME})** ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴡɪᴛʜ ᴘᴏɴɢ ᴏꜰ `{ms}` ms",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )

@Tanjiro.on_message(filters.command(["chatbot off"]) & ~filters.private)
async def chatbot_off(client, message):
    tanjiro_db = MongoClient(MONGO_URL)["TanjiroDb"]["Tanjiro"]
    if message.from_user and message.from_user.id not in await is_admins(message.chat.id):
        return await message.reply_text("You are not admin")
    is_tanjiro = tanjiro_db.find_one({"chat_id": message.chat.id})
    if not is_tanjiro:
        tanjiro_db.insert_one({"chat_id": message.chat.id})
        await message.reply_text("Chatbot Disabled!")
    else:
        await message.reply_text("ChatBot Already Disabled")

@Tanjiro.on_message(filters.command(["chatbot on"]) & ~filters.private)
async def chatbot_on(client, message):
    tanjiro_db = MongoClient(MONGO_URL)["TanjiroDb"]["Tanjiro"]
    if message.from_user and message.from_user.id not in await is_admins(message.chat.id):
        return await message.reply_text("You are not admin")
    is_tanjiro = tanjiro_db.find_one({"chat_id": message.chat.id})
    if is_tanjiro:
        tanjiro_db.delete_one({"chat_id": message.chat.id})
        await message.reply_text("ChatBot Enabled!")
    else:
        await message.reply_text("Chatbot Already Enabled")

@Tanjiro.on_message(filters.command(["chatbot"]) & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**ᴜsᴀɢᴇ:**\n/**chatbot [on/off]**\n**ᴄʜᴀᴛ-ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ(s) ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!**")

Tanjiro.run()
