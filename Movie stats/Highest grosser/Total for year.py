import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

Hig_Gross = pd.read_csv('HighestGrossers (1).csv')

for col in ['TOTAL FOR YEAR','TOTAL IN 2019 DOLLARS','TICKETS SOLD']:
        Hig_Gross[col].replace(to_replace=',', value='',regex=True, inplace=True)
        Hig_Gross[col].replace(to_replace='\$', value=' ',regex=True, inplace=True)
        Hig_Gross[col] = Hig_Gross[col].astype(str).astype('float64')
Hig_Gross['GENRE'] = Hig_Gross['GENRE'].fillna('Action')

fig = px.histogram(data_frame=Hig_Gross,
                   x='MOVIE',
                   y='TOTAL FOR YEAR',
                   color='GENRE')

fig.show()