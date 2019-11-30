import pandas as pd
cars=pd.read_csv('cars.csv')

#2a
x=cars.loc[0:5,0::2]
print(x)

#2B
mazda=cars.iloc[[0]]
print(mazda)


#2C
camaro=cars.loc[[23],['cyl']]
print(camaro)

#2D
mazhonford=cars.loc[[1,18,28],['Model','cyl','gear']]
print(mazhonford)



