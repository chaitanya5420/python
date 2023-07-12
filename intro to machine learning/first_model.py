import pandas as pd
from sklearn.tree import DecisionTreeRegressor


# setting dataset path   |  dot(.) is telling th root directory path 
paths = './datasets/first_model.csv'



# reading  dataset and converting into dataframe
df = pd.read_csv(paths) 



# coverting dataframe into required datasets - X and Y
selected_col = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF","FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]
X = df[selected_col]
# print(X)


Y = df.SalePrice
# print(Y)


# storing Decision tree algorithem into a variable
algorithem = DecisionTreeRegressor(random_state=1)
print(df.YearBuilt)

'''
training part = making model by fitting algorithem into datasets - X,Y 
working = it takes columns define in X and setting realtionship with corresponding Y values thats why we use fit method ,  so in next step 
we give new dataset for X axis (columns of new data should be same as X )and it will automatically predict Y axis value 
'''
model = algorithem.fit(X,Y)
print(model)

# using above fitted model and try to make Prediction on top 5 rows data
prediction = algorithem.predict(X.head())
print(prediction)