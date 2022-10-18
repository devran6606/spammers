from .. import worker
from telethon import events, Button

@worker.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Yapımcım Hakkında",
                    buttons=[
                        [Button.url("✨ Developer", url="https://t.me/affetmezzz")],
                        [Button.inline("✨ Help",data="op")]
                    ])

@worker.on(events.callbackquery.CallbackQuery(data="op"))
async def ex(event):
    await event.edit("Yardım için bu komutu kullanın lütfen /help",
                    buttons=[
                        [Button.url("✨ İletişim", url="https://t.me/affetmezzz")]
                    ])
