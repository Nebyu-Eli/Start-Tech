# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:32:17 2022

@author: hp
"""

from db7 import Database7
from db8 import Database8
import pandas as pd
df = pd.read_csv('IPL_Ball.csv')
df = df[:20]

df2 = pd.read_csv('IPL_Matches.csv')
#df2 = df2[:20]

data = Database7('Ball_to_ball.db')
data2 = Database8('Matches.db')

for i in range(20):
    data.insert(df.values.tolist()[i][0],df.values.tolist()[i][1],df.values.tolist()[i][2],df.values.tolist()[i][3],df.values.tolist()[i][4],df.values.tolist()[i][5],df.values.tolist()[i][6],df.values.tolist()[i][7],df.values.tolist()[i][8],df.values.tolist()[i][9],df.values.tolist()[i][10],df.values.tolist()[i][11],df.values.tolist()[i][12],df.values.tolist()[i][13],df.values.tolist()[i][14],df.values.tolist()[i][15],df.values.tolist()[i][16])
for i in range(816):
    data2.insert(df2.values.tolist()[i][0],df2.values.tolist()[i][1],df2.values.tolist()[i][2],df2.values.tolist()[i][3],df2.values.tolist()[i][4],df2.values.tolist()[i][5],df2.values.tolist()[i][6],df2.values.tolist()[i][7],df2.values.tolist()[i][8],df2.values.tolist()[i][9],df2.values.tolist()[i][10],df2.values.tolist()[i][11],df2.values.tolist()[i][12],df2.values.tolist()[i][13],df2.values.tolist()[i][14],df2.values.tolist()[i][15],df2.values.tolist()[i][16])
 
    
total_data = data2.fetch()
#Games played on 2nd may 2013
target_date = []
for i in range(len(total_data)):
    if total_data[i][3] == '02-05-2013':
        target_date.append(total_data[i])

print("Games played on 2nd may 2013 are: ")
for i in range(len(target_date)):
    print(target_date[i])

#margin of victory more than 100 runs
runs100 = []
for i in range(len(total_data)):
    if total_data[i][12] == 'runs' and int(total_data[i][13]) > 100:
        runs100.append(data2.fetch()[i])
        
print("Margin of victory more than 100 runs are: ")
for i in range(len(runs100)):
    print(runs100[i])

        
#Number of cities games were played in
cities = set()
for i in range(len(total_data)):
    cities.add(total_data[i][2])

cities = list(cities)
print("Number of cities to participate are: {} , and the cities are as follows:".format(len(cities)))
for i in range(len(cities)):
    print(cities[i])
