import numpy as np
import pandas as pd
worker_type = np.arange(3)
years = np.arange(3)


#import required datas from excel

df_requirements = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Requirement', header = 0, index_col= 0)
df_beginning_workforce = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Beginning', header = 0, index_col = 0)
#df_resign_rate = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Resign', header = 0, index_col = 0)
df_hiring_limit = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx', sheet_name='Hiring_Limit', header = 0, index_col = 0)
df_hiring_cost = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Hiring_Cost', header = 0, index_col = 0)
df_promoting_cost = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Promoting_Cost', header = 0, index_col = 0)
df_idle = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Idle', header = 0, index_col = 0)
df_outsorcing_cost = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Outsourcing_Cost', header = 0, index_col = 0)
df_part_time_cost = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Part_Time_Cost', header = 0, index_col = 0)
#df_part_time_total = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Part_Time_Total', header = 0, index_col = 0)
#df_education_limit = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Education', header = 0, index_col = 0)
#df_outsorcing_total = pd.read_excel(r'C:\Users\Emir\Desktop\case2\WorkforceData.xlsx',sheet_name = 'Outsourcing_Total', header = 0, index_col = 0)

#tekli verileri çekmeye uğraşmadım, onları programda direkt değer olarak yazacağım 

#convert the data into appropriate format

#two dimensional datas

#requirements for each i type workforce for year j
requirements = {}

for i in np.arange(len(worker_type)):
    for j in np.arange(len(years)):
        requirements[(i,j)] = df_requirements.iloc[i,j]
    
#one dimensional datas

#beginning workforce of the first year
beginning_workforce = {}
beginning_workforce = df_beginning_workforce.to_numpy()[0]

#yearly resign rate for each type of workforce
#resign_rate = {}
#resign_rate = df_resign_rate.to_numpy()[0]

#yearly hiring limit for each type of workforce
hiring_limit = {}
hiring_limit = df_hiring_limit.to_numpy()[0]

#hiring cost of each type of workforce
hiring_cost = {}
hiring_cost = df_hiring_cost.to_numpy()[0]

#education limit for C to B
"""education_limit = {}
education_limit = df_education_limit.to_numpy()[0]"""

#promoting cost C to B and B to A
promoting_cost = {}
promoting_cost = df_promoting_cost.to_numpy()[0]

#idle cost
idle = {}
idle = df_idle.to_numpy()[0]

#outsorcing cost
outsorcing_cost = {}
outsorcing_cost = df_outsorcing_cost.to_numpy()[0]

#total outsorcing workforce in one year
"""outsorcing_total = {}
outsorcing_total = df_outsorcing_total.to_numpy()[0]"""

#part-time cost
part_time_cost = {}
part_time_cost = df_part_time_cost.to_numpy()[0]

#total part-time workforce in one year
"""part_time_total = {}
part_time_total = df_part_time_total.to_numpy()[0]"""














