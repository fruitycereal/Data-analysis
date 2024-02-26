import pandas as pd
import plotly.express as px

df = pd.read_csv('AnnualTicketSales.csv')
df.drop('Unnamed: 5',axis = 1,inplace = True)

j = []
for i in df['TICKETS SOLD']:
    j.append(i.replace(",",""))
    
df['Tickets_sold'] = j
k = []
for i in df.columns:
    if i not in ['YEAR','TICKETS SOLD','Tickets_sold']:
        for j in df[i]:
            k.append(j[1:].replace(',',''))
        df[i] = k
    k.clear()
        
df.drop('TICKETS SOLD',axis = 1,inplace = True)
df = df.astype(float)

ticketprices = df[['YEAR','AVERAGE TICKET PRICE']]
fig = px.bar(x = [i for i in ticketprices.YEAR],y = [i for i in ticketprices['AVERAGE TICKET PRICE']],color =[i for i in ticketprices['AVERAGE TICKET PRICE']])
fig.update_layout(xaxis_title = 'YEARS',yaxis_title = 'AVERAGE TICKET PRICE ($)')
fig.show()