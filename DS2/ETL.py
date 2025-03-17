# Läs in "Matsvinn grundskola och gymnasium 2024.csv" och skriv ut de första raderna
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns

# Extract
df = pd.read_csv("Matsvinn grundskola och gymnasium 2024.csv")
# Kolla att det funkar
# print(df.head())


# Transform

# Ta bort eating kolumnen t.ex.
#df = df.drop(columns=['eating'])

# Kolla att det funkar
# print(df.to_string())

# Ta bort rader med NaN-värden
df = df.dropna(how='any', axis=0)

# Kolla att det funkar
# print(df.to_string())

# Rensa kolumner med NaN-värden
# Obs! Då finns ingenting kvar i dataframen
# df = df.dropna(how='all', axis=0)

# Kolla att det funkar
# print(df.to_string())

# Skapa en ny kolumn 'total' som är summan av 'serving', 'plate' och 'kitchen'
df['total'] = df['serving'] + df['plate'] + df['kitchen']

df.to_csv('Matsvinn grundskola och gymnasium 2024.csv', index=False)



# Sortera på datum
df = df.sort_values(by='date')

print(df.to_string())


# Gör om df['total'] till heltal
df['serving'] = df['serving'].astype(int)

# plt.plot(df['date'], df['serving'])
# Stapeldiagram
plt.bar(df['date'], df['total'])

plt.xlabel('Date')
plt.ylabel('Total')
plt.title('Total matsvinn per dag')
plt.show()


# Histogram för datafördelning för att visa hur datan är fördelad.
plt.figure(figsize=(10, 6))
sns.histplot(df['total'], bins=20, kde=True)
plt.title('Histogram för datafördelning')
plt.xlabel('Total serving')
plt.ylabel('Frekvens')
plt.show()
 
# Linjediagram för att visa trender över tid.
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='date', y='total', label='Total')
sns.lineplot(data=df, x='date', y='serving', label='serving')
plt.title('Linjediagram för att visa trender över tid')
plt.xlabel('År')
plt.ylabel('servering')
plt.legend()
plt.show()
 
 
# Scatter plot för att visa relationer mellan två variabler med årtal på varje punkt.
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='plate', y='kitchen')
plt.title('Scatter plot för att visa relationer mellan två variabler.')
plt.xlabel('plate')
plt.ylabel('kitchen')
plt.grid(True, color= 'black', linestyle='--', linewidth=0.5)
 

 
plt.show()

# Pie chart för fördelning av arbetslöshet mellan kvinnor och män
total_plate = df['plate'].sum()
total_kitchen = df['kitchen'].sum()
 
labels = ['Plate', 'Kitchen']
sizes = [total_plate, total_kitchen]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)
 
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.title('Fördelning på plate och kitchen')
plt.axis('equal')  
plt.show()
 

# Load
df.to_excel('Matsvinn-bearbetad.xlsx', index=False)

print("bearbetade datan har sparats till Matsvinn-bearbetad.xlsx")
print("Histogram visar hur datan är fördelad.")
print("Linjediagram visar trender över tid")
print("Scatter plot visar relationer mellan två variabler med en vis dag på varje punkt")
print("Pie chart visar fördelning på tallrikar och kök ")