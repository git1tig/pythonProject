#Домашка one hot без Чайников
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
for i in range(0, len(data.index)):
        if data.iloc[i]['whoAmI']=="human":
            data.iloc[i]['whoAmI']=1
        else:
            data.iloc[i]['whoAmI']=0
print(data)
