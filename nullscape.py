import nbtlib
from nbtlib import *
from nbtlib.tag import *

datfile = nbtlib.load('./level.dat')
gateways = []
for i in range(0, 20):
    gateways.append(Int(i))

datfile.root['Data']['DragonFight']['PreviouslyKilled'] = Byte(0)
datfile.root['Data']['DragonFight']['DragonKilled'] = Byte(0)
datfile.root['Data']['DragonFight']['Gateways'] = List[Int](gateways)
datfile.save()