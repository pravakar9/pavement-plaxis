import math

import pandas as pd
from plxscripting.easy import *

input_port_i = '10000'
input_port_o = '10001'
input_password = 'MfDgR%~%4~?>rSiG'  # PUT YOUR PLAXIS 3D INPUT PASSWORD HERE
save_path = r'C:\Users\TUF\Desktop'
s_i, g_i = new_server('localhost', 10000, password='MfDgR%~%4~?>rSiG')
s_i.new()


surfacedisplacement_1 = g_i.surfdispl((-11.5, -10, -5), (11.5, -10, -5), (11.5, 10, -5), (-11.5,  10, -5))
eq= g_i.displmultiplier()
eq.setproperties(
    "Name", "eq",
    "Signal", "Table",
    "DataType", "Accelerations",
    "DriftCorrection", True,  
)
df = pd.read_excel(r'C:\\Users\\TUF\\Downloads\\eq.xls')
for i in range(1, len(df)):
    value1 = df['G'][i]
    value2 = df['H'][i]
    if pd.isna(value1) or pd.isna(value2):
        break
    # Use the values in your Python code here

    eq.Table.add(value1, value2) #assign time as value1 and multiplier as value2 in Table of eq a dynamic displacement multiplier