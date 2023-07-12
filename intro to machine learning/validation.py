import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error


# taking dataset path and read it in a variable called home_data 
data_path ='./datasets/first_model.csv'
df= pd.read_csv(data_path)



# chossing features from data
selecting_col=['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
x = df[selecting_col] 

y = df['SalePrice']


#splitting data into training and testing dataset
train_x , val_x , train_y , val_y = train_test_split(x,y ,random_state=1)


# saving algorithem for model in variable
algo = DecisionTreeRegressor(random_state=1)

#applyting algorithem into training datasets to make model 
algo.fit(train_x , train_y)


#predicting on testing dataset of x dataset and giving values for y
validation_result = algo.predict(val_x)


#printing top  5 values of pridicting value and actual value for y 
predicted_value = validation_result[:6]
print("predicted value are :",predicted_value)

actual_value = val_y[:6]
print("actual values are :\n",actual_value)



# applying absolute mean value
mean_abs = mean_absolute_error(actual_value , predicted_value) 
print("mean absolute value is  :",mean_abs)

