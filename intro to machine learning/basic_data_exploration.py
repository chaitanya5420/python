import pandas as pd


paths = './datasets/train.csv'

df =pd.read_csv(paths)
print(df)


# describe applies some stasticle function and give values like mean,std,count(non-missinng-value)
desc_math=df.describe()   
print(desc_math)  



# taking out Mean from original dataset  
desc_mean=df['LotArea'].mean()    
print(desc_mean)



#  it is taking particular cell value from rows(YearBuilt) and columns(max) 
newly_built_house =desc_math['YearBuilt']['max']            
print(newly_built_house)



# .colums = it is displaying all the columns of our dataframe
# col = df.columns
# print(col)


#.id  = taking single column value
# id_col=df.Id
# print(id_col)
    # Or
# print(df['Id'])  



# Taking desired columns according to our need 
# Giving keys list to access columns/values accroding to keys
# var = df[['key1']]
# selecting_col = ['Id' , 'LotArea']
# x=df[selecting_col]
# print(x)   
# print(x.head())


