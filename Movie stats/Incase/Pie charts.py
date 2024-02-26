import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

Hig_Gross = pd.read_csv('HighestGrossers (1).csv')

for col in ['TOTAL FOR YEAR','TOTAL IN 2019 DOLLARS','TICKETS SOLD']:
        Hig_Gross[col].replace(to_replace=',', value='',regex=True, inplace=True)
        Hig_Gross[col].replace(to_replace='\$', value=' ',regex=True, inplace=True)
        Hig_Gross[col] = Hig_Gross[col].astype(str).astype('float64')
Hig_Gross['GENRE'] = Hig_Gross['GENRE'].fillna('Action')
px.histogram(data_frame=Hig_Gross,x='MOVIE',y='TOTAL FOR YEAR',color='GENRE').update_xaxes(categoryorder="total descending")

sort = Hig_Gross.sort_values(['TOTAL FOR YEAR', 'MOVIE'],ascending=False,ignore_index=True)
categorical_cols = sort[['GENRE','MPAA RATING','DISTRIBUTOR']]
def pieChartPlotter(dataset, columnName):

    values = dataset[columnName].value_counts()
    labels = dataset[columnName].unique()
    pie, ax = plt.subplots(figsize=[10, 6])

    patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.2f%%', shadow=True, pctdistance=.5
                                       )

    plt.legend(patches, labels, loc="best")
    plt.title(columnName, color='black', fontsize=14)
    plt.setp(texts, color='white', fontsize=9)
    plt.setp(autotexts, size=10, color='black')
    autotexts[1].set_color('black')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
for column in categorical_cols:
    pieChartPlotter(sort, column) 
