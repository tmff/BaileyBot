import discord
import time
import gacha
import atexit

TOKEN = "MTA2ODI2NzYyMDU3MjM1MjY2NA.GeO9kX.lycuaidGCsDGL3vB_z3CNOIF20txGGGB3GSVsc"
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content == "!bailey" or message.content== '!b':
        user = message.author
        print(user)
        await message.reply('Rolling for Bailey!')
        ctx = await message.reply(":)")
        ##do roll
        bailey = gacha.RollForBailey()
        star = ''
        for i in range(0,bailey.rarity):
            if i > 3:
                time.sleep(1)
            star += ':star:'
            await ctx.edit(content=star)
            time.sleep(0.3 + i * 0.1)
        time.sleep(0.5)
        await message.reply(bailey.url)
        time.sleep(0.25)
        match (bailey.rarity):
            case gacha.COMMON:
                await message.reply(content='eh, nothing special. you got the common ' + bailey.name)
            case gacha.RARE:
                await message.reply(content='hmm. this one will look nice in your collection. you got the rare ' + bailey.name)
            case gacha.EPIC:
                await message.reply(content='oh my bailey! this bailey is quite hard to come by! you got epic ' + bailey.name + '!')
            case gacha.LEGENDARY:
                await message.reply(content="HOLY SHIT!!! THIS ONE'S SUPER DUPER RARE! YOU GOT legendary " + bailey.name + '!')
            case gacha.MYTHICAL:
                await message.reply(content="Oh my gosh!!!!!!!! I can't believe it...? the rarest bailey EVER????? you got the MYTHICAL " + bailey.name + '!')
        gacha.AddBaileyToResults(bailey,str(user))
    if message.content == '!bc' or message.content == '!baileycollection':
        user = message.author
        await message.reply(gacha.GetResults(str(user)))
 

def exit_handler():
    print("Writing results to file")
    gacha.WriteResultsToFile(gacha.results)
    print("Done writing results to file")
    print("Exiting")

atexit.register(exit_handler)
client.run(TOKEN)



