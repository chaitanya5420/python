

Pseudocode


Task = you have two datasets with similer column but diffrent size one dataset has 49 rows and the other one has 20 rows .your task is to find those 
       values which are present in dataset two but not in dataset 1 . and then show that new dataframe with the previous version of it -in this 
       case it is dataset2.



steps to solve this problem = 2

step-1 : comparing all the elements between two columns    
         used_function  = isin()
          
step-2 : now making a dataframe that has compared value and previous values 
         used_function = merge(left_on , right_on )
          