
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# saving path into a varibale
paths = './datasets/first_model.csv'


# reading the datatset
df = pd.read_csv(paths)


# breaking down dataframe(df) into required columns

selected_col = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF","FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]
x=df[selected_col]

y=df.SalePrice


#breaking-down data into training and testing
train_x , val_x , train_y , val_y = train_test_split(x,y , random_state=1)


#saving our random forest algo into a variable
algo = RandomForestRegressor(random_state=1)

#fitting algo to make model
algo.fit(train_x,train_y)

#predicting val_y by val_x value
algo.predict(val_x)


# taking out mean_absolute_error value
predicted_result=algo.predict(val_x)
mean_abs = mean_absolute_error(val_y , predicted_result)

# printing actual value and predicted value
actual_value=val_y[:6]
print(actual_value)

predicted_value=predicted_result[:6]
print(predicted_value)