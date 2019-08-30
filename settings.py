PLAYER = {'name':'', 'level':1, 'shipname':'', 'isk':1000}

STATUS = {'docked':True, 'sector':'Terran', 'station':'ISS'}

INV = ['i', 'like', 'ass']
C_ALL = [
'\n'
'?          List available commands',
'list       List specified items',
'quit       Quit game',
'player     List player details',
'station    Action involving some space station',
'scan       Scan the invironment',
'warp       Warp to a sector'
'status     View player status'
]
C_LIST = [
'\nstats      List stats of items',
'players    List players on server',
'inv        List inventory'
]
C_STATION1 = [
'\ndock       Dock at station',
'undock     Undock from station'
]
C_SECTORS=[
'\nSectors:    Threat Level',
'------------------------',
'Verran,     Level: 1', # Venus Sector
'Terran,     Level: 0.5', # Earth's Sector
'Martian,    Level: 1', # Mars's Sector
'Jupiter,    Level: 2.5', # Jupiter's sector
'Saturn,     Level: 5', # Saturn's Sector
'Chaos,      Level: 9' # Uranus's Sector
]

C_STATIONS=[
'Station:   '
'Ark        (UE Military Base)', # Venus Station
'UES        (United Earth Station)', # Earth's Station
'MESS       (Martian Empire Space Station)', # Mars's Station
'Jupiter    (Jupiter Colony)', # Jupiter's Station
'Themis     (Saturn Station)', # Saturn's Station
'Nyx    (Chaos Sector Station)' # Uranus's Sector
]

SHIPS={
'corvette':{'cost':1000000,'armor':1000}
}

SECTORS=[
'Verran', # Venus Sector
'Terran', # Earth's Sector
'Martian', # Mars's Sector
'Jupiter', # Jupiter's sector
'Saturn', # Saturn's Sector
'Chaos' # Uranus's Sector
]

ARMOR = 1000
SHIELD = 1000
