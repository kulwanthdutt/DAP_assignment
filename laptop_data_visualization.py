import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("laptop_data.csv")
data=pd.DataFrame(df)
print(data.iloc[:,1])

name=list(data.iloc[:5,1])
price=list(data.iloc[:5,0])

#plt.figure(figsize=(20,10))
plt.bar(price,name,color='red')

plt.title('laptop and their prices')
plt.xlabel('laptop name')
plt.ylabel('price')

plt.show()