import requests
import discord
import asyncio

client = discord.Client()

def getUniverse(placeid):
    r = requests.get('https://api.roblox.com/universes/get-universe-containing-place?placeid=' + str(placeid))
    text = r.text.split(":")[1]
    placeid = text.rstrip(text[-1])

def getUsersAtUniverse(universeid):
    universeid = getUniverse(universeid)
    r = requests.get('https://games.roblox.com/v1/games?universeIds=' + str(universeid))
    playing = r.json()['data'][0]['playing']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-playercount'):
        channel01 = client.get_channel(899068023015632916)
        placeid = 1213026131
        r = requests.get('https://api.roblox.com/universes/get-universe-containing-place?placeid=' + str(placeid))
        text = r.text.split(":")[1]
        placeid = text.rstrip(text[-1])
        universeid = placeid
        r = requests.get('https://games.roblox.com/v1/games?universeIds=' + str(universeid))
        playing = r.json()['data'][0]['playing']
        embedVar = discord.Embed(title="Washington D.C. PlayerCount Systems", description=" ", color=0xFFFF00)
        embedVar.add_field(name="Players", value=str(playing), inline=False)
        embedVar.set_footer(icon_url="https://www.nsa.gov/Portals/70/images/about/cryptologic-heritage/center-cryptologic-history/insignia/nsa-insignia-lg.png", text="NSA Program - Coder: Zeltric#2518")
        message = await channel01.send(embed=embedVar)
        num = 0
        while (True):
            universeid = placeid
            r = requests.get('https://games.roblox.com/v1/games?universeIds=' + str(universeid))
            print(r.status_code)
            playing = r.json()['data'][0]['playing']
            embedVar = discord.Embed(title="Washington D.C. PlayerCount Systems", description=" ", color=0xFFFF00)
            embedVar.add_field(name="Players", value=str(playing), inline=False)
            embedVar.set_footer(icon_url="https://www.nsa.gov/Portals/70/images/about/cryptologic-heritage/center-cryptologic-history/insignia/nsa-insignia-lg.png", text="NSA Program - Coder: Zeltric#2518")
            await message.edit(embed=embedVar)
            await asyncio.sleep(60)





client.run('ODk5MDQxNjkyOTMyNTM4NDE4.YWs_0g.u8pZ_F8QepG4DgyY1Pnxea-URwg')
