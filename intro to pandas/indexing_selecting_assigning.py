import pandas as pd

'''
selecting can be done in two ways -  1 by python builtin accessor method  =  . and []
                                     2 by pandas bultin accessor method   = loc and iloc
iloc = work upon indexing      df.iloc[row_indexing ,column_indexing ]
loc = work upon name/labels    df.loc[row_name/indexing , column_name/indexing]
'''



df = pd.read_csv("./datasets/winemag-data-130k-v2.csv", index_col=0)



# Select the description column from df and assign the result to the variable desc
desc = df.description
# print(desc)


# Select the first value from the description column of df, assigning it to variable first_description
first_description = df.description[0]
# print(first_description)


# Select the first row of data (the first record) from df, assigning it to the variable first_row.
first_row = df.iloc[0]
# print(first_row)


# Select the first 10 values from the description column in df, assigning the result to variable first_descriptions.
first_10row =df.description.iloc[0:10]
# print(first_10row)


# Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews
by_index_labels = df.loc[[1,2,3,5,8]]
# print(by_index_labels)


# Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100. In other words, generate the following DataFrame:



# Create a variable df containing the country and variety columns of the first 100 records.
# Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
# Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.