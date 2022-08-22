from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
import time
from Config import Config

PR_HELP = """
**✘ هل تحتاج إلى حذف الكثير من الرسائل؟ هذا هو سبب التطهير!**

‣ `/purge` × قم بالرد على رسالة لحذف الرسائل من هناك.
‣ `/spurge` × مثل التطهير ، لكن لا يرسل رسالة التأكيد النهائية.
‣ `/del` × يحذف الرد على الرسالة.
"""

@Zaid.on(events.NewMessage(pattern=r"^[?!]purge"))
@is_admin
async def purge_messages(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.delete_messages:
         await event.reply("You are missing the following rights to use this command:CanDelMsgs!")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "Reply to a message to select where to start purging from.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"Purged in {time_:0.2f} Second(s)"
    await event.respond(text, parse_mode='markdown')

@Zaid.on(events.NewMessage(pattern="^[!?/]spurge"))
@is_admin
async def spurge(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.delete_messages:
         await event.reply("You are missing the following rights to use this command:CanDelMsgs!")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "Reply to a message to select where to start purging from.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)

@Zaid.on(events.NewMessage(pattern="^[!?/]del$"))
@is_admin
async def delete_messages(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.delete_messages:
       await event.reply("You are missing the following rights to use this command:CanDelMsgs!")
       return
    msg = await event.get_reply_message()
    if not msg:
      await event.reply("Reply to a msg to delete it.")
      return

    await msg.delete()
    await event.delete()

@Zaid.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])
