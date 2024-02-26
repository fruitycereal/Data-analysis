import pandas as pd
import plotly.express as px

top_dist = pd.read_csv('TopDistributors.csv')

for col in ['TOTAL GROSS','AVERAGE GROSS','MARKET SHARE']:
        top_dist[col].replace(to_replace=',', value='',regex=True, inplace=True)
        top_dist[col].replace(to_replace='\$', value=' ',regex=True, inplace=True)
        top_dist[col].replace(to_replace='\%', value=' ',regex=True, inplace=True)
        top_dist[col] = top_dist[col].astype(str).astype('float64')

fig = px.histogram(top_dist,x='DISTRIBUTORS',y='AVERAGE GROSS',color='RANK')
fig.show()