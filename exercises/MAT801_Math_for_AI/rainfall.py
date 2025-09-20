from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

#Data Loading
r_data = pd.ExcelFile("rainfall_data.xlsx")
df = pd.read_excel("rainfall_data.xlsx",'Monthly_Rainfall')

#Set up Scaler
scaler = StandardScaler()
df_x = scaler.fit_transform(df)
