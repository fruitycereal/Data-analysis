import pandas as pd
pd.set_option('float_format', '{:f}'.format)
import plotly.express as px

HighestGrossers = pd.read_csv('HighestGrossers (1).csv')

HighestGrossers['TOTAL FOR YEAR'] = HighestGrossers['TOTAL FOR YEAR'].apply(lambda x: x.replace('$', ''))
HighestGrossers['TOTAL FOR YEAR'] = HighestGrossers['TOTAL FOR YEAR'].apply(lambda x: x.replace(',', ''))
HighestGrossers['TOTAL FOR YEAR'] = HighestGrossers['TOTAL FOR YEAR'].astype(int)
fig = px.line(HighestGrossers, x="MOVIE", y="TOTAL FOR YEAR", markers=True)
fig.show()