import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("Project/GravityStarData.csv")

boolVal = []

for dis in df.Distance:
    if(dis<=100):
        boolVal.append(True)
    else:
        boolVal.append(False)

distance = pd.Series(boolVal)
star_dist = df[distance]
star_dist.reset_index(inplace=True, drop=True)

gravity_boolVal = []

for grv in star_dist.Gravity:
    if(grv<=350 and grv>=150):
        gravity_boolVal.append(True)
    else:
        gravity_boolVal.append(False)

gravity = pd.Series(gravity_boolVal)

finalStar = star_dist[gravity]
finalStar.reset_index(inplace=True, drop=True)
finalStar.to_csv("Project/StarsFiltered.csv")
print("Your new file with filtered star data is created...")