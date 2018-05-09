import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#a = np.array([[1,2,3],[2,3,4],[7,5,6],[2,3,5],[9,8,5],[4,3,2]])
#print(a)

a = {'nos':[1,2,3],'grades':[44,55,32],'g':[9,7,6]}

df = pd.DataFrame(a)
#print(df)

df.to_json('df.json')
df = pd.read_json('df.json')
df.to_html('fg.html')

print(df)

#print(df.head())
#print(df.tail())

df.plot()
plt.show()