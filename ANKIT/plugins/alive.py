from telethon import events
import os
from .. import worker
from spam-bot import BOT_USERS, BOT_USER, ALIVE_NAME
import asyncio
currentversion = "ONLY ONE"

ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "🤠 Affetmez [offline] "
import os
xnkit786 = os.environ.get("PM_IMG", None)
if not xnkit786:
 xnkit786 = "https://te.legra.ph/file/f6bdfa9f59dd1f33984f1.jpg"
pm_caption = "• __Affetmez spammer online__\n\n"
pm_caption += "• __Python: 3.9.7__ \n"
pm_caption += "• __Database durumu:  Fonksiyonel__\n"
pm_caption += "• __Kurucu : `Affetmez`__\n"
pm_caption += f"• __Hizmet veriliyor_ : {ALIVE_NAME} \n"
pm_caption += "• __Heroku Databese : aws-working properly__\n\n"
pm_caption += "• __Copyright bγ : ©Zxr team__\n\n"
pm_caption += "• __İletişim__ : [Affetmez](https://t.me/affetmezzz)"


@worker.on(events.NewMessage(incoming=True, pattern="^/alive"))
async def alive(event):
  if not str(event.sender_id) in BOT_USERS:
    return await event.reply("Üzgünüm beni kullanacak yetkide değilsin")
  await worker.send_file(event.chat_id, xnkit786, caption=pm_caption) 
