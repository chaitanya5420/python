'''
Here we are managing tree leafs an try to get minimum absolute error value to get more accurate model
'''


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error


# setting dataset path   |  dot(.) is telling th root directory path 
paths = './datasets/first_model.csv'

# reading  dataset and converting into dataframe
df = pd.read_csv(paths)


# coverting dataframe into required features/columns - X and Y
selected_col = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF","FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]
x=df[selected_col]

y=df.SalePrice


#spilitting data
train_x , val_x , train_y , val_y = train_test_split(x,y , random_state=1)


# making function to get mean value 
def mae(max_leaf_node , train_x , val_x , train_y , val_y ):
    algo = DecisionTreeRegressor( max_leaf_nodes=max_leaf_node,random_state=1)      
    algo.fit(train_x,train_y)
    predict = algo.predict(val_x)
    mean_abs = mean_absolute_error(val_y , predict)
    return mean_abs

#taking diffrent leafs to get minimum absolute error value
leaf_nodes = [5, 25, 50, 100, 250, 500]

scores = {i:mae(i , train_x , val_x , train_y , val_y)  for i in leaf_nodes}
print(scores)

# giving min absolte error value 
minimum_absolute_value = min(scores , key=scores.get)
print(minimum_absolute_value)







































#dictionary exercise


d ={5: 35044.51299744237, 25: 29016.41319191076, 50: 27405.930473214907, 100: 27282.50803885739, 250: 27893.822225701646, 500: 29454.18598068598}

#printing dictionary
# print('whole dictionary is \n{}'.format(d))

#accessing value by dictionary key
# print(d[25])
# print(d.get(25))

#keys method will return a list of all keys
# print(d.keys())        #give list of keys


#value method returns a list of all values 
# print(d.values())

#return all keys with it's value in a list of tuples of each element 
# key_value_pair = d.items()
