import pandas as pd
import plotly.express as px

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

year_price = pd.read_csv('AnnualTicketSales.csv')
year_price.drop(columns=['Unnamed: 5'],axis=0,inplace=True)

for col in ['TICKETS SOLD', 'TOTAL BOX OFFICE','TOTAL INFLATION ADJUSTED BOX OFFICE']:
        year_price[col].replace(to_replace=',', value='',regex=True, inplace=True)
        year_price[col].replace(to_replace='\$', value=' ',regex=True, inplace=True)
        year_price[col] = year_price[col].astype(str).astype('float')

fig = px.line(year_price, 
                 x="YEAR", 
                 y="TOTAL INFLATION ADJUSTED BOX OFFICE")
fig.show()