import json
import random
from enum import Enum
from dataclasses import dataclass
import time
import jsonpickle

class Element(Enum):
    SILLY = 1
    GRUMPY = 2
    SLEEPY = 3
    def __str__(self):
        match self:
            case Element.SILLY:
                return "<:silly:1070146370817769472> Silly <:silly:1070146370817769472>"
            case Element.GRUMPY:
                return "<:grumpy:1070146403868872704> Grumpy <:grumpy:1070146403868872704>"
            case Element.SLEEPY:
                return "<:eepy:1070146389570494585> Sleepy <:eepy:1070146389570494585>"

COMMON = 1
RARE = 2
EPIC = 3
LEGENDARY = 4
MYTHICAL = 5

class Unit:
    def __init__(self,name:str,url:str,rarity : int,element:Element) -> None:
        print("Unit created")
        self.name = name
        self.url = url
        self.rarity = rarity
        self.element = element

class User:
    def __init__(self,userid: str,units: list,lastRollUnix : int) -> None:
        self.userid = userid
        self.units = units
        self.lastRollUnix = lastRollUnix
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)




def loadBaileys():
    test = Unit("Bailey and Cait","https://cdn.discordapp.com/attachments/1039213143903182939/1068264038280204329/IMG_8402.jpg",MYTHICAL,Element.SILLY)
    baileys.append(test)
    baileys.append(Unit("Nosey Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068264970766266409/4B67D659-3DB6-4EE4-9477-6485374C51C6.jpg",RARE,Element.SILLY))
    baileys.append(Unit("Bedtime Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068264997337182228/5B180F00-BCA4-4124-AFA0-68C1E7E06ECD.jpg",RARE,Element.SLEEPY))
    baileys.append(Unit("Christmas Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265020053528597/24208FC2-DFC0-448B-8733-652BEE1AD099.jpg",EPIC,Element.SILLY))
    baileys.append(Unit("Halloween Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265097451012228/DAA9CB65-55AF-4560-8A56-5703E6B91AF6.jpg",LEGENDARY,Element.SILLY))
    baileys.append(Unit("Smug Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265141466054676/2616DEAF-B9FB-4F61-874A-C1BB05C06F20.jpg",COMMON,Element.GRUMPY))
    baileys.append(Unit("Soggy Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265176463323146/EEF3FD8C-10A1-4303-887D-D8BBB84C9C78.jpg",COMMON,Element.SILLY))
    baileys.append(Unit("Yawning Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265210013552670/756E505D-1D25-45CD-8F5D-8C0EDFBFA27C.jpg",RARE,Element.SLEEPY))
    baileys.append(Unit("Relaxing Bailey", "https://cdn.discordapp.com/attachments/1039213143903182939/1068265238174117918/5F2D938C-6E98-4DFF-B5F6-37133728220B.jpg",COMMON,Element.SLEEPY))
    baileys.append(Unit("Sideways Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265254687096982/A0473F56-A65D-47C8-B75A-2FEA3F912C1B.jpg",COMMON,Element.SILLY))
    baileys.append(Unit("Side eye Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265313105358899/5BE93BCC-C800-4CB2-8A59-AD17A06A4148.jpg",COMMON,Element.GRUMPY))
    baileys.append(Unit("Birds' eye Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265340557066310/70F096D0-CFCD-4F6E-9768-0D02B9B0CE01.jpg",RARE,Element.SILLY))
    baileys.append(Unit("Window Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265411990261790/8B69D8B6-5718-403E-AE0A-98116495BD74.jpg",COMMON,Element.SILLY))
    baileys.append(Unit("Pondering Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265411990261790/8B69D8B6-5718-403E-AE0A-98116495BD74.jpg",RARE,Element.SILLY))
    baileys.append(Unit("Chair Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265556567928863/1E4CBF09-F1FA-484F-8402-071C0F9164FE.jpg",EPIC,Element.SILLY))
    baileys.append(Unit("Garden Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265636180000871/74F933CC-52E5-428C-94C3-361D8C50D09B.jpg",RARE,Element.SILLY))
    baileys.append(Unit("Smug Bailey Plus","https://cdn.discordapp.com/attachments/1039213143903182939/1068265907085906042/AAFA29F9-2E28-4F98-9FA1-FECAE1E4723E.jpg",RARE,Element.GRUMPY))
    baileys.append(Unit("Sheep Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068265979144048700/EA21832A-E1AF-475B-BDFB-5CDDE4D6388E.jpg",EPIC,Element.SILLY))
    baileys.append(Unit("Blurry Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068266001952669776/5ECAF731-5848-433F-A1C4-199CF7ED0D8A.jpg",RARE,Element.SILLY))
    baileys.append(Unit("Super silly Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068266038057238548/18D0D61F-16CD-4A3E-A676-D092578347D8.jpg",EPIC,Element.SILLY))
    baileys.append(Unit("Closed Eye Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068266135511912569/D6A2E018-6A31-415C-9634-DEC1F2C304C7.jpg",LEGENDARY,Element.SLEEPY))
    baileys.append(Unit("Carried Bailey ft Mum","https://cdn.discordapp.com/attachments/1039213143903182939/1068266209046442105/DC18548B-BEFE-423F-88F8-B62D5D552D23.jpg",LEGENDARY,Element.SLEEPY))
    baileys.append(Unit("Idle Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068266294245339176/0933F032-32B5-4EBE-A461-FA825510FE2F.jpg",COMMON,Element.SLEEPY))
    baileys.append(Unit("Mid-Chew Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068266396515049512/9156F170-D6F2-4B01-AB27-D3277A878CA3.jpg",RARE,Element.SLEEPY))
    baileys.append(Unit("Foggy Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068298357367386284/327104651_869774834351906_8273537274965534988_n.png",COMMON,Element.SLEEPY))
    baileys.append(Unit("Eated the bees Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068298407740969102/327109592_5924233827635604_8473461490764313283_n.png",COMMON,Element.SLEEPY))
    baileys.append(Unit("Ghost Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068298663895502958/321910802_1408591113274077_2086779536172306200_n.png",MYTHICAL,Element.SLEEPY))
    baileys.append(Unit("Leaning Bailey ft Sam","https://cdn.discordapp.com/attachments/1039213143903182939/1068298794980085800/322464833_548204903874158_576126474742874050_n.png",RARE,Element.SLEEPY))
    baileys.append(Unit("Stinky Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1068298897245614160/321021612_952434979070030_8839148083040989088_n.png",LEGENDARY,Element.SLEEPY))
    baileys.append(Unit("What the hell is that Bailey","https://cdn.discordapp.com/attachments/1039213143903182939/1069567114458972210/IMG_8463.jpg",MYTHICAL,Element.GRUMPY))






