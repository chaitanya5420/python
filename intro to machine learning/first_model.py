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


# storing algorithem into a variable
algo = DecisionTreeRegressor(random_state=1)


# making model by fitting algorithem into datasets - X,Y 
model = algo.fit(X,Y)
print(model)

# using above fitted model and try to make prediction on new data (top 5 rows of original data)
prediction = algo.predict(X.head())
print(prediction)