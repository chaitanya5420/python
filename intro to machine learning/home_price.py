import pandas as pd
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_absolute_error

# saving dataset path into variable 
trian_path = './datasets/home_prediction/train.csv'

# making dataframe data by using datasets path  
df_train = pd.read_csv(trian_path)


# breaking dataframe into two subsets x and y
selected_col = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd','PoolArea','ScreenPorch','3SsnPorch','LowQualFinSF' ]
x = df_train[selected_col]
y = df_train.SalePrice


# storing random forest algorithem into a variable 
algo = RandomForestRegressor(random_state=45)


# fitting working = fit takes the data that we provide and train our model using this data 
# how - fitting random forest instance
fitting=algo.fit(x,y)

# making prediction of above fitted datasets
train_validation = fitting.predict(x)


# print(train_validation[:6])
# print(mean_absolute_error(y,train_validation))
# print(y[:6])


# now again we are setting up things to use new unseen data (test data) 
test_path = './datasets/home_prediction/test.csv'
df_test = pd.read_csv(test_path)

test_x = df_test[selected_col]
# test_y = df_test.columns
# print(test_y)



algo.fit(x,y)

algo.fit(x,y)

test_validation = algo.predict(test_x)


# making dictionary for id and predicted sale price
output = pd.DataFrame({'id':df_test.Id , 'saleprice':test_validation})
output.to_csv('house_pred.dictonary' , index=False)
print(output)
