import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["عفرتو","مطور السورس","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ْ𓆩⧛ َ 𝘼َِ𝙁َِ𝙍َِ𝙊َِ𝙊َِ𝙏َِ𝙊ِ ┇ عـ๋͜‏ـۂفــ͡ـࢪتوُ ⧚𓆪](https://t.me/IIUll_l)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @IIUll_l ❫
◉ 𝙸𝙳      : ❪ `5904216848` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@UI_VM)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ْ𓆩⧛ َ 𝘼َِ𝙁َِ𝙍َِ𝙊َِ𝙊َِ𝙏َِ𝙊ِ ┇ عـ๋͜‏ـۂفــ͡ـࢪتوُ ⧚𓆪", url=f"https://t.me/IIUll_l"), 
                 ],[
                   InlineKeyboardButton(
                        "「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」", url=f"https://t.me/UI_VM"),
                ],

            ]

        ),

    )
@app.on_message(
    command(["مطور", "المطور"])
    & filters.group
  
)
async def kimmyy(client: Client, message: Message):
    usr = await client.get_users(OWNER)
    name = usr.first_name
    async for photo in client.iter_profile_photos(OWNER, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀⌯⊶★━⩺**
                    
🔥 ¦𝚆𝙾𝙽𝙴𝚁 :[{usr.first_name}](https://t.me/{OWNER})
📀 ¦𝚄𝚂𝙴𝚁 :@{OWNER} 
🆔 ¦𝙸𝙳 :`{usr.id}`
 
**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀⌯⊶★━⩺** """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{OWNER}")
            ],                   
          ]              
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    await app.send_message(OWNER, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
                    return await app.send_message(config.LOG_GROUP_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
      