def RollForBailey(userid : str) -> Unit | int:
    if userid not in users:
        users[userid] = User(userid,[],0)
    user = users[userid]
    lastRoll = user.lastRollUnix
    print(lastRoll)
    currentTime = int(time.time())
    if currentTime - lastRoll < 1800:
        return lastRoll + 1800
    user.lastRollUnix = currentTime
    num = random.randint(0,100)
    if num < 60:
        return GetRandomBaileyForRarity(COMMON)
    elif num < 80:
        return GetRandomBaileyForRarity(RARE)
    elif num < 88:
        return GetRandomBaileyForRarity(EPIC)
    elif num < 99:
        return GetRandomBaileyForRarity(LEGENDARY)
    else:
        ##mythical
        return GetRandomBaileyForRarity(MYTHICAL)


def GetRandomBaileyForRarity(rarity : int) -> Unit:
    list = []
    for i in baileys:
        if i.rarity == rarity:
            list.append(i)
    if len(list) == 0:
        return baileys[5]
    return list[random.randint(0,len(list) - 1)]


class Wrapper:
    def __init__(self):
        self.users = []

def WriteResultsToFile(users : dict):
    out = []
    for i in users:
        out.append(jsonpickle.encode(users[i]))

    wr = Wrapper()
    wr.users = out
    with open("results.txt","w") as f:
        f.write(jsonpickle.encode(wr))
        
def LoadResultsFromFile() -> dict:
    with open("results.txt","r") as f:
        newDict = {}
        wr = jsonpickle.decode(f.read())
        for i in wr.users:
            user = jsonpickle.decode(i)
            newDict.update({user.userid : user})
        return newDict


def AddBaileyToResults(bailey : Unit, user: str) -> None:
    if user not in users:
        users.update({user : User(user,[],time.time())})
    ##list = results[user]
    newUser = users[user]
    newUser.units.append(baileys.index(bailey))

def GetResults(user : str,page : int) -> str:
    if user in users:
        output = ""
        baileyList = users[user].units
        if(len(baileyList) % 5 == 0):
            pageCount = len(baileyList) / 5
        else:
            pageCount = (len(baileyList) // 5) + 1
        if page > pageCount or page < 1:
            return "Page " + str(page) + " does not exist!"

        output += "Page " + str(page) + " of " + str(pageCount) + "\n"

        for i in range((page - 1) * 5,min(page * 5,len(baileyList))):
            bailey = baileyList[i]
            output += baileys[bailey].name + "\n" + baileys[bailey].url + "\n"

        return output
    else:
        return "You dont have any baileys yet!"



@dataclass
class Turn:
    player: str
    bailey: Unit
    amount: int

def BattleBaileys(turn1 : Turn, turn2: Turn) -> Turn:
    ##TODO ADD MYTHICAL EFFECTS
    match turn1.bailey.element:
        case Element.SLEEPY:
            if turn2.bailey.element == Element.GRUMPY:
                return turn1
            elif turn2.bailey.element == Element.SLEEPY:
                if turn1.amount > turn2.amount:
                    return turn1
                elif turn1.amount == turn2.amount:
                    if random.choice([True,False]):
                        return turn1
                    else:
                        return turn2
                else:
                    return turn2
            else:
                return turn2
        case Element.GRUMPY:
            if turn2.bailey.element == Element.SLEEPY:
                return turn2
            elif turn2.bailey.element == Element.GRUMPY:
                if turn1.amount > turn2.amount:
                    return turn1
                elif turn1.amount == turn2.amount:
                    if random.choice([True,False]):
                        return turn1
                    else:
                        return turn2
                else:
                    return turn2
            else:
                return turn1
        case Element.SILLY:
            if turn2.bailey.element == Element.GRUMPY:
                return turn2
            elif turn2.bailey.element == Element.SILLY:
                if turn1.amount > turn2.amount:
                    return turn1
                elif turn1.amount == turn2.amount:
                    if random.choice([True,False]):
                        return turn1
                    else:
                        return turn2
                else:
                    return turn2
            else:
                return turn1



def GetRandomBaileyFromUser(user : str):
    if user not in users or len(users[user].units) == 0:
        return (baileys[5],1)
    userBaileys = users[user].units
    singleBaileyList = list(dict.fromkeys(users[user].units))
    unit = baileys[singleBaileyList[random.randint(0,len(singleBaileyList) - 1)]]
    amount = userBaileys.count(baileys.index(unit)) * unit.rarity
    return (unit,amount)


testUser = User("tmf#0001",[0],0)

users = {
    
}

###
##results = {
##    "tmf#0001" : [0]
##}
baileys = []
loadBaileys()
print("Baileys loaded")
print("Loading results from file")
users = LoadResultsFromFile()
print("Results loaded from file")
users.update({"tmf#0001" : testUser})
