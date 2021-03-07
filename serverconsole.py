import sys
import os.path
import json
import time

def openIfExists(name):
    if os.path.isfile(name):
        f = open(name, 'r')
        return json.load(f)
    else:
        return {}

oped = openIfExists('oped-players.json')
banned = openIfExists('banned-players.json')
whitelist = openIfExists('whitelist.json')
world = openIfExists("world.json")

def readPoint(position):
    (x,y,z) = position
    if(y <= 0): 
        return "bedrock"
    if(not (str(position) in world)):
        return "air"
    return world[str(position)]

def theEnd():
    f = open('oped-players.json', 'w')
    json.dump(oped, f)
    f.close()

    f = open('banned-players.json', 'w')
    json.dump(banned, f)
    f.close()

    f = open('whitelist.json', 'w')
    json.dump(whitelist, f)
    f.close()


    f = open('world.json', 'w')
    json.dump(world, f)
    f.close()



print("Loading server console")
time.sleep(.2)
print("Loading terrain generation")
time.sleep(4)
print('done')
time.sleep(.98)
print("> ", end=" ", flush=True);
for line in sys.stdin:
    command = line.split()
    if len(command) == 0:
        print('invalid command, use ? or help for a list of commands')
        continue
    if command[0] == "stop":
        theEnd()
        exit()
    if command[0] == "op":
        print("opped " + command[1])
        oped[command[1]] = { 'name' : command[1], 'level': 4, 'bypassesPlayerLimit':False }
    if command[0] == "deop":
        del oped[command[1]]
        print("deopped " + command[1])
    if command[0] == "ban":
        what = ""
        for word in command[2:]:
            what += " " + word
        banned[command[1]] = { 'name' : command[1], 'reason' : what, 'due-by' : None, 'active' : True}
        print("banned " + command[1] + " for: " + what)
    if command[0] == "pardon":
        del banned[command[1]]
        print("Pardoned " + command[1])
    if command[0] == "give":
        print("gave " + command[1] + " " + command[2] + "*" + command[3])
    if command[0] == "setblock":
        world[str((command[1],command[2],command[3]))] = command[4]
        print("Set the block at " + command[1] + " " + command[2] + " " + command[3] + " to " + command[4])
    if command[0] == "banlist":
        print('Banned Players:[')
        for player in banned:
            print("   " + player + " for:'" + banned[player]['reason'].lstrip() + "'")
        print(']')
    print("> ", end=" ", flush=True);
#variables
#d = int(3)
#r = "py is amazing"
#playername = str(null)