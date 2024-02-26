import pandas as pd
import plotly.express as px

top_dist = pd.read_csv('TopDistributors.csv')

for col in ['TOTAL GROSS','AVERAGE GROSS','MARKET SHARE']:
        top_dist[col].replace(to_replace=',', value='',regex=True, inplace=True)
        top_dist[col].replace(to_replace='\$', value=' ',regex=True, inplace=True)
        top_dist[col].replace(to_replace='\%', value=' ',regex=True, inplace=True)
        top_dist[col] = top_dist[col].astype(str).astype('float64')

fig = px.pie(top_dist, values=top_dist['MARKET SHARE'], names='DISTRIBUTORS', title='DISTRIBUTOR AND MARKET SHARE')
fig.show()