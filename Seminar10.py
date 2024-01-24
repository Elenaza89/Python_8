#  В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random as rd

lst = ['robot'] *10
lst += ['human'] * 10
rd.shuffle(lst)

data = pd.DataFrame({'whoIam':lst})

# Способ 1:  использование метода get_dummies
data =pd.get_dummies(data['whoIam'], dtype=int)

#data.head()
print (lst)
print(data)

# Cпособ 2: Формирование матрицы tbl
tbl = [[ 'human', 'robot']]
for i in range(len(lst)):    
    list1 = list()
    if lst[i] == 'robot':
        list1.append(0)
        list1.append(1)
    else:
        list1.append(1)
        list1.append(0)
    tbl.append(list1)
    
print(tbl)


       