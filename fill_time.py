#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:55:05 2020

@author: ebrain
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd
import datetime

def next_time(time):
    if time%100 == 45:
        if time - time%100 == 2200:
            return 900
        else:
            return time - 45 + 100
    else:
        return time + 15

Dataframe = pd.read_csv("./peak_data.csv")
Dataframe = Dataframe[["tgtDate", "tgtHhmi", "peak"]]
end_num = len(Dataframe)
cnt = 0
def next_day (now_day):
    now_day = str(now_day)
    result = datetime.datetime.strptime(now_day,"%Y%m%d") + datetime.timedelta(days=1)
    return int(result.strftime("%Y%m%d"))
    
def Insert_row_(row_number, df, row_value): 
    # Slice the upper half of the dataframe 
    df1 = df[0:row_number] 
   
    # Store the result of lower half of the dataframe 
    df2 = df[row_number:] 
   
    # Inser the row in the upper half dataframe 
    df1.loc[row_number]=row_value 
   
    # Concat the two dataframes 
    df_result = pd.concat([df1, df2]) 
   
    # Reassign the index labels 
    df_result.index = [*range(df_result.shape[0])] 
   
    # Return the updated dataframe 
    return df_result 



while(cnt < end_num - 1):
    if next_time(Dataframe["tgtHhmi"][cnt]) == Dataframe["tgtHhmi"][cnt+1]:
        cnt = cnt+1 
        continue
    else:
        if next_time(Dataframe["tgtHhmi"][cnt]) == 900:
            
            Dataframe = Insert_row_(cnt+1, Dataframe,[next_day(Dataframe["tgtDate"][cnt]), 900, -1]) 
        else:
            Dataframe = Insert_row_(cnt+1, Dataframe,[Dataframe["tgtDate"][cnt],next_time(Dataframe["tgtHhmi"][cnt]), -1]) 
            
        cnt = cnt+1
        end_num = end_num + 1
        
        

        
            