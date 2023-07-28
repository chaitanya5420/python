import pandas as pd


# converting excel dataset into panda dataframe
df_train1 = pd.read_excel("./datasets/train1.xlsx")
df_train2 = pd.read_excel("./datasets/train2.xlsx")


# printing both dataframe
# print(df_train1)
# print(df_train2)


# values to comapre with first sheet 
values_to_be_found = df_train2["dataset_2_col_second"]
# print(values_to_be_found)


# making a boolean indexing series with isin and using this inside our dataframe will give those rows who have True indexing
filtered_rows_dataframe = df_train1[df_train1["dataset_1_col"].isin(values_to_be_found)]
# print(filtered_rows_dataframe)


# droping out same value of this colume
filtered_rows_dataframe = filtered_rows_dataframe.drop_duplicates()
# print(filtered_rows_dataframe)


# making a excel file of rows and columns filtered by second dataset(20 value) 
filtered_rows_dataframe.to_excel("final.xlsx", index=False)

# --------------------------------------------------------Merging Part Start-----------------------------------------------------------------------------------




# display dimensions of all three dataset)
# print(df_train1.shape)
# print(df_train2.shape)
# print(filtered_rows_dataframe.shape)


# merging  second dataframe and final datafarme with concat
# final_sheet = pd.concat([final_dataframe , df_train2] )
# final_sheet.to_excel('new1.xlsx')
#                       OR
# merging  second dataframe and final datafarme with join
# final_sheet = final_dataframe.join(df_train2)
# final_sheet.to_excel('by_join.xlsx')
#                       OR
# merging  second dataframe and final datafarme with merge
final_sheet = pd.merge(df_train2 , filtered_rows_dataframe , left_on ='dataset_2_col_second' , right_on = 'dataset_1_col')
# print(final_sheet.columns)

final_sheet.to_excel('by_merge.xlsx')



