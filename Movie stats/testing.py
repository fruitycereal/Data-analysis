import pandas as pd
import plotly.express as px

top_dist = pd.read_csv('HighestGrossers (1).csv')

for col in ['MOVIE','GENRE','YEAR']:
        top_dist[col].replace(to_replace=',', value='',regex=True, inplace=True)
        top_dist[col].replace(to_replace='\$', value=' ',regex=True, inplace=True)
        top_dist[col].replace(to_replace='\%', value=' ',regex=True, inplace=True)
        top_dist[col] = top_dist[col].astype(str).astype('float64')
top_dist['YEAR'] = top_dist['YEAR'].fillna('Action')

fig = px.pie(top_dist, values=top_dist['YEAR'], names='DISTRIBUTORS', title='DISTRIBUTOR AND MARKET SHARE')
fig.show()