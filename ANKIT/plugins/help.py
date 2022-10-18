from . import *
from .. import worker, ALIVE_NAME
from telethon import events, Button


ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "Affetmez[offline]"

@worker.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    tatti=f"Spam Bot Kullanıcısı => {ALIVE_NAME} \nBu bot [Affetmez](t.me/affetmezzz) tarafından yapılmıştır"
    await event.reply(tatti,
                    buttons=[
                        [Button.inline("🌀 Yardım menüsü için tıkla",data="helpme")]
                    ])

@worker.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="Merhaba ben spam botu\nDatabase'de kayıtlı olan kullanıcılar beni kullanabilir\n\n Beni denemek için bir gruba alın"
    await event.edit(text,
                     buttons=[
                         [Button.inline("✨ Bilgi", data="lu")],
                         [Button.inline("✨ Komutlar", data="2")],
                         [Button.inline("✨ Kapat", data="3")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="2"))
async def ex(event):
    uuu="Komutlar hakkında bilgi almak için düğmelere dokun"
    await event.edit(uuu,
                     buttons=[
                         [Button.inline("🚨 spam", data="spam")],
                         [Button.inline("🚨 bigspam", data="bigspam")],
                         [Button.inline("🚨 uspam", data="uspam")],
                         [Button.inline("🚨 mspam", data="mspam")],
                         [Button.inline("⏪ Çıkış", data="helpme")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="3"))
async def ex(event):
    text3="Menü başarıyla kapatıldı"
    await event.edit(text3,
                     buttons=[
                         [Button.inline("Kolay gelsin", data="helpme")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="lu"))
async def ex(event):
    text4="Başka bilgiler"
    await event.edit(text4,
                     buttons=[
                         [Button.url("Telegram grubumuz", url="https://t.me/bbzxrchat")],
                         [Button.url("Telegram", url="https://t.me/affetmezzz")],
                         [Button.inline("Çıkış", data="helpme")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="spam"))
async def ex(event):
    texi="➽ /spam <numara> <yazı> \nMaksimum /spam 99 selam"
    await event.edit(texi,
                     buttons=[
                         [Button.inline("⬅️ Geri", data="2")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="bigspam"))
async def ex(event):
    tut="➽ /bigspam <numara> <yazı> \nMinimum /bigspam 101 yazı \nMaksimum /bigspam 9999 yazı"
    await event.edit(tut,
                     buttons=[
                         [Button.inline("⬅️ Geri", data="2")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="uspam"))
async def ex(event):
    tempu="➽ /uspam <yazı> \nLimit yok\nDurdurmak için => /restart "
    await event.edit(tempu,
                     buttons=[
                         [Button.inline("⬅️ Geri", data="2")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="mspam"))
async def ex(event):
    achdh="➽ Herhangi Bir Medya & Dosyayı Yanıtlayın /mspam <sayı> \n Limit sayıya bağlı \nDurdurmak için => /restart"
    await event.edit(achdh,
                     buttons=[
                         [Button.inline("⬅️ Geri", data="2")]
                     ])
