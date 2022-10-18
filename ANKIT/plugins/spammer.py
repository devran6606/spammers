import asyncio
import os
from .. import worker, BOT_USERS, BOT_USER, LOGGER_GROUP
from asyncio import wait
from telethon import events
LOGGER_GROUP = int(os.environ.get("LOGGER_GROUP", None))
import re
abcd = "@affetmezzz|@BBZXR"
x = "@affetmezzz"
king = [1337863761]

@worker.on(events.NewMessage(incoming=True, pattern="/bigspam"))
async def bigspam(e):
  users = BOT_USERS
  if not str(e.sender_id) in users:
    return await e.reply("Üzgünüm beni kullanacak yetkide değilsin")
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
    await asyncio.sleep(0.01)
  if re.search(abcd.lower(), e.text.lower()):
    return await e.reply("Bu benim de sahibim Affetmez bu")
  if not e.text in abcd:
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#ʙɪɢsᴘᴀᴍ\n"
                        + f"Bigspam komutu başarıyla kullanıldı\n{(e.chat.title)} (`{e.chat_id}`)\n\n{counter} kez şu yazı tekrarlanacaktır => {e.text}",
                    )

@worker.on(events.NewMessage(incoming=True, pattern="/spam"))
async def spammer(e):
  users = BOT_USERS
  if not str(e.sender_id) in users:
    return await e.reply("Üzgünüm beni kullanacak yetkide değilsin")
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
    await asyncio.sleep(0.01)
  if re.search(abcd.lower(), e.text.lower()):
    return await e.reply("Bu benim de sahibim Affetmez bu")
  if not e.text in abcd:
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#sᴘᴀᴍ\n"
                        + f"Spam komutu başarıyla kullanıldı \n{(e.chat.title)} (`{e.chat_id}`)\n\n{counter} kez şu yazı tekrarlanacak => {e.text}",
                    )

@worker.on(events.NewMessage(incoming=True, pattern="/uspam"))
async def uspammer(e):
  if not str(e.sender_id) in BOT_USERS:
    return await e.reply("Üzgünüm beni kullanacak yetkide değilsin")
  if (abcd.lower()) in (e.text.lower()):
    return await e.reply("Bu benim de sahibim Affetmez bu")
  else:
      xD = e.text[7:]
      a = 1
      while a == 1:
        await e.client.send_message(e.chat, xD)
        await asyncio.sleep(1.95)

@worker.on(events.NewMessage(incoming=True, pattern="/mspam"))
async def tiny_pic_spam(e):
  if not str(e.sender_id) in BOT_USERS:
    return await e.reply("Üzgünüm beni kullanacak yetkide değilsin")
  if str(e.sender_id) in BOT_USERS:
    try:
      reply = await e.get_reply_message()
    except:
      await event.respond("bir şeyler ters gidiyor yanlış yapıyor olmalısın \nBir resim veya yazıyı etiketliceksin sonra /mspam <sayı>")
      return "offf siktir git"
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        media = await e.client.download_media(reply)
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, media)
        await e.delete()
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#ᴍᴇᴅɪᴀsᴘᴀᴍ\n"
                        + f"Media spam komutu başarıyla kullanıldı\n{(e.chat.title)} (`{e.chat_id}`)\n\n{counter} kez şu yazı tekrarlanacaktır => {e.text}",
                    )


@worker.on(events.NewMessage(incoming=True, pattern="/restart"))
async def restart(e):
  if not str(e.sender_id) in BOT_USERS:
    return await e.reply("Üzgünüm beni kullanacak yetkide değilsin")
  if str(e.sender_id) in BOT_USERS:
    try:
        text = "Yeniden Başlatılıyor ✨"
        await e.reply(text, parse_mode=None, link_preview=None)
        await worker.disconnect()
    except Exception:
        pass
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
