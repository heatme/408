import os

from telethon import Button, events

from Zaid import *

IMG = os.environ.get(
    "PING_PIC", "https://te.legra.ph/file/c571e6fdb14b99d1e184a.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Y_408"
)

CAPTION = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@Zaid.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("⚜ Cԋαɳɳҽʅ ⚜", "https://t.me/TELEMEX")]]
    await Zaid.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
