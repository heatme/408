from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏᴀ! {}
━━━───⊶⛧•.𝘽ِ𝙞َ𝙇ِ𝙡𝙞ِ𝙚.•⛧⊷───━━━

🎻¦انا بوت تشغيل وتنزيل الاغاني والفديو

👮🏼‍♂️¦اضفني مشرف في مجموعتك لأعمل

🌐¦اتبع مايلي لمعرفه كيفيه الاستخدام

❓¦اضغط علي ذر طريقه الاستخدام

 ⚡️¦مميزات الروبوت يعمل بجودة فائقه

━━━───⊶⛧•.𝘽ِ𝙞َ𝙇ِ𝙡𝙞ِ𝙚.•⛧⊷───━━━
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ʙᴏᴛ ᴅᴇᴠ", "https://t.me/Y_408")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 ʙᴏᴛ ᴅᴇᴠ", "https://t.me/Y_408")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return
