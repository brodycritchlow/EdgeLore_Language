from ListOfDirectoriesForAsunaAi import __FOLDER_PATH__
from ListOfDirectoriesForAsunaAi_2 import __PROGRAM_NAME__
from Pokemonarrayscript import *
from MasterScriptForte_Redone_2 import *
import pandas as pd
df = pd.read_excel (r'C:\ASUNAAI\EXTENSIONS\XLSX\TESTDATAFORPYTHONSCRIPT.xlsx', sheet_name='POKEMON000DATA')
a = df['POKEMON_NAME_LLR']
b = df['LOWERLEVELRANGE']
c = df['HIGHERLEVELRANGE']
d = df['ENCOUNTERPERCENTAGE']
e = df['TIME_OF_DAY']
f = df['SEASON_DATA']
g = df['ROUTE_NAME']
h = df['HABITAT_DEX_DATA']
print("Pokemon That Show Up At Day")
print (ROUTE,df.ROUTE_NAME[0],HAS,A,df.ENCOUNTERPERCENTAGE[2],CHANCE,TO,FIND,FLAAFFY,INSIDE,df.HABITAT_DEX_DATA[0],DURING,df.TIME_OF_DAY[0])
print (ROUTE,df.ROUTE_NAME[0],HAS,A,df.ENCOUNTERPERCENTAGE[1],CHANCE,TO,FIND,RATTATA,INSIDE,df.HABITAT_DEX_DATA[0],DURING,df.TIME_OF_DAY[0])
print (ROUTE,df.ROUTE_NAME[0],HAS,A,df.ENCOUNTERPERCENTAGE[3],CHANCE,TO,FIND,DEERLING,INSIDE,df.HABITAT_DEX_DATA[0],DURING,df.TIME_OF_DAY[0])
print("******************************************************************")
print("Pokemon That Show Up At Night")
print (ROUTE,df.ROUTE_NAME[0],HAS,A,df.ENCOUNTERPERCENTAGE[1],CHANCE,TO,FIND,RATICATE,INSIDE,df.HABITAT_DEX_DATA[0],DURING,df.TIME_OF_DAY[1])
print (ROUTE,df.ROUTE_NAME[0],HAS,A,df.ENCOUNTERPERCENTAGE[0],CHANCE,TO,FIND,SABLEYE,INSIDE,df.HABITAT_DEX_DATA[0],DURING,df.TIME_OF_DAY[1])
print (ROUTE,df.ROUTE_NAME[0],HAS,A,df.ENCOUNTERPERCENTAGE[2],CHANCE,TO,FIND,BELDUM,INSIDE,df.HABITAT_DEX_DATA[0],DURING,df.TIME_OF_DAY[1])





