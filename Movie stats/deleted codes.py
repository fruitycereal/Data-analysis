import pandas as pd
import plotly.express as px

top_dist = pd.read_csv('TopDistributors.csv')

for col in ['TOTAL GROSS','AVERAGE GROSS','MARKET SHARE']:
        top_dist[col].replace(to_replace=',', value='',regex=True, inplace=True)
        top_dist[col].replace(to_replace='\$', value=' ',regex=True, inplace=True)
        top_dist[col].replace(to_replace='\%', value=' ',regex=True, inplace=True)
        top_dist[col] = top_dist[col].astype(str).astype('float64')

d = px.histogram(top_dist, x='DISTRIBUTORS', y='TOTAL GROSS',color='RANK')
d.show()




import plotly.graph_objects as go
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
from pandas.core.frame import DataFrame
from plotly.subplots import make_subplots
from typing import DefaultDict