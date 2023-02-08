import dash_bootstrap_components.themes
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import matplotlib as plot
import folium
import dash_bootstrap_components as dbc
import navigation
from dash_bootstrap_components import themes





# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
df =pd.read_csv("Student_dataset_2021.csv")
new=df.groupby('stream')
newdf=new.max()
fig7 =px.bar(newdf,y='jee_perc',text='jee_perc',color='jee_perc',labels={'jee_perc':'Highest percentile in jee'})
newdf2=df.groupby('stream')
df2=newdf2.mean()
fig2 =px.bar(df2,x='parent_income',text='parent_income',color='parent_income',labels={'parent_income':'Average parent income'})
df3=new.count()
fig3 =px.bar(df3,x='gender',color='gender',title='MALE VS FEMALE RATIO IN IT',labels={'gener':'gender'})
df6=df.groupby('gender')
newdf=df6.count()
fig =px.pie(newdf,values='sid',hole=0.5,color='sid')
fig6=fig.update_traces(textinfo='percent+value')
df=pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/location.csv")
a_list=df[['place','latitude','longitude']].values.tolist()
map=folium.Map(location=[19.0760,72.8777])
fg=folium.FeatureGroup(name='map')
for i in a_list:
    fg.add_child(folium.Marker(location=[i[1],i[2]],popup=i[0],icon=folium.Icon(color='green')))
map.add_child(fg)
map.save('Locations.html')
fig =px.pie(newdf,values='sid',hole=0.5,color='sid')
fig.update_traces(textinfo='percent+value')
fig8=fig
df3=pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/Student_dataset_2021.csv")
newdata9=df3.groupby('minority')
newdata10=newdata9.max()
fig10 =px.bar(newdata10,y='jee_perc',text='jee_perc',color='jee_perc',labels={'jee_perc':'Highest percentile in jee'})




app.layout = html.Div([
navigation.navbar,

    dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(
        id='example-graph',
        figure=fig7
    ),],),
        dbc.Col([dcc.Graph(
            id='example-graph2',
            figure=fig2
        ),
            dcc.Graph(
                id='example-graph10',
                figure=fig10
            ),
        ]),

    ]),


    dcc.Graph(
            id='example-graph3',
            figure=fig8
        ),
    html.Iframe(id='maps', srcDoc=open('Locations.html', 'r').read(), width='100%', height='600'),

])
])


if __name__ == '__main__':
    app.run_server(debug=True)