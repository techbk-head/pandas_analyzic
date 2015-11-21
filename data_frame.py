import pandas as pd 
import pickle

u_cols = ['dates', 'pid', 'level', 'prog', 'infor'] #Set columns for DataFrame
file = pd.read_csv('b', sep=',', names=u_cols) #Read file log and display to dataframe's format
file.to_pickle('a') # Save DataFrame to anotherfile
print (file)