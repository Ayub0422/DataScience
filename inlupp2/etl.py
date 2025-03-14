import pandas as pd
import os


file_path = "C:\\Users\\ÄGARE\\Documents\\Data science\\inlupp2\\datamedservering.csv"
# os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv(file_path)
print(df)

Servering_per_skola = df.groupby('id')['serving'].sum().reset_index()
print(Servering_per_skola)
# df = pd.read_csv(min_mapp + "/matsvinn.csv")
 
 # Radera kolumn som saknade värden.

# df = df.drop(columns=['eating'])
#df = df.drop(columns=['plate', "kitchen", "eating"])
#print(df)

# print(df.isnull().values.any())


#print("drop")
#df = df.dropna()
#print(df)

Servering_per_skola.to_csv("servering_per_skola.csv", index=False)

