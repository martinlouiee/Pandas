import pandas as pd
cars=pd.read_csv('cars.csv')

top=cars.loc[0:5]
bottom=cars.loc[27:32]
result=pd.concat([top,bottom])

print(result)



