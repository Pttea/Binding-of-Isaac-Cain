from collections import Counter

activeList=[]
passiveList=[]

pickupDict = {
    "1": "Red heart",
    "2": "Soul heart",
    "3": "Black heart",
    "4": "Eternal",
    "5": "Gold heart",
    "6": "Bone heart",
    "7": "Rotten heart",
    "8": "Penny",
    "9": "Nickle",
    "10": "Dime",
    "11": "Lucky penny",
    "12": "Key",
    "13": "Golden key",
    "14": "Charged Key",
    "15": "Bomb",
    "16": "Golden bomb",
    "17": "Giga bomb",
    "18": "Micro battery",
    "19": "Lil' battery",
    "20": "Mega battery",
    "21": "Card",
    "22": "Pill",
    "23": "Rune",
    "24": "Dice Shard",
    "25": "Cracked Key",
}


class ActiveItem:
    def __init__(self, name, id, recipe1, recipe2, recipe3, recipe4):
        self.name = name
        self.id = id
        self.recipe1 = recipe1
        self.recipe2 = recipe2
        self.recipe3 = recipe3
        self.recipe4 = recipe4

    def __str__(self):
        return f"{self.name}"

class PassiveItem:
    def __init__(self, name, id, recipe1, recipe2, recipe3, recipe4):
        self.name = name
        self.id = id
        self.recipe1 = recipe1
        self.recipe2 = recipe2
        self.recipe3 = recipe3
        self.recipe4 = recipe4

    def __str__(self):
        return f"{self.name}"
    


import itertools as it
filename='ActiveCollectibles.txt'
with open(filename, 'r') as f:
    for key, group in it.groupby(f, lambda line: line.startswith(' | {{i|')):
        if not key:
            group = list(group)
            del group[-1]
            group[0] = group[0][:-3]
            group[1] = int(group[1][3:-1])
            group[2] = [int(x) for x in group[2][28:-3].split("|")]
            group[3] = [int(x) for x in group[3][28:-3].split("|")]
            group[4] = [int(x) for x in group[4][28:-3].split("|")]
            group[5] = [int(x) for x in group[5][28:-3].split("|")]
            for i in range(2,6):
                group[i].sort()
            activeList.append(ActiveItem(group[0],group[1],group[2],group[3],group[4],group[5]))
            


filename2='PassiveCollectibles.txt'
with open(filename2, 'r') as f:
    for key, group in it.groupby(f, lambda line: line.startswith(' | {{i|')):
        if not key:
            group = list(group)
            del group[-1]
            group[0] = group[0][:-3]
            group[1] = int(group[1][3:-1])
            group[2] = [int(x) for x in group[2][28:-3].split("|")]
            group[3] = [int(x) for x in group[3][28:-3].split("|")]
            group[4] = [int(x) for x in group[4][28:-3].split("|")]
            group[5] = [int(x) for x in group[5][28:-3].split("|")]
            for i in range(2,6):
                group[i].sort()
            passiveList.append(PassiveItem(group[0],group[1],group[2],group[3],group[4],group[5]))
            

def pickupSwap(recipe):
    for i in range(len(recipe)):
        string = str(recipe[i])
        recipe[i] = pickupDict[string]

def get_recipe(lst, id):
    for i in range(len(lst)):
        if lst[i].id == id:
            pickupSwap(lst[i].recipe1)
            pickupSwap(lst[i].recipe2)
            pickupSwap(lst[i].recipe3)
            pickupSwap(lst[i].recipe4)
            return print(f"{lst[i].name} has an item recipe of \n {lst[i].recipe1} \n {lst[i].recipe2} \n {lst[i].recipe3} \n {lst[i].recipe4}")
        else:
            continue
    return f"{user_input} is not a valid item id"



def filter(lst, user_input):
    craft = []
    for i in range(len(lst)):
        recipe = []
        if not Counter(user_input) - Counter(lst[i].recipe1):
            pickupSwap(lst[i].recipe1) 
            recipe.append(lst[i].name)
            recipe.append(lst[i].recipe1)
            craft.append(recipe)
        elif not Counter(user_input) - Counter(lst[i].recipe2):
            pickupSwap(lst[i].recipe2) 
            recipe.append(lst[i].name)
            recipe.append(lst[i].recipe2)
            craft.append(recipe)
        elif not Counter(user_input) - Counter(lst[i].recipe3):
            pickupSwap(lst[i].recipe3) 
            recipe.append(lst[i].name)
            recipe.append(lst[i].recipe3)
            craft.append(recipe)
        elif not Counter(user_input) - Counter(lst[i].recipe4):
            pickupSwap(lst[i].recipe4) 
            recipe.append(lst[i].name)
            recipe.append(lst[i].recipe4)
            craft.append(recipe)
        else:
            continue
    print(f"You can craft {len(craft)} items")
    return print(*craft, sep= "\n")

def youCanMake(lst, user_input):
    craft = []
    for i in range(len(lst)):
        recipe = []
        if not Counter(lst[i].recipe1) - Counter(user_input):
            pickupSwap(lst[i].recipe1) 
            recipe.append(lst[i].name)
            recipe.append(lst[i].id)
            recipe.append(lst[i].recipe1)
            craft.append(recipe)
        elif not Counter(lst[i].recipe2) - Counter(user_input):
            pickupSwap(lst[i].recipe2) 
            recipe.append(lst[i].name)
            recipe.append(lst[i].id)
            recipe.append(lst[i].recipe2)
            craft.append(recipe)
        elif not Counter(lst[i].recipe3) - Counter(user_input):
            pickupSwap(lst[i].recipe3) 
            recipe.append(lst[i].name)
            recipe.append(lst[i].id)
            recipe.append(lst[i].recipe3)
            craft.append(recipe)
        elif not Counter(lst[i].recipe4) - Counter(user_input):
            pickupSwap(lst[i].recipe4) 
            recipe.append(lst[i].name)
            recipe.append(lst[i].id)
            recipe.append(lst[i].recipe4)
            craft.append(recipe)
        else:
            continue
    print(f"You can craft {len(craft)} items")
    return print(*craft, sep= "\n")



#filter(passiveList, [14])

my_pickups =[1,1,1,6,8,8,8,8,8,8,12,12,12,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,16,21,22]

youCanMake(passiveList,my_pickups)


'''
get_recipe(passiveList, 619)
get_recipe(passiveList, 463)
get_recipe(passiveList, 64)
'''
'''
['Sacrificial Dagger', 172, ['Red heart', 'Red heart', 'Soul heart', 'Soul heart', 'Nickle', 'Key', 'Bomb', 'Pill']]
['Divorce Papers', 547, ['Red heart', 'Red heart', 'Red heart', 'Penny', 'Penny', 'Penny', 'Key', 'Bomb']]
['Schoolbag', 534, ['Red heart', 'Soul heart', 'Soul heart', 'Nickle', 'Key', 'Bomb', 'Bomb', 'Pill']]
['Bot Fly', 629, ['Soul heart', 'Soul heart', 'Penny', 'Nickle', 'Key', 'Bomb', 'Bomb', 'Pill']]
['Box', 198, ['Red heart', 'Red heart', 'Red heart', 'Red heart', 'Penny', 'Penny', 'Bomb', 'Bomb']]
['Treasure Map', 54, ['Red heart', 'Red heart', 'Red heart', 'Red heart', 'Red heart', 'Red heart', 'Penny', 'Nickle']]
'''