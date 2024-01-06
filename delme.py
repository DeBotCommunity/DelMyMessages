# Module by @DeBotMod
# took from the userbot Hikka
from telethon import events

from userbot import client

info = {'category': 'chat', 'pattern': '.delme|.delmenow', 'description': 'удаляет все ваши сообщения|удаляет все ваши '
                                                                          'сообщения без вопросов'}


@client.on(events.NewMessage(pattern=r".delme", outgoing=True))
async def delme_command(event):
    chat = event.chat
    if chat:
        try:
            args = event.raw_text.split(' ')[1]
            if args != str(event.chat.id + event.sender_id):
                await event.edit(
                    f"**Если ты точно хочешь это сделать, то напиши:** ```.delme {event.chat.id+event.sender_id}```"
                )
                return
        except IndexError:

            await event.edit(
                f"**Вы уверены, что хотите удалить все свои сообщения?** "
                f"**Чтобы подтвердить, введите** ```.delme {event.chat.id+event.sender_id}```"
            )
            return

        await delete(chat, event, True)
    else:
        await event.edit("**Личку не очищаю!!**")


@client.on(events.NewMessage(pattern=r'.delmenow', outgoing=True))
async def delmenow_command(event):
    chat = event.chat
    if chat:
        await delete(chat, event, False)
    else:
        await event.edit("**Личку не очищаю!!**")


async def delete(chat, message, now):
    if now:
        all = (await message.client.get_messages(chat, from_user="me")).total
        await message.edit(f"**{all} сообщений будет удалено!**")
    else:
        await message.delete()
    _ = not now
    async for msg in message.client.iter_messages(chat, from_user="me"):
        if _:
            await msg.delete()
        else:
            _ = "_"
    (
        await message.delete()
        if now
        else "something strange "
    )
