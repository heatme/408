from telethon import events, Button
from Zaid import Zaid, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("ادمن", data="admin"), Button.inline("اوامر الطرد", data="bans")],
    [Button.inline("اوامر تثبيت الرسائل", data="pins"), Button.inline("اوامر حذف الرسائل", data="purges")],
    [Button.inline("اوامر التشغيل", data="play"), Button.inline("اوامر المحذوفين", data="zombies")],
    [Button.inline("اوامر الدردشة", data="locks"), Button.inline("اوامر الايدي", data="misc")],
    [Button.inline("الرئيسيه", data="start")]]

HELP_TEXT = "مرحبا بك في قائمة الاوامر\n\n انقر علي الأزرار!"


@Zaid.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply("تواصل معي في المساء للحصول على قائمة المساعدة المتاحة!", buttons=[
       [Button.url("اوامر البوت!", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.NewMessage(pattern="^/start help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT, buttons=btn)
