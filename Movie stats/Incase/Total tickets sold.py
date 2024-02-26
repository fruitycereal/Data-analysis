import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
year_price = pd.read_csv('AnnualTicketSales.csv')
year_price.drop(columns=['Unnamed: 5'],axis=0,inplace=True)
year_price.head()

for col in ['TICKETS SOLD', 'TOTAL BOX OFFICE','TOTAL INFLATION ADJUSTED BOX OFFICE', 'AVERAGE TICKET PRICE']:
        year_price[col].replace(to_replace=',', value='',regex=True, inplace=True)
        year_price[col].replace(to_replace='\$', value=' ',regex=True, inplace=True)
        year_price[col] = year_price[col].astype(str).astype('float')

fig = px.scatter(year_price, 
                 x="YEAR", 
                 y="TICKETS SOLD",  
                 color= "TOTAL BOX OFFICE" , 
                size ="AVERAGE TICKET PRICE",
                trendline='rolling', trendline_options=dict(window=1))
fig.show()