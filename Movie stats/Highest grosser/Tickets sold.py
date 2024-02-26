import pandas as pd
pd.set_option('float_format', '{:f}'.format)
import plotly.express as px

HighestGrossers = pd.read_csv('HighestGrossers (1).csv')

HighestGrossers['TICKETS SOLD'] = HighestGrossers['TICKETS SOLD'].apply(lambda x: x.replace('$', ''))
HighestGrossers['TICKETS SOLD'] = HighestGrossers['TICKETS SOLD'].apply(lambda x: x.replace(',', ''))
HighestGrossers['TICKETS SOLD'] = HighestGrossers['TICKETS SOLD'].astype(int)
fig = px.line(HighestGrossers, x="YEAR", y="TICKETS SOLD")
fig.show()