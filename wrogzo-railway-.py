
# -*- coding: utf-8 -*-
import discord
import asyncio

# 7 bot tokeni ve kanal ID'leri
bot_configs = [
    {"token": "TOKEN1", "channel_id": 1375168637492658226},
    {"token": "TOKEN2", "channel_id": 1375168637492658226},
    {"token": "TOKEN3", "channel_id": 1375168637492658226},
    {"token": "TOKEN4", "channel_id": 1375168637492658226},
    {"token": "TOKEN5", "channel_id": 1375168637492658226},
    {"token": "TOKEN6", "channel_id": 1375168637492658226},
    {"token": "TOKEN7", "channel_id": 1375168637492658226},
]

clients = []

def create_bot(token, channel_id):
    intents = discord.Intents.default()
    intents.voice_states = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"🤖 Bot giriş yaptı: {client.user}")
        voice_channel = client.get_channel(channel_id)
        if voice_channel:
            try:
                await voice_channel.connect()
                print(f"🎧 Bağlandı: {voice_channel.name}")
            except Exception as e:
                print(f"⚠️ Bağlantı hatası: {e}")
        else:
            print("❌ Ses kanalı bulunamadı.")

    asyncio.create_task(client.start(token))
    clients.append(client)

async def main():
    for cfg in bot_configs:
        create_bot(cfg["token"], cfg["channel_id"])
    while True:
        await asyncio.sleep(60)

asyncio.run(main())
