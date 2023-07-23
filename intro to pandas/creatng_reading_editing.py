import pandas as pd 

# 1(A) - creating DataFrame using dataframe class

self_made_df = pd.DataFrame( {"Apples": [30,40,50] , "Bananas":[40,20,15]} , index = ["1st year" ,"2nd year" , "2rd year"])
# print(self_made_df)

# 1(B) - # creating dataframe using series class
series_df = pd.Series( [1,2,3,4,5] , index =["1st","2nd" ,"3rd" , "4th" , "5th"]  , name = "no from 1 to 5")
print(series_df)





# 2 - Reading DataFrame

# index_col will make able to  use particular column as a index 
df = pd.read_csv("./datasets/winemag-data_first150k.csv" ,index_col=0)
# print(df)

# display 5 result from the top of dataframe
# print(df.head())

# display rows and columns od dataframe in a tuple
# print(df.shape)                  
    
# .to_string will print entire dataframe
# print(df.to_string())



# 3 - Writing\Saving dataframe in csv format

# here we can use any type of format like json 
df.to_csv("winedatasetcopy.csv")


