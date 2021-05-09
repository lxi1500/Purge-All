import discord, asyncio

token = input("Insert token: ")

client = discord.Client(self_bot=True)





@client.event
async def on_ready():
  print(f"[STATUS] Logged into {client.user.name}")
  for i in client.private_channels:
    print(f"[STATUS] Purging {i.name}")
    await i.send("Purger made by lxi1500 on github xxx")
    await asyncio.sleep(3)
    async for message in i.history(limit=9999999):
        try:
            await message.delete()
            print(f"[STATUS] Deleted message {message.id}")
        except:
            continue      




client.run(token, bot=False)
