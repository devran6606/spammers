from .. import worker
from telethon import events, Button

@worker.on(events.NewMessage(incoming=True, pattern="/dev"))
async def repo(event):
    await event.reply("Yapımcım ile iletişime geçmek için butona basın",
                    buttons=[
                        [Button.url("🍪 Affetmez", url="https://t.me/affetmezzz")]
                    ])
