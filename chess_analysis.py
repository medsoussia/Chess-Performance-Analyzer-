"""
Chess Performance Analyzer
Author: Mohamed Ben Soussia
Description: Analyze my monthly chess ratings using pandas and matplotlib.
"""


import pandas as pd
import matplotlib.pyplot as plt

data = {
    "month": ["Mai", "Jun", "Juillet", "Aout", "Sep", "Oct", "Nov", "Dec", "Janv"],

    "rapid":  [1350, 1400, 1450, 1500, 1550, 1600, 1650, 1680, 1720],
    "blitz":  [1450, 1480, 1500, 1520, 1580, 1620, 1660, 1700, 1730],
    "bullet": [1250, 1280, 1300, 1350, 1380, 1400, 1420, 1450, 1480],

    "games":  [30, 45, 50, 60, 55, 70, 80, 65, 75]
}
df=pd.DataFrame(data)
print("\n the first 5 rowws is :")
print(df.head())
print("\n average rapid rating = ")
print(df['rapid'].mean())
print("\n highest blitz rating = ")
print(df['blitz'].max())
print("\n total games played = ")
print(df['games'].sum())
df['total_rating']=df["blitz"]+df["rapid"]+df['bullet']
df['games_per_rating']=df['games'] / df['total_rating']
print("\n the new dataframe is :")
print(df)
print("\n months with games > 60 :")
print(df[df['games'] > 60])
print(df.sort_values('total_rating', ascending=False))
print("\n month with the highest total_rating is :")
print(df[df['total_rating']==df['total_rating'].max()])
df['rapid_growth']=df['rapid'].diff()
df['blitz_growth']=df['blitz'].diff()
print("\n the new dataframe is : ")
print(df)
df['rapid_avg_3'] = df['rapid'].rolling(3).mean()
print(df)
best_month =df.loc[ df['total_rating'].idxmax() ]
worst_month =df.loc[ df['total_rating'].idxmin() ]
print("\n the best month is :")
print(best_month)
print("\n the worst month is : ")
print(worst_month)



#  LINE PLOT 
plt.figure(figsize=(10,6))

plt.plot(df['month'], df['rapid'], marker='o', label='Rapid')
plt.plot(df['month'], df['blitz'], marker='o', label='Blitz')
plt.plot(df['month'], df['rapid_avg_3'], linestyle='--', label='Rapid Trend (3M avg)')

plt.xlabel("Month")
plt.ylabel("Rating")
plt.title("Chess Rating Growth Dashboard")
plt.legend()
plt.grid()

plt.savefig("chess_dashboard.png")
plt.show()


#  BAR CHART 
plt.figure(figsize=(8,5))

plt.bar(df['month'], df['games'])

plt.xlabel("Month")
plt.ylabel("Games Played")
plt.title("Games Played Per Month")

plt.savefig("games_bar.png")
plt.show()


#  HISTOGRAM 
plt.figure(figsize=(8,5))

plt.hist(df['rapid'], bins=5)

plt.xlabel("Rapid Rating")
plt.ylabel("Frequency")
plt.title("Rapid Rating Distribution")

plt.savefig("rapid_hist.png")
plt.show()
