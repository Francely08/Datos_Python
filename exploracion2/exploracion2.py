from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('avocado.csv')
data.fillna(0,inplace=True)

#obtener el número de filas y columnas
print(data.shape)

#obtener los primeros 100 regitros
print(data.head(100))

#obtener los ultimos 20 registros
print(data.tail(20))

print(data.describe())

#obtener el minimo
print(data.min())

#obtenr el maximo
print(data.max())

#obtener el grafico
albany=data[data]['region'] =='Albany'
altlanta=data[data]['region']=='Atlanta'
west=data[data]['region']=='West'

a_albany=albany.plot(x='year', y='AveragePrice', kind='scatter')
a_atlanta=altlanta.plot(x='year', y='AveragePrice', kind='scatter')
a_west=west.plot(x='year', y='AveragePrice', kind='scatter')

plt.show()