import pandas as pd 
import json

u_cols = ['dates', 'pid', 'level', 'prog', 'infor'] #Set columns for DataFrame
df = pd.read_csv('b', sep=',', names=u_cols) #Read file log and display to dataframe's format
file = dict([(i,[a,b,c,d]) for i,a,b,c,d in zip(df.dates, df.pid,df.level,df.prog,df.infor)])


#print (file)