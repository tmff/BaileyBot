import discord
import time
import gacha
import atexit
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime
from dataclasses import dataclass


class SimpleView(discord.ui.View):

    @discord.ui.button(label=":arrow_left:",style=discord.ButtonStyle.success)
    async def left(self, interaction : discord.Interaction, button : discord.ui.Button):
        await interaction.response.send_message("Woof Woof!", ephemeral=True)

def run():
    intents = discord.Intents.all()
    ##client = discord.Client(command_prefix='!', intents=intents)
    client = commands.Bot(command_prefix='!', intents=intents) 

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
    
    @client.event
    async def on_message(ctx):
        await client.process_commands(ctx)


        
    @client.command()
    async def bc(ctx):
        user = ctx.author
        splitArray = ctx.message.content.split(' ')
        try:
            page = int(splitArray[1])
        except:
            page = 1
        await ctx.reply(gacha.GetResults(str(user),page))

    @client.command()
    async def baileycollection(ctx):
        user = ctx.author
        splitArray = ctx.message.content.split(' ')
        try:
            page = int(splitArray[1])
        except:
            page = 1
        await ctx.reply(gacha.GetResults(str(user),page))

    @client.command()
    async def b(message):
        user = message.author
        
        print(user)
        await message.reply('Rolling for Bailey!')
        ctx = await message.reply(":)")
        ##do roll
        bailey = gacha.RollForBailey(str(user))
        if type(bailey) is int:
            await ctx.edit(content="You have already rolled for a bailey this hour!, please wait until " + datetime.utcfromtimestamp(bailey).strftime('%Y-%m-%d %H:%M:%S'))
            return
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

    @client.command()
    async def baileyBattle(ctx):
        user = ctx.author
        if user in pendingBattles:
            for i in ongoingBattles:
                if i.player1 == user or i.player2 == user:
                    await ctx.reply("You are already in a battle!")
                    return
            await ctx.reply("You already have a pending battle request! Please cancel it with !cancelBattle")
            return
        if(ctx.message.mentions[0] == user):
            await ctx.reply("You can't battle yourself!")
            return
        if len(ctx.message.mentions) == 0:
            await ctx.reply("Please mention a user to battle!")
            return
        userToBattle = ctx.message.mentions[0]
        pendingBattles.update({str(user):str(userToBattle)})
        await ctx.reply("Battle request sent to " + str(userToBattle) + "!")

    @client.command()
    async def cancelPendingBattle(message):
        user = message.author
        pendingBattles.pop(str(user))
        await message.reply("Battle request cancelled!")
        

    @client.command()
    async def acceptBattle(ctx):
        user = ctx.author
        userWithRequest = ctx.message.mentions[0]
        if len(ctx.message.mentions) == 0:
            await ctx.reply("Please mention a user to battle!")
            return
        if str(userWithRequest) in pendingBattles:
            if pendingBattles[str(userWithRequest)] == str(user):
                player1 = user
                player2 = userWithRequest
                await ctx.reply("Battle accepted!")
                await ctx.channel.send("Battle between " + str(user) + " and " + str(userWithRequest) + " is starting!")
                await ctx.channel.send("Bailey bot will each send you a dm with your hand, select a card to play by selecting the corresponding number! Once both players have sent their cards, the round will commence! first to 3 wins!")
                await ctx.channel.send("https://cdn.discordapp.com/attachments/1039213143903182939/1070143487514771486/IMG_2357.jpg")
                player1Hand = []
                player2Hand = []
                for i in range(0,7):
                    unit1 = gacha.GetRandomBaileyFromUser(str(player1))
                    unit2 = gacha.GetRandomBaileyFromUser(str(player2))
                    await player1.send(str(i + 1) + ": " + unit1[0].name + "\nPower: " + str(unit1[1])+" Element:" + str(unit1[0].element) + " \n"+ unit1[0].url)
                    await player2.send(str(i + 1) + ": " + unit2[0].name + "\nPower: " + str(unit2[1])+" Element:" + str(unit2[0].element) + " \n"+ unit2[0].url)
                    player1Hand.append(unit1)
                    player2Hand.append(unit2)
                battle = Battle(player1,player2,ctx.channel)
                battle.player1Hand = player1Hand
                battle.player2Hand = player2Hand
                battle.canChoose = True
                ongoingBattles.update({battle.player1:battle})
                ongoingBattles.update({battle.player2:battle})
                await player1.send("Please select a card to play by typing !choose [number]")
                await player2.send("Please select a card to play by typing !choose [number]")
            else:
                await ctx.reply("That user didn't send you a battle request!")
        else:
            await ctx.reply("That user didn't send you a battle request!")

    async def roundStart(battle):
        time.sleep(3)
        await battle.channel.send("Round " + str(battle.player1Points + battle.player2Points + 1) + " starting!")
        battle.player1Choice = -1
        battle.player2Choice = -1
        await battle.player1.send("Please select a card to play by typing !choose [number]")
        await battle.player2.send("Please select a card to play by typing !choose [number]")
        battle.canChoose = True



    @client.command()
    async def choose(ctx):
        if ctx.author not in ongoingBattles:
            await ctx.reply("You are not in a battle!")
            return
        i = ongoingBattles[ctx.author]
        if i.canChoose == False:
            return
        if ctx.author == i.player1:
            val = -1
            try:
                val = int(ctx.message.content.split(' ')[1])
            except:
                await i.player1.send("Please enter a valid number!")
                return
            if val > 7 or val < 1:
                await i.player1.send("Please enter a number less than 8 and greater than 1!")
                return
            if val in i.player1UsedCards:
                await i.player1.send("You have already used that card!")
                return
            i.player1UsedCards.append(val)
            i.player1Choice = val
        elif ctx.author == i.player2:
            val = -1
            try:
                val = int(ctx.message.content.split(' ')[1])
            except:
                await i.player2.send("Please enter a valid number!")
                return
            if val > 7 or val < 1:
                await i.player2.send("Please enter a number less than 8 and greater than 1!")
                return
            if val in i.player2UsedCards:
                await i.player2.send("You have already used that card!")
                return
            i.player2UsedCards.append(val)
            i.player2Choice = val
        if i.player1Choice != -1 and i.player2Choice != -1:
            print("Player 1 Chosen Cards: " + str(i.player1UsedCards))
            print("Player 2 Chosen Cards: " + str(i.player2UsedCards))
            await handleBattle(i)
        else:
            await ctx.reply("Waiting for other player to make a choice...")
            return

    async def handleBattle(battle):
        battle.canChoose = False
        await battle.channel.send("Both players have chosen their cards!")
        temp = battle.player1Hand[battle.player1Choice - 1]
        turn1 = gacha.Turn(battle.player1,temp[0],temp[1])
        temp = battle.player2Hand[battle.player2Choice - 1]
        turn2 = gacha.Turn(battle.player2,temp[0],temp[1])
        
        await battle.channel.send(str(turn1.player) + " played " + str(turn1.bailey.name) + " with power " + str(turn1.amount) + "\n " + turn1.bailey.url)
        await battle.channel.send(str(turn2.player) + " played " + str(turn2.bailey.name) + " with power " + str(turn2.amount) + "\n " + turn2.bailey.url)

        match turn1.bailey.element:
            case gacha.Element.SLEEPY:
                if turn2.bailey.element == gacha.Element.SLEEPY:
                    await battle.channel.send("Both players played sleepy cards!")
                    if turn1.amount > turn2.amount:
                        await battle.channel.send(turn1.bailey.name + " is more sleepy than " + turn2.bailey.name + "!")
                    else:
                        await battle.channel.send(turn2.bailey.name + " is more sleepy than " + turn1.bailey.name + "!")
                elif turn2.bailey.element == gacha.Element.SILLY:
                    await battle.channel.send(turn2.bailey.name + " is too silly to be sleepy!")
                elif turn2.bailey.element == gacha.Element.GRUMPY:
                    await battle.channel.send(turn1.bailey.name + " is too sleepy to be grumpy!")
            case gacha.Element.SILLY:
                if turn2.bailey.element == gacha.Element.SILLY:
                    await battle.channel.send("Both players played silly cards!")
                    if turn1.amount > turn2.amount:
                        await battle.channel.send(turn1.bailey.name + " is more silly than " + turn2.bailey.name + "!")
                    else:
                        await battle.channel.send(turn2.bailey.name + " is more silly than " + turn1.bailey.name + "!")
                elif turn2.bailey.element == gacha.Element.GRUMPY:
                    await battle.channel.send(turn2.bailey.name + " is too grumpy to be silly!")
                elif turn2.bailey.element == gacha.Element.SLEEPY:
                    await battle.channel.send(turn1.bailey.name + " is too silly to be sleepy!")
            case gacha.Element.GRUMPY:
                if turn2.bailey.element == gacha.Element.GRUMPY:
                    await battle.channel.send("Both players played grumpy cards!")
                    if turn1.amount > turn2.amount:
                        await battle.channel.send(turn1.bailey.name + " is more grumpy than " + turn2.bailey.name + "!")
                    else:
                        await battle.channel.send(turn2.bailey.name + " is more grumpy than " + turn1.bailey.name + "!")
                elif turn2.bailey.element == gacha.Element.SLEEPY:
                    await battle.channel.send(turn2.bailey.name + " is too sleepy to be grumpy!")
                elif turn2.bailey.element == gacha.Element.SILLY:
                    await battle.channel.send(turn1.bailey.name + " is too grumpy to be silly!")

        time.sleep(2)
        winner = gacha.BattleBaileys(turn1,turn2)
        print(str(winner.player))
        await battle.channel.send(str(winner.player) + " won the round!")
        if winner.player == battle.player1:
            battle.player1Points += 1
            if battle.player1Points == 3:
                await battle.channel.send(str(battle.player1) + " won the battle!")

                ongoingBattles.pop(battle.player1)
                ongoingBattles.pop(battle.player2)
                return
        else:
            battle.player2Points += 1
            if battle.player2Points == 3:
                await battle.channel.send(str(battle.player2) + " won the battle!")

                ongoingBattles.pop(battle.player1)
                ongoingBattles.pop(battle.player2)

                return
        await roundStart(battle)

    @client.command()
    async def cancelBattle(ctx):
        if ctx.author in ongoingBattles:
            await ctx.reply("Battle cancelled!")
            battle = ongoingBattles[ctx.author]
            ongoingBattles.pop(battle.player1)
            ongoingBattles.pop(battle.player2)
            return
        await ctx.reply("You are not in a battle!")
        

                
        

    load_dotenv()
    client.run(os.getenv("TOKEN"))



class Battle:
    def __init__(self, player1, player2, channel):
        self.player1 = player1
        self.player2 = player2
        self.channel = channel
        self.player1Points = 0
        self.player2Points = 0
        self.player1Hand = []
        self.player2Hand = []
        self.player1UsedCards = []
        self.player2UsedCards = []
        self.player1Choice = -1
        self.player2Choice = -1
        self.canChoose = False

pendingBattles = {}

ongoingBattles = {}



def getUserFromMention(mention):
    if mention.startswith('<@') and mention.endswith('>'):
        mention = mention[2:-1]
        if mention.startswith('!'):
            mention = mention[1:]
        return mention

def exit_handler():
    print("Writing results to file")
    gacha.WriteResultsToFile(gacha.users)
    print("Done writing results to file")
    print("Exiting")

if __name__ == "__main__":
    atexit.register(exit_handler)
    run()
##client.run(TOKEN)



