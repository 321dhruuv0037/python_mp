import base64
import math

import dash_bootstrap_components.themes
import seaborn as sns
from dash import Dash, html, dcc, dash, Output, Input
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import matplotlib as plt
import folium
import dash_bootstrap_components as dbc
from folium.plugins import HeatMap
from matplotlib import pyplot as plt

import navigation
import numpy as np
from dash_bootstrap_components import themes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import folium
import dash_table


from folium.plugins import HeatMap
from folium.plugins import MarkerCluster, FeatureGroupSubGroup






# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
font_awesome1 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css'
font_awesome2 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/regular.min.css'
font_awesome3 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/solid.min.css'
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    '/assets/style2.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/regular.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/solid.min.css'
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# df =pd.read_csv("Student_dataset_2021.csv")
# new=df.groupby('stream')
# newdf=new.max()
# fig7 =px.bar(newdf,y='jee_perc',text='jee_perc',color='jee_perc',labels={'jee_perc':'Highest percentile in jee'})
# newdf2=df.groupby('stream')
# df2=newdf2.mean()
# fig2 =px.bar(df2,x='parent_income',text='parent_income',color='parent_income',labels={'parent_income':'Average parent income'})
# df3=new.count()
# fig3 =px.bar(df3,x='gender',color='gender',title='MALE VS FEMALE RATIO IN IT',labels={'gener':'gender'})
# df6=df.groupby('gender')
# newdf=df6.count()
# fig =px.pie(newdf,values='sid',hole=0.5,color='sid')
# fig6=fig.update_traces(textinfo='percent+value')
# df=pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/location.csv")
# a_list=df[['place','latitude','longitude']].values.tolist()
# map=folium.Map(location=[19.0760,72.8777])
# fg=folium.FeatureGroup(name='map')
# for i in a_list:
#     fg.add_child(folium.Marker(location=[i[1],i[2]],popup=i[0],icon=folium.Icon(color='green')))
# map.add_child(fg)
# map.save('Locations.html')
# fig =px.pie(newdf,values='sid',hole=0.5,color='sid')
# fig.update_traces(textinfo='percent+value')
# fig8=fig
# df3=pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/Student_dataset_2021.csv")
# newdata9=df3.groupby('minority')
# newdata10=newdata9.max()
# fig10 =px.bar(newdata10,y='jee_perc',text='jee_perc',color='jee_perc',labels={'jee_perc':'Highest percentile in jee'})
#
# ###machine learning###
# dfnew1=pd.read_csv("Student_dataset_2021.csv")
# X=dfnew1[[ 'x_perc','xii_perc','cet_perc','physics_xii','chem_xii','maths_xii']]
# Y = dfnew1['jee_perc']
# X_train,X_test,Y_train,Y_test= train_test_split(X, Y, test_size=0.4,random_state=101)
# lm = LinearRegression()
# lm.fit(X_train, Y_train)
# print(lm.intercept_)
# print(lm.coef_)
# X_train.columns
# newdf=pd.DataFrame(lm.coef_,X.columns,columns=['jee percentile'])
# abcd=newdf.to_html()

df =pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/slider.csv")
year_list = list(df['year'].unique())
print(year_list)

options = [
    {'label': 'COMPS', 'value': 'COMPS'},
    {'label': 'EXTC', 'value': 'EXTC'},
    {'label': 'MECH', 'value': 'MECH'},
    {'label': 'IT', 'value': 'IT'},
    {'label':'ALL BRANCHES','value':'none'}
]
options1 = [
    {'label': 'NO OF STUDENTS', 'value': 'sid'},
    {'label': 'XTH PERCENTAGE', 'value': 'x_perc'},
    {'label': 'XII TH PERCENTAGE', 'value': 'xii_perc'},
    {'label': 'JEE PERCENTILE', 'value': 'jee_perc'}
]

options2 = [
    {'label': 'NO OF STUDENTS', 'value': 'sid'},
    {'label': 'XTH PERCENTAGE', 'value': 'x_perc'},
    {'label': 'XII TH PERCENTAGE', 'value': 'xii_perc'},
    {'label': 'JEE PERCENTILE', 'value': 'jee_perc'}
]
df = pd.read_csv('slider.csv')
df = df.fillna(df.mean())
max_df = df.groupby(['year', 'stream'])['jee_perc'].mean().reset_index()
fig1 = px.line(max_df, x='year', y='jee_perc', color='stream', title='Average Percentile by Year and Stream',hover_data=['jee_perc', 'year'],labels={'jee_perc': 'JEE Percentile'})
fig1.update_layout(xaxis=dict(tickmode='linear', dtick=1))
highest = max_df.loc[max_df['jee_perc'].idxmax()]
formatted_percentile = "{:.2f}".format(highest['jee_perc'])
formatted_year = int(highest['year'])
highest_branch = highest['stream']
filtered_df = df[df['year'] == '2021']
corr = filtered_df['sid'].corr(filtered_df['x_perc'])
print("Correlation between SID and X percentile: {:.2f}".format(corr))

# Add an annotation to the graph with the highest percentile value and year
best_stream = highest['stream']

print(f"The best performing stream is {best_stream}")
# Group the data by stream and calculate the percentage change for each stream
stream_df = df.groupby('stream')['jee_perc'].pct_change().reset_index()

# Find the stream with the highest percentage growth
# Read the CSV file into a Pandas DataFrame
# data = pd.read_csv('heatmap.csv')
#
# # Create a map centered on a specific location
# m = folium.Map(location=[18.932245, 72.826439], zoom_start=10)
#
# # Create a heatmap layer from the data
# heat_data = [[row['latitude'], row['longitude']] for index, row in data.iterrows()]
# heatmap = HeatMap(heat_data, name='Heatmap')
#
# # Add the heatmap layer to the map
# heatmap.add_to(m)
# #text marker
#
#
# # Add a layer control to the map
# folium.LayerControl().add_to(m)
# #western line
# folium.PolyLine([(18.9354, 72.8262),(18.9442, 72.8239),(18.9536, 72.8174),(18.9591, 72.8132),(18.9696, 72.8196),(18.9827, 72.8193)
# ,(19.0088, 72.8308)
# ,(19.0111, 72.8403)
#  ,(19.0173, 72.8426)
#  ,(19.0271, 72.8464)
#  ,(19.0395, 72.8445)
#  ,(19.0544, 72.8402)
#  ,(19.0686, 72.8394)
#  ,(19.0814, 72.8416)
#  ,(19.0972, 72.8445)
#  ,(19.1197, 72.8464)
# ,(19.1365, 72.8497)
# ,(19.1542, 72.8534)
# ,(19.1647, 72.8491)
# ,(19.1867, 72.8486)
# ,(19.204431413672715, 72.85164270837505)
# ,(19.2292, 72.8572)
# ,(19.2502, 72.8592)
#  ,(19.2813, 72.8563)
#  ,(19.3103, 72.8517)
#  ,(19.3465, 72.8545)
#  ,(19.3802, 72.8395)
#  ,(19.4186, 72.8179)
# ,(19.455235541869268, 72.81211431208968),(19.519096449558383, 72.85036910889094),(19.577117893783946, 72.82171623907293),(19.6982688067134, 72.772179156276),(19.990148370578478, 72.74472504650069)],color="green",tooltip="Western Line",weight=3).add_to(m)
#
# folium.Marker(location=[19.455134379429648, 72.81202848139804],
#               popup=folium.Popup('<i>Western Line</i>'),
#               tooltip='Western Line',
#               icon=folium.DivIcon(html="""Western Line""",
#                                   class_name="mapText"),
#               ).add_to(m)
#
# # inject html into the map html
# m.get_root().html.add_child(folium.Element("""
# <style>
# .mapText {
#     white-space: nowrap;
#     color:green;
#     font-size:medium
# }
# </style>
# """))
# #csmt to kasara
# folium.PolyLine([(18.943888,72.835991),(18.994736760414902, 72.83299728510069),(19.020330448510123, 72.84365954445657),(19.066573611668673, 72.87980951393833),(19.085515812592636, 72.90727222557408),(19.18659041458438, 72.97536110837471),(19.19042930746032, 73.02342671394041),(19.18871434223293, 73.04228938324867),(19.23571726600612, 73.13078415340435),(19.29602463586944, 73.20378245441398),(19.439762665560814, 73.30787021023416),(19.64852859016493, 73.47304712558349)],color="blue",tooltip="Central Line").add_to(m)
# #kalyan to khopoli
# folium.PolyLine([(19.23571726600612, 73.13078415340435),(19.16699440588468, 73.23863896084042),(18.91283348037467, 73.3207955409171),(18.789286786303602, 73.34539545440576)],color="blue",tooltip="Central Line").add_to(m)
# folium.Marker(location=[19.23644145356165, 73.13028936975887],
#               popup=folium.Popup('<i>Central Line</i>'),
#               tooltip='Central Line',
#               icon=folium.DivIcon(html="""Central Line""",
#                                   class_name="mapText"),
#               ).add_to(m)
# #harbour csmt to panvel
# folium.PolyLine([(18.940295750335533, 72.83575288324467),(18.962173966262736, 72.83900556789912),(18.988393871718458, 72.84329590608344),(19.0162622023617, 72.85879774048796),(19.067444858086915, 72.8800346016453),(19.048343621374624, 72.93196402557346),(19.06339879342969, 72.99882074488211),(19.055727544411585, 73.017959166992),(19.02220959140532, 73.0189194026994),(19.01947799290236, 73.03948562689445),(19.02666691178611, 73.05961378456648),(19.008516434583814, 73.09459223336893),(18.992155097791116, 73.12093264019435)],color="yellow",tooltip="Harbour Line").add_to(m)
# #harbor wadala to goregaon
# folium.PolyLine([(19.0162622023617, 72.85879774048796),(19.041049756832933, 72.84699720172428),(19.056530893119035, 72.83989345615814),(19.068513041300847, 72.8399588909093),(19.164918718417084, 72.84922634833158)],color="yellow",tooltip="Harbour Line").add_to(m)
# #metro line 9 gkp-vsv
# folium.PolyLine([(19.08680000156715, 72.90811058324704),(19.09658860912144, 72.89500762742944),(19.10809761674883, 72.87981916604637),(19.121114420719188, 72.8482312390653),(19.130568159099553, 72.82134052371956)],color="cyan",tooltip="Metro Line 9").add_to(m)
# #thane vashi line
# folium.PolyLine([(19.18675254065755, 72.97540402372054),(19.176037824932855, 72.99472545441198),(19.103518084649536, 73.01215414724949),(19.07580016180758, 73.01782716790103),(19.06339879342969, 72.99882074488211)],color="purple",tooltip="TransHarbour Line").add_to(m)
#
# # inject html into the map html
# m.get_root().html.add_child(folium.Element("""
# <style>
# .mapText {
#     white-space: nowrap;
#     color:green;
#     font-size:medium
# }
# </style>
# """))
# folium.LayerControl(overlay={
#     'Markers': '<span style="color: green">Western Line</span> | <span style="color: blue">Central Line</span> | <span style="color: yellow">Harbour Line</span>',
# }).add_to(m)
#
#
#
#
# # Save the map to an HTML file
# m.save('heatmap.html')
import pandas as pd

# read the csv file
df =pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/slider.csv")
print(df.describe())
# fill missing values with the mean of the column
df = df.fillna(df.mean())

# group the data by year and stream and calculate the mean JEE percentile
max_df = df.groupby(['year', 'stream'])['jee_perc'].mean().reset_index()

# filter the data for the years 2021 and 2022
filtered_df = max_df[max_df['year'].isin([2018, 2021])]

# pivot the data to create a table with streams as columns and years as index
pivot_df = filtered_df.pivot(index='year', columns='stream', values='jee_perc')

# calculate the percentage change between the two years for each stream
percent_change = (pivot_df.loc[2021] - pivot_df.loc[2018]) / pivot_df.loc[2018] * 100

# display the percentage change for each branch
print("Percentage change in JEE percentile by branch:\n", percent_change)

# find the branch with the highest percentage change
highest_change = percent_change.idxmax()
print("The branch with the highest percentage change is:", highest_change, "with a change of", round(percent_change[highest_change], 2), "%.")
df =pd.read_csv("slider.csv")
print(df.head())

years = ['2018', '2019', '2020', '2021']
divisions = ['COMPS', 'EXTC', 'MECH']

# Define the list of locations
locations = ['Central Harbour', 'Western Line']

# Define the table header
cols_to_include = ['sid','x_perc', 'xii_perc', 'cet_perc', 'physics_xii', 'chem_xii', 'maths_xii', 'jee_perc', 'parent_income']
df_summary = df[cols_to_include].describe().round(0).reset_index()
df_summary = df_summary.rename(columns={'sid': 'Student ID', 'x_perc': 'Xth Percentage', 'xii_perc': 'XII th Percentage', 'cet_perc': 'CET Percentile', 'physics_xii': 'Physics XIIth', 'chem_xii': 'Chemistry XIIth', 'maths_xii': 'Maths XIIth', 'jee_perc': 'JEE Percentile', 'parent_income': 'Parent Income'})



print(df_summary)












app.layout = html.Div([
    html.Div(
    [
        navigation.navbar,
        html.H1("Student Data Analysis Dashboard" ,style={'margin-left':'300px','padding-top':'10px'}),
        html.P(
            "Key Takeaways From The Page",
            className="lead",style={'margin-left':'800px','margin-top':'50px'}
        ),
    ],
    className="container",
),
html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
]),

#     dbc.Container([
#     dbc.Row([
#         dbc.Col([
#             dcc.Graph(
#         id='example-graph',
#         figure=fig7
#     ),],),
#         dbc.Col([dcc.Graph(
#             id='example-graph2',
#             figure=fig2
#         ),
#             dcc.Graph(
#                 id='example-graph10',
#                 figure=fig10
#             ),
#             html.Div(
#
#             )
#         ]),
#
#     ]),
#
#
#     dcc.Graph(
#             id='example-graph3',
#             figure=fig8
#         ),
#     html.Iframe(id='maps', srcDoc=open('Locations.html', 'r').read(), width='100%', height='600'),
#
# ])
        dbc.Row([
            dbc.Col([
html.Div([
            html.Div([
                html.P('Year:', className='fix_label', style={'color': 'black',
                                                              'margin-top': '15px'}),

                 # # dcc.Slider(id='select_years',
                 # #           min=year_list[0],
                 # #           max=year_list[-1],
                 # #           value=year_list[1],
                 # #           step=1,
                 # #           included=False,
                 # #           updatemode='drag',
                 # #           tooltip={'always_visible': True},
                 # #           marks={str(yrs): str(yrs) for yrs in range(year_list[0], year_list[-1], 2)},
                 #           className='slider_component'),
                dcc.Slider(
                    id='select_years',
                    min=2016,
                    max=2021,
                    step=None,
                    value=2021,
                    marks={i: str(i) for i in range(2016, 2022)}
                ),
            ], className='container_slider'),
dcc.Graph(id='bar_graph',
                      config={'displayModeBar': 'hover'},
                      className='bar_graph_border',style={'border': '1px ridge black'}),
html.Div([    html.A('Know more ➤', href='https://datamind-documentation.netlify.app/barchart.html', target='_blank'),    ' about Bar Charts.'], style={'text-align': 'center', 'padding-top': '20px', 'font-size': '20px'})


]),
            ],width=6,style={'padding': '10px'}),
            #column 2
            dbc.Col([
                html.Div(id='calculations'),
            ],width=6 , style={'padding': '10px'}),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar_graph3',
                      config={'displayModeBar': 'hover'},
                      className='bar_graph_border',style={'border': '1px ridge black', 'background-color': '#f8f9fa'}),
html.Div([    html.A('Know more ➤', href='https://datamind-documentation.netlify.app/barchart.html', target='_blank'),    ' about Bar Charts.'], style={'text-align': 'center', 'padding-top': '20px', 'font-size': '20px'})
        ], width=6 , style={'padding': '10px'}),
        dbc.Col([
            dcc.Graph(id='bar_graph2',
                      config={'displayModeBar': 'hover'},
                      className='bar_graph_border',style={'border': '1px ridge black'}),
html.Div([    html.A('Know more ➤', href='https://datamind-documentation.netlify.app/barchart.html', target='_blank'),    ' about Bar Charts.'], style={'text-align': 'center', 'padding-top': '20px', 'font-size': '20px'})
        ], width=6 , style={'padding': '10px'})
    ]),
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Graph(id='pie_chart',
                          config={'displayModeBar': 'hover'},
                          className='bar_graph_border',style={'border': '1px ridge black'}),
html.Div([    html.A('Know more ➤', href='https://datamind-documentation.netlify.app/piechart.html', target='_blank'),    ' about Pie Charts.'], style={'text-align': 'center', 'padding-top': '20px', 'font-size': '20px'})

            ]),
        ], width=6, style={'padding': '10px'}),
        dbc.Col([
            html.Div([
                dcc.Graph(id='pie_chart2',
                          config={'displayModeBar': 'hover'},
                          className='bar_graph_border ',style={'border': '1px ridge black'}),
html.Div([    html.A('Know more ➤', href='https://datamind-documentation.netlify.app/piechart.html', target='_blank'),    ' about Pie Charts.'], style={'text-align': 'center', 'padding-top': '20px', 'font-size': '20px'})

            ]),

        ], width=6, style={'padding': '10px'})
    ]),
    dbc.Row([
        dbc.Row([
dbc.Row([
    html.Div([
        html.P(dcc.Markdown(
            """Graph Representing Performance of All **branches** Over The Years"""
        ), style={'line-height': '1', 'font-size': '25px', 'margin-bottom': '20px', 'text-align': 'center'}),
    ], style={'background-color': 'white', 'border-radius': '10px', 'border': '2px solid black', 'padding': '20px'}),
]),

            html.Div(id='selected-branch'),
        ],className='my-dropdown1'),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig1),
        ], width=9),

        dbc.Col([
           html.Div([
               html.H1(children='Analysis',style={'justify-content':'center','text-align': 'center','display': 'flex'}),

               # Display the best performing stream
               html.Div(
                   children=[
                       f"The best performing stream is {best_stream}",
                       html.I(className='fa-sharp fa-solid fa-user-tie',style={'padding':'10px'})
                   ],
                   style={'padding-top': '30px', 'font-size': '20px'}
               ),
               html.Div(
                   children=[
                       f"Highest average JEE percentile: {formatted_percentile} ",
                       html.Br(),
                       f"Year: ({formatted_year}) for {highest_branch} ",
                       html.I(className='fas fa-fire')
                   ]
               ,style={'padding-top':'40px','font-size':'20px'}),
               html.Div(
                   children=[
                       "The branch with the highest percentage change is:",
                       html.Br(),
                       highest_change,
                       " with a change of ",
                       round(percent_change[highest_change], 2),
                       " ",
                       html.I(className='fa-solid fa-percent')
                   ]
                   , style={'padding-top': '60px', 'font-size': '20px'}),
           ]),
        ],style={ 'background-image': 'url("https://wallpapercave.com/wp/wp6422920.jpg")',
    'background-size': 'cover',
    'background-repeat': 'no-repeat',
    'box-shadow': 'inset 0px 0px 10px 1px rgba(255, 255, 255, 0.5), inset 0px 0px 20px 1px rgba(255, 255, 255, 0.2), 0px 0px 10px 1px rgba(0, 0, 0, 0.5)',
    'color': 'white',},className='card',width=3),
    ],style={'padding':'20px'} ),
html.Div([    html.A('Know more ➤', href='https://datamind-documentation.netlify.app/linechart.html', target='_blank'),    ' about Line Charts.'], style={'text-align': 'center', 'padding-top': '20px', 'font-size': '20px'}),
    html.Div([
html.Div(
    [
        html.Img(src="assets/logo3.png", style={'display': 'block', 'margin': 'auto','height':'100px','width':'400px'})
    ],style={'text-align': 'center','padding':'20px'}
),
dbc.Row([
        dbc.Col([
            html.P("Select the first Axis",style={'font-size':'20px'}),
            dcc.Dropdown(
                id='my-dropdown1',
                className='dropdown',
                options=options1,
                value='sid',

            ),
        ]),
        dbc.Col([
            html.P("Select the second Axis", style={'font-size': '20px'}),
            dcc.Dropdown(
                id='my-dropdown2',
                options=options2,
                className='dropdown',
                value='x_perc',

            ),
        ]),
        dbc.Col([
            html.P("Select the Branch", style={'font-size': '20px'}),
            dcc.Dropdown(
                id='my-dropdown3',
                options=options,
                value='IT',
                className='dropdown',
                style={'width': '400px'}

            ),
        ]),
        dbc.Col([
                html.P("Select the Year", style={'font-size': '20px'}),
                    dcc.Slider(
                        id='my-slider',
                        min=2018,
                        max=2021,
                        step=None,
                        value=2021,
                        marks={i: str(i) for i in range(2018, 2022)}
                    ),
                ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph')
        ]),

dbc.Col([    html.H2('COUNT', style={'margin-top': '0', 'margin-bottom': '30px'}),    html.Div(id='output', style={'font-size': '20px'})], width=2, style={
    'background-image': 'url("https://wallpapercave.com/wp/wp6422920.jpg")',
    'background-size': 'cover',
    'background-repeat': 'no-repeat',
    'box-shadow': 'inset 0px 0px 10px 1px rgba(255, 255, 255, 0.5), inset 0px 0px 20px 1px rgba(255, 255, 255, 0.2), 0px 0px 10px 1px rgba(0, 0, 0, 0.5)',
    'color': 'white',
    'display': 'flex',
    'flex-direction': 'column',
    'justify-content': 'center',
    'align-items': 'center',
    'padding': '10px'
})

    ],style={'padding':'10px'}),
html.Div([    html.A('Know more ➤', href='https://datamind-documentation.netlify.app/histogram.html', target='_blank'),    ' about Histogram.'], style={'text-align': 'center', 'padding-top': '20px', 'font-size': '20px'}),

    ]),
    ],className='graph_generator',style={'border':'2px inset black','background-color':'#ECF0F1'}),
    dbc.Row([
        html.P(dcc.Markdown(
            """
            **Below map** shows the distribution of Students **accross** the city of ***Mumbai***
            """
        ), style={'line-height': '1', 'font-size': '25px',
                  'margin-left':'300px','margin-bottom': '20px'}),
        dbc.Col([html.Iframe(id='maps', srcDoc=open('heatmap.html', 'r').read(), width='100%', height='600',style={'border':'5px solid black','padding':'5px'}),]),
dbc.Col(
    [
        html.P(dcc.Markdown(
            """
            **Insights**
            """
        ), className="text2"),
dbc.Row([
    dbc.Col([
html.P(dcc.Markdown(
            """
            **Select Branch:**
            """
        ), className="text1"),
    ]),
    dbc.Col([
dcc.Dropdown(
            id='my-dropdown4',
            options=options,
            value='IT',
            className='dropdown',
            style={'width': '200px', 'padding-top': '10px','msrgin-left':'40px'}
        ),
    ]),
]),
dbc.Row([
    dbc.Col([
html.P(dcc.Markdown(
    """
    **Select Year:**
    """
), className="text1", style={"text-align": "left"})
    ]),
html.Div(
    dcc.Slider(
        id='my-slider2',
        min=2016,
        max=2021,
        step=None,
        value=2021,
        marks={i: str(i) for i in range(2016, 2022)}
    ),
    style={'width': '120%','color':'white'},
    className='slider-container'
)
]),
html.P(dcc.Markdown(
    """
   Below is the **Count** of the students for different regions of mumbai :
    """
), style={"text-align": "left",'padding-top':'40px'}),


        html.Div(id='calculations2',style={'padding-top':'20px'})
    ],
    width=3,
    style={
        'padding': '10px',
         'background-image': 'url("https://wallpapercave.com/wp/wp6422920.jpg")',
            'background-size': 'cover',
            'background-repeat': 'no-repeat',
            'box-shadow': 'inset 0px 0px 10px 1px rgba(255, 255, 255, 0.5), inset 0px 0px 20px 1px rgba(255, 255, 255, 0.2), 0px 0px 10px 1px rgba(0, 0, 0, 0.5)',
            'color': 'white',
    }
)

        ]),
html.Div([    html.A('Know more ➤', href='https://datamind-documentation.netlify.app/heatmap.html', target='_blank'),    ' about Density Heatmap.'], style={'text-align': 'center', 'padding-top': '20px', 'font-size': '20px'}),
    ],style={'padding':'20px'}),
    dbc.Row([
        html.Div(id='slider-output')
    ]),
    html.Div([
        html.H1("Data Analysis and Predictions",
                style={'margin-left': '300px', 'padding': '10px', 'font-size': '60px'}),
        dbc.Row([
            dbc.Col([
html.P(dcc.Markdown(
                    """
                    Below is  **Correlation** of Different Features of The **Dataset** amongst Itself
                    """
                ),style={'font-size':'20px'}),
                html.Div(id='MachineLearningAnalysis'),
                html.P(dcc.Markdown(
                    """
                    **Below ** is  the analysis of Students **data** for the above ***table***
                    """
                ), style={'justify-content': 'center','align-items': 'center','display': 'flex',}),
                html.Div(
                    id='MachineLearningAnalysis2',
                    className='MachineLearningAnalysis2',
                    style={
                        'background-color': 'white',
                        'border': '2px solid black',
                        'box-shadow': '5px 5px 5px grey',
                        'padding': '10px',
                        'margin': '10px',
                        'border-radius': '10px',
                    }
                ),
            ], className='MachineLearningAnalysis'),
            dbc.Col([
html.P(dcc.Markdown(
                    """
                    Below is  The ** Heamtmap of Correlation** of Different Features of The **Dataset** 
                    """
                ),style={'font-size':'20px'}),
                dbc.Card(dcc.Graph(id='heatmap'))
            ], className='heatmap'),

        ]),
        dbc.Row([
html.P(
    dcc.Markdown(
        """
        **Below** is the **Statistical Analysis** of the **Entire Dataset**
        """
    ),
    style={
        'font-size': '25px',
        'justify-content': 'center',
        'align-items': 'center',
        'display': 'flex',
        'background-color': 'white',
        'border-radius': '50px',
        'padding': '10px',
        'border': '2px solid black',
    }
),
            dbc.Col(
                dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in df_summary.columns],
                    data=df_summary.round(0).to_dict('records'),
                    style_table={'overflowX': 'scroll'},
                    style_cell={
                        'minWidth': '0px', 'maxWidth': '180px',
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                        'textAlign': 'center',
                        'fontFamily': 'Arial, sans-serif',
                        'fontSize': '12px',
                        'backgroundColor': '#f2f2f2'
                    },
                    style_header={
                        'backgroundColor': 'black',
                        'color': 'white',
                        'fontWeight': 'bold',
                        'textAlign': 'center',
                        'fontFamily': 'Arial, sans-serif',
                        'fontSize': '14px'
                    },
                ),
            ),
        ]),
    ], className='Data_analysis', style={'border': '5px solid black','padding':'10px'}),

    html.Footer(className=' footer text-center text-lg-start text-muted', style={'text-align': 'left', 'background-color': '#333333'}, children=[
        html.Section(className='', style={'padding': '5px'}, children=[
            html.Div(className='container text-center text-md-start mt-5', children=[
                html.Div(className='row mt-3', children=[
                    html.Div(className='col-md-3 col-lg-4 col-xl-3 mx-auto mb-4', children=[
                        html.Div(className='cell-sm-6 cell-lg-3 cell-xl-4', children=[
                            html.A(href='/index.html', children=[
                                html.Img(className='img-responsive', src='/assets/Datamind2.png', alt='DBIT', width='350', height='150')
                            ]),
                            html.P(className='offset-top-20 offset-md-top-35 inset-xl-right-30', style={'color': 'white', 'padding': '1rem', 'text-align': 'left'}, children=[
                                html.B(children='We are a specialized data company that offers a range of services related to data science, data analysis, data visualization, and machine learning.')
                            ])
                        ])
                    ]),
                    html.Div(className='col-md-3 col-lg-2 col-xl-2 mx-auto mb-4', style={'color': '#e5e5e5', 'margin-top': '2rem', 'text-align': 'left'}, children=[
                        html.H5(className='text-uppercase fw-bold mb-4', style={'text-align': 'center'}, children=[
                            html.B(children='quick links')
                        ]),
                        html.P(children=[
                            '>',
                            html.A(href='assets/aboutus .html', className='text-reset', style={'text-decoration': 'none', 'text-align': 'left'}, children=['ABOUT US'])
                        ]),
                        html.P(children=[
                            '>',
                            html.A(href='assets/docu.html', className='text-reset', style={'text-decoration': 'none', 'text-align': 'left'}, children=['ABOUT US'])
                        ]),
                        html.P(children=[
                            '>',
                            html.A(href='https://github.com/321dhruuv0037/python_mp', className='text-reset', style={'text-decoration': 'none', 'text-align': 'left'}, children=['CONTRIBUTORS'])
                        ])
                    ]),
                    html.Div(className='col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4', style={'color': '#e5e5e5', 'text-align': 'left'}, children=[
                        html.P(style={'text-align': 'left'}, children=[
                            html.B(html.H5(style={'text-align': 'left'}, children=['Capstone Data Company'])),
                            html.Br(),
                            '1st Floor, C Wing',
                            html.Br(),
                            'Don Bosco Institute Of Technology Premier Automobiles Road, Opp. Fiat Company, Kurla (W), Mumbai- 400 070',
                            html.Br(),
                               ]),


    ])
                    ]),
                   html.B(html.H5(style={'text-align': 'centre','margin-left':'330px'}, children=['Copyright 2023 © All rights reserved by Capstone Data Comapany'])),
                ])
            ])
        ])
])

@app.callback(Output('bar_graph2', 'figure'),
              [Input('select_years', 'value')])
def update_graph(value):
    df5 = df.groupby(['stream', 'year'])['parent_income'].mean().reset_index()
    df6 = df5[df5['year'] == value]

    return {
        'data': [
            go.Bar(
                x=df6['stream'],
                y=df6['parent_income'],
                text=df6['parent_income'],
                width=[0.4, 0.4, 0.4, 0.4],

                texttemplate='%{text:,.2s}',
                textposition='outside',
                marker=dict(color='#38D56F'),
                textfont=dict(
                    family="sans-serif",
                    size=12,
                    color='black'),
            )
        ],
        'layout': go.Layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            title={
                'text': '<b>Average Annual Parent Income branchwise (₹) in' + ' ' + str((value)),

                'y': 0.98,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': 'black',
                'size': 17},
            hovermode='closest',
            margin=dict(t=30, r=70),
            xaxis=dict(showline=True,
                       showgrid=False,
                       showticklabels=True,
                       linecolor='black',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='black')

                       ),

            yaxis=dict(title='<b>Average Parent Income (₹)</b>',
                       visible=True,
                       color='black',
                       showline=False,
                       showgrid=True,
                       )
        )
    }


@app.callback(Output('bar_graph', 'figure'),
              [Input('select_years', 'value')])
def update_graph(value):
    df3 = df.groupby(['stream', 'year'])['jee_perc'].max().reset_index()
    df4 = df3[df3['year'] == value]

    return {
        'data': [
            go.Bar(
                x=df4['stream'],
                y=df4['jee_perc'],
                width=[0.4,0.4,0.4,0.4],
                text=df4['jee_perc'],
                texttemplate='%{text:,.2s}',
                textposition='outside',
                marker=dict(color='#38D56F'),
                textfont=dict(
                    family="sans-serif",
                    size=12,
                    color='black'),
            )
        ],
        'layout': go.Layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            title={
                'text': '<b>Highest Percentile branchwise (%) in' + ' ' + str((value)),

                'y': 0.98,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': 'black',
                'size': 17},
            hovermode='closest',
            margin=dict(t=30, r=70),
            xaxis=dict(showline=True,
                       showgrid=False,
                       showticklabels=True,
                       linecolor='black',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='black')

                       ),

            yaxis=dict(title='<b>Highest Percentile (%)</b>',
                       visible=True,
                       color='black',
                       showline=False,
                       showgrid=True,
                       )
        )

    }
@app.callback(Output('pie_chart', 'figure'),
              [Input('select_years', 'value')])
def update_graph(value):
    df6 = df.groupby(['year', 'gender'])['sid'].count().reset_index()
    df7 = df6[df6['year'] == value]

    return {
        'data': [go.Pie(
            labels=df7['gender'],
            values=df7['sid'],
            hoverinfo='label+value+percent',
            textinfo='label+value',
            textfont=dict(size=13),
            texttemplate='%{label}: %{value:,.0f}<br>(%{percent})',
            textposition='auto',
            rotation=160
        )],
        'layout': go.Layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            title={
                'text': '<b>Gender Ratio In' + ' ' + str(value),

                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': 'rgb(50, 50, 50)',
                'size': 15},
            hovermode='x',
            legend={
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'xanchor': 'center',
                'yanchor': 'bottom',
                'x': 0.5,
                'y': -0.2
            }

        )
    }
@app.callback(Output('pie_chart2', 'figure'),
              [Input('select_years', 'value')])
def update_graph(value):
    df8 = df.groupby(['year','sector'])['sid'].count().reset_index()
    df9 = df8[df8['year'] == value]

    return {
        'data': [go.Pie(
            labels=df9['sector'],
            values=df9['sid'],
            hoverinfo='label+percent',

        )],
        'layout': go.Layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            title={
                'text': '<b>Sectorwise Split In Parents Job In' + ' ' + str(value),

                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': 'rgb(50, 50, 50)',
                'size': 14},
            hovermode='x',
            legend={
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'xanchor': 'center',
                'yanchor': 'bottom',
                'x': 0.5,
                'y': -0.5
            }

        )
    }
@app.callback(Output('bar_graph3', 'figure'),
              [Input('select_years', 'value')])
def update_graph(value):
    df10 = df.groupby(['quota', 'year'])['jee_perc'].max().reset_index()
    df11 = df10[df10['year'] == value]

    return {
        'data': [
            go.Bar(
                x=df11['quota'],
                y=df11['jee_perc'],
                width=[0.3,0.3],
                text=df11['jee_perc'],
                texttemplate='%{text:,.2s}',
                textposition='outside',
                marker=dict(color='#38D56F'),
                textfont=dict(
                    family="sans-serif",
                    size=12,
                    color='black'),
            )
        ],
        'layout': go.Layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            title={
                'text': '<b>Average Marks Scored By Minority And Non Minority Students in' + ' ' + str((value)),

                'y': 0.98,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': 'black',
                'size': 15},
            hovermode='closest',
            margin=dict(t=30, r=70),
            xaxis=dict(showline=True,
                       showgrid=False,
                       showticklabels=True,
                       linecolor='black',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='black')

                       ),

            yaxis=dict(title='<b>Average marks (%)</b>',
                       visible=True,
                       color='black',
                       showline=False,
                       showgrid=True,
                       )
        )
    }


@app.callback(
    Output('calculations', 'children'),
    [Input('select_years', 'value')]
)
def display_data(value):
    #This code first filters the dataframe df to only include rows where the year is 2019. Then, it groups the resulting dataframe by sector and counts the number of occurrences of sid in each group. The resulting dataframe df_genre has columns sector and sid.
    #, the code uses idxmax() to find the row index of the row with the maximum value of sid, and then selects the sector value from that row using .loc[]. The resulting df_genre2 should be the sector with the highest count of sid for the year 2019.
    df_year = df[df['year'] == value]

    df_genre = df_year.groupby(['sector'])['sid'].count().reset_index()
    df_genre2 = df_genre.loc[df_genre['sid'].idxmax(), 'sector']
    df13 = df_year.groupby(['stream', 'year'])['jee_perc'].max().reset_index()
    df14 = df13.loc[df13['jee_perc'].idxmax(), 'jee_perc']
    df15 = df_year.groupby(['stream', 'year'])['jee_perc'].mean().reset_index()
    df16 = df15.loc[df15['jee_perc'].idxmax(), 'jee_perc']
    df17 = df.groupby(['stream', 'year'])['parent_income'].mean().reset_index()
    df18 = df17.loc[df17['parent_income'].idxmax(), 'parent_income']
    df19 = df_year.groupby(['stream', 'year'])['sid'].count().reset_index()
    df20 = df19.loc[df19['sid'].idxmax(), 'stream']
    df21 = df_year.groupby(['stream', 'year'])['sid'].count().reset_index()
    df22 = df21.loc[df21['sid'].idxmax(), 'sid']
    df23 = df_year.groupby(['stream', 'year'])['x_perc'].mean().reset_index()
    df24 = df23.loc[df23['x_perc'].idxmax(), 'x_perc']
    df25 = df_year.groupby(['stream', 'year'])['xii_perc'].mean().reset_index()
    df26 = df25.loc[df25['xii_perc'].idxmax(), 'xii_perc']
    df27 = df_year.groupby(['stream', 'year'])['maths_xii'].mean().reset_index()
    df28 = df27.loc[df27['maths_xii'].idxmax(), 'maths_xii']
    df29 = df_year.groupby(['stream', 'year'])['physics_xii'].mean().reset_index()
    df30 = df29.loc[df29['physics_xii'].idxmax(), 'physics_xii']
    df31 = df_year.groupby(['stream', 'year'])['chem_xii'].mean().reset_index()
    df32 = df31.loc[df31['chem_xii'].idxmax(), 'chem_xii']

    # Format the data for display

    # Return the formatted data as a table
    return [html.Table(
        [html.Thead([html.Tr([html.Th('columns'), html.Th('Symbol'), html.Th('Information')], className='header_hover')
                     ]),
         html.Tbody([
             html.Tr([
                 html.Td('Sector in which most parents were employed'),
                 html.Td(html.I(className='fa-solid fa-briefcase', style={'font-size': '150%'})),
                 html.Td('{:s}'.format(df_genre2))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Highest percentile in jee mains'),
                 html.Td(html.I(className='fa-solid fa-star', style={'font-size': '150%'})),
                 html.Td('{0:,.2f}'.format(df14))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Average Percentile In Jee Mains'),
                 html.Td(html.I(className='fa-solid fa-star-half-stroke', style={'font-size': '150%'})),

                 html.Td('{0:,.2f}%'.format(df16))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Average Annual Parent Income'),
                 html.Td(html.I(className='fa-sharp fa-solid fa-indian-rupee-sign',
                                style={'font-size': '150%', 'padding': '5px'})),

                 html.Td('₹{0:,.2f}'.format(df18))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Branch With Most Number Of Students'),
                 html.Td(html.I(className='fa-sharp fa-solid fa-school',
                                style={'font-size': '150%', 'padding': '5px'})),

                 html.Td('{:s}'.format(df20))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Most Number Of Students In A Branch'),
                 html.Td(html.I(className='fa-sharp fa-solid fa-user',
                                style={'font-size': '150%', 'padding': '5px'})),

                 html.Td('{0:,.2f}'.format(df22))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Average Marks Scored In Class xth'),
                 html.Td(html.I(className='fa-sharp fa-solid fa-percent',
                                style={'font-size': '150%', 'padding': '5px'})),

                 html.Td('{0:,.2f}%'.format(df24))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Average Marks Scored In Class xiith'),
                 html.Td(html.I(className='fa-sharp fa-solid fa-crosshairs',
                                style={'font-size': '150%', 'padding': '5px'})),

                 html.Td('{0:,.2f}%'.format(df26))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Average Marks Scored In Class xiith maths'),
                 html.Td(html.I(className='fa-sharp fa-solid fa-calculator',
                                style={'font-size': '150%', 'padding': '5px'})),

                 html.Td('{0:,.2f}%'.format(df28))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Average Marks Scored In Class xiith physics'),
                 html.Td(html.I(className='fa-sharp fa-solid fa-atom',
                                style={'font-size': '150%', 'padding': '5px'})),

                 html.Td('{0:,.2f}%'.format(df30))
             ], className='hover_only_row'),
             html.Tr([
                 html.Td('Average Marks Scored In Class xiith chemistry'),
                 html.Td(html.I(className='fa-sharp fa-solid fa-vial-circle-check',
                                style={'font-size': '150%', 'padding': '5px'})),

                 html.Td('{0:,.2f}%'.format(df32))
             ], className='hover_only_row'),
         ])
         ], className='table_style')
    ]
@app.callback(
    Output('MachineLearningAnalysis', 'children'),
    [Input('select_years', 'value')]
)
def display_data(value):
    #This code first filters the dataframe df to only include rows where the year is 2019. Then, it groups the resulting dataframe by sector and counts the number of occurrences of sid in each group. The resulting dataframe df_genre has columns sector and sid.
    #, the code uses idxmax() to find the row index of the row with the maximum value of sid, and then selects the sector value from that row using .loc[]. The resulting df_genre2 should be the sector with the highest count of sid for the year 2019.
    df = pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/slider.csv")
    df_year = df[df['year'] == value]
    X = df_year[['x_perc', 'xii_perc', 'cet_perc', 'physics_xii', 'chem_xii', 'maths_xii']]
    Y = df_year['jee_perc']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=101)
    lm = LinearRegression()
    lm.fit(X_train, Y_train)
    random_names = ['xth percentage', 'xii th percentage', 'cet percentage', 'physics xii th percentage',
                    ' chemistry xii th percentage', 'maths xii th percentage']
    coef_names = dict(zip(X.columns, random_names))
    df = pd.DataFrame(lm.coef_, index=[coef_names[col] for col in X.columns], columns=['JEE Percentile'])
    df.columns = ['JEE Percentile']

    return [html.Table([html.Thead(html.Tr([html.Th(col) for col in df.columns])
                                   ),
                        html.Tbody([
                            html.Tr([
                                html.Td(df.index[i]),
                                html.Td("{:.2f}".format(df['JEE Percentile'][i]))
                            ]) for i in range(len(df))
                        ], className='hover_only_row')
                        ], className='table_style')
            ]

@app.callback(
    Output('heatmap', 'figure'),
    [Input('select_years', 'value')]
)
def update_heatmap(selected_columns):
    # Get selected range of columns


    # Create correlation matrix
    df = pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/slider1.csv")
    corr_matrix = df.corr()

    # Create heatmap trace
    trace = go.Heatmap(
        x=corr_matrix.columns,
        y=corr_matrix.columns[::-1],
        z=corr_matrix.values[::-1],
        colorscale='RdBu',
        colorbar=dict(title='Correlation')
    )

    # Set layout
    layout = go.Layout(
        title='Heatmap of Correlation',
        xaxis=dict(title='Columns'),
        yaxis=dict(title='Columns')
    )

    # Create figure
    fig = go.Figure(data=[trace], layout=layout)

    return fig


@app.callback(
    Output('MachineLearningAnalysis2', 'children'),
    [Input('select_years', 'value')]
)
def display_data(value):
    df = pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/slider.csv")
    df_year = df[df['year'] == value]
    X = df_year[['x_perc', 'xii_perc', 'cet_perc', 'physics_xii', 'chem_xii', 'maths_xii']]
    Y = df_year['jee_perc']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=101)
    lm = LinearRegression()
    lm.fit(X_train, Y_train)
    df = pd.DataFrame(lm.coef_, X.columns, columns=['jee percentile'])
    df = df.rename(index={'x_perc': 'xth percentage', 'xii_perc': 'xii th percentage', 'cet_perc': 'cet percentile', 'physics_xii': 'physics percentage xii',
                          'chem_xii': 'chemistry percentage xii', 'maths_xii': 'maths percentage xii'})

    # Iterate through each row in the DataFrame and check whether the coefficient is positive or negative
    result = []
    for i in range(len(df)):
        coefficient = df['jee percentile'][i]
        feature = df.index[i]
        if coefficient > 0:
            result.append(html.P(
                [html.Strong("Percentage increase in JEE percent"), f" has a ",html.Strong("positive"),f" impact on ", html.Strong(feature),
                 f" and it increases by: {coefficient:.2f}%"], style={'margin': '10px 0'}))
        elif coefficient < 0:
            result.append(html.P(
                [html.Strong("Percentage increase in JEE percent"), f" has a ",html.Strong("negative"),f" impact on ", html.Strong(feature),
                 f" and it decreases by: {coefficient:.2f}%"], style={'margin': '10px 0'}))
        else:
            result.append(html.P([html.Strong("Percentage increase in JEE percent"), f" has ",html.Strong("no"),f" impact on ", html.Strong(feature)], style={'margin': '10px 0'}))

    return result
@app.callback(
    Output('graph', 'figure'),
    [Input('my-slider', 'value')],
    [Input('my-dropdown3', 'value')],
    [Input('my-dropdown1', 'value')],
    [Input('my-dropdown2', 'value')])

def update_graph(selected_year, selected_stream, dropdown1_value, dropdown2_value):
    # Filter data based on selected year and stream
    # df['sid'] = df['sid'].astype(str)
    if(selected_stream == 'none'):
        filtered_df = df[df['year'] == selected_year]
        if (dropdown1_value == 'x_perc' and dropdown2_value == 'xii_perc') or (
                dropdown1_value == 'xii_perc' and dropdown2_value == 'x_perc'):
            fig = go.Figure(data=go.Scatter(x=filtered_df['sid'], y=filtered_df['jee_perc'], mode='markers'))
        elif (dropdown1_value == 'sid' and dropdown2_value == 'x_perc') or (
                dropdown1_value == 'x_perc' and dropdown2_value == 'sid'):
            fig = px.histogram(filtered_df, x='x_perc', nbins=10, labels={'x_perc': 'Xth Percentage'},
                               color_discrete_sequence=['#EB89B5'], opacity=0.8)
            fig.update_layout(
                title_text='Sampled Results',  # title of plot
                xaxis_title_text='Value',  # xaxis label
                yaxis_title_text='Count',  # yaxis label
                bargap=0.1,  # gap between bars of adjacent location coordinates
                bargroupgap=0.1  # gap between bars of the same location coordinates
            )

        elif (dropdown1_value == 'xii_perc' and dropdown2_value == 'jee_perc') or (
                dropdown1_value == 'jee_perc' and dropdown2_value == 'xii_perc'):
            fig = px.scatter(filtered_df, x='xii_perc', y='jee_perc', labels={'sid': 'SID', 'x_perc': 'X percentile'},
                             color='stream')
        elif (dropdown1_value == 'jee_perc' and dropdown2_value == 'sid') or (
                dropdown1_value == 'sid' and dropdown2_value == 'jee_perc'):
            fig = px.histogram(filtered_df, x='jee_perc', nbins=10, labels={'jee_perc': 'jee percentile'},
                               color_discrete_sequence=['#EB89B5'], opacity=0.8, )
            fig.update_layout(
                title_text='Sampled Results',  # title of plot
                xaxis_title_text='Value',  # xaxis label
                yaxis_title_text='Count',  # yaxis label
                bargap=0.1,  # gap between bars of adjacent location coordinates
                bargroupgap=0.1  # gap between bars of the same location coordinates
            )
        elif (dropdown1_value == 'xii_perc' and dropdown2_value == 'sid') or (
                dropdown1_value == 'sid' and dropdown2_value == 'xii_perc'):
            fig = px.histogram(filtered_df, x='xii_perc', nbins=10, labels={'xii_perc': 'XII TH PERCENTAGE'},
                               color_discrete_sequence=['#EB89B5'], opacity=0.8, )
            fig.update_layout(
                title_text='Sampled Results',  # title of plot
                xaxis_title_text='Value',  # xaxis label
                yaxis_title_text='Count',  # yaxis label
                bargap=0.1,  # gap between bars of adjacent location coordinates
                bargroupgap=0.1  # gap between bars of the same location coordinates
            )
        else:
            fig = go.Figure()

    else:
        df3 = df[df['year'] == selected_year]
        filtered_df = df3[df3['stream'] == selected_stream]
        if (dropdown1_value == 'x_perc' and dropdown2_value == 'xii_perc') or (
                dropdown1_value == 'xii_perc' and dropdown2_value == 'x_perc'):
            fig = px.scatter(filtered_df, x='x_perc', y='jee_perc',labels={'x_perc': 'XTH PERCENTAGE', 'jee_perc': 'JEE PERCENTILE'},
                             color='stream')
            fig.update_layout(xaxis_title='XTH PERCENTAGE', yaxis_title='JEE percentile')
        elif (dropdown1_value == 'sid' and dropdown2_value == 'x_perc') or (
                dropdown1_value == 'x_perc' and dropdown2_value == 'sid'):
            fig = px.histogram(filtered_df, x='x_perc', nbins=10, labels={'x_perc': 'Xth Percentage'},
                               color_discrete_sequence=['#EB89B5'], opacity=0.8, )
            fig.update_layout(
                title_text='Sampled Results',  # title of plot
                xaxis_title_text='Value',  # xaxis label
                yaxis_title_text='Count',  # yaxis label
                bargap=0.1,  # gap between bars of adjacent location coordinates
                bargroupgap=0.1  # gap between bars of the same location coordinates
            )
        elif (dropdown1_value == 'xii_perc' and dropdown2_value == 'jee_perc') or (
                dropdown1_value == 'jee_perc' and dropdown2_value == 'xii_perc'):
            fig = px.scatter(filtered_df, x='xii_perc', y='jee_perc', labels={'xii_perc': 'XII PERCENTAGE', 'jee_perc': 'JEE PERCENTILE'},
                             color='stream')
            fig.update_layout(xaxis_title='XII percentile', yaxis_title='JEE percentile')
        elif (dropdown1_value == 'jee_perc' and dropdown2_value == 'sid') or (
                dropdown1_value == 'sid' and dropdown2_value == 'jee_perc'):
            fig = px.histogram(filtered_df, x='jee_perc', nbins=10, labels={'jee_perc': 'jee percentile'},
                               color_discrete_sequence=['#EB89B5'], opacity=0.8, )
            fig.update_layout(
                title_text='Sampled Results',  # title of plot
                xaxis_title_text='Value',  # xaxis label
                yaxis_title_text='Count',  # yaxis label
                bargap=0.1,  # gap between bars of adjacent location coordinates
                bargroupgap=0.1  # gap between bars of the same location coordinates
            )
        elif (dropdown1_value == 'xii_perc' and dropdown2_value == 'sid') or (
                dropdown1_value == 'sid' and dropdown2_value == 'xii_perc'):
            fig = px.histogram(filtered_df, x='xii_perc', nbins=10, labels={'xii_perc': 'XII TH PERCENTAGE'},
                               color_discrete_sequence=['#EB89B5'], opacity=0.8, )
            fig.update_layout(
                title_text='Sampled Results',  # title of plot
                xaxis_title_text='Value',  # xaxis label
                yaxis_title_text='Count',  # yaxis label
                bargap=0.1,  # gap between bars of adjacent location coordinates
                bargroupgap=0.1  # gap between bars of the same location coordinates
            )
        else:
            fig = go.Figure()
    # Define data and layout for different graph types

    # Set layout for all graph types
    fig.update_layout(title_text='{} Graph: {} vs {}'.format(selected_stream, dropdown1_value, dropdown2_value))

    # Return the figure
    return fig
@app.callback(
    Output('output', 'children'),
    [Input('my-slider', 'value')],
    [Input('my-dropdown3', 'value')])
def update_output(selected_year, selected_stream):
    if selected_stream == 'none':
        df_filtered = df[df['year'] == selected_year]
        count = len(df_filtered)
        return f'Total students in {selected_year}: {count}'
    else:
        df_filtered = df[(df['year'] == selected_year) & (df['stream'] == selected_stream)]
        count = len(df_filtered)
        return f'Total students in {selected_stream} branch in {selected_year}: {count}'
@app.callback(
    Output('calculations2', 'children'),
    [Input('my-slider2', 'value')],
    [Input('my-dropdown4', 'value')])
def update_output(selected_year, selected_stream):
    if selected_stream == 'none':
        df_filtered = df[df['year'] == selected_year]
        df_filtered1 = df_filtered.groupby('line').count().reset_index()
        df_filtered2 = df_filtered1.loc[df_filtered1['jee_perc'].idxmax(), 'jee_perc']
        central_count = df_filtered[df_filtered['line'] == 'central']['line'].count()
        western_count = df_filtered[df_filtered['line'] == 'western']['line'].count()
        harbour_count = df_filtered[df_filtered['line'] == 'harbour']['line'].count()

        return [html.Table(
            [html.Thead(
                [html.Tr([html.Th('CENTRAL'), html.Th('WESTERN'), html.Th('HARBOUR')], className='header_hover')
                 ]),
             html.Tbody([
                 html.Tr([
                     html.Td('{:d}'.format(int(central_count))),
                     html.Td('{:d}'.format(int(western_count))),
                     html.Td('{:d}'.format(int(harbour_count)))
                 ], className='hover_only_row')
             ])
             ], className='table_style')
        ]
    else:
        df_filtered = df[(df['year'] == selected_year) & (df['stream'] == selected_stream)]
        central_count = df_filtered[df_filtered['line'] == 'central']['line'].count()
        western_count = df_filtered[df_filtered['line'] == 'western']['line'].count()
        harbour_count = df_filtered[df_filtered['line'] == 'harbour']['line'].count()
        return [html.Table(
            [html.Thead(
                [html.Tr([html.Th('CENTRAL'), html.Th('WESTERN'), html.Th('HARBOUR')], className='header_hover')
                 ]),
                html.Tbody([
                    html.Tr([
                        html.Td('{:d}'.format(int(central_count))),
                        html.Td('{:d}'.format(int(western_count))),
                        html.Td('{:d}'.format(int(harbour_count)))
                    ], className='hover_only_row')
                ])
            ], className='table_style')
        ]

@app.callback(
    Output('slider-output', 'children'),
    [Input('select_years', 'value')]
)
def update_output(value):
    # Update the heatmap data based on the slider value
    nwdf100 = pd.read_csv('coords.csv')
    df = nwdf100[nwdf100['year'] == value]
    # Group the data by location and count the number of students for each location
    data = df.groupby(['name', 'latitude', 'longitude'])['pincode'].count().reset_index()
    # .reset_index()
    data.columns = ['name', 'latitude', 'longitude', 'number_of_students']

    # Create a map centered on a specific location
    m = folium.Map(location=[18.932245, 72.826439], zoom_start=10)

    marker_cluster = MarkerCluster().add_to(m)

    area_group = FeatureGroupSubGroup(marker_cluster, 'Area')

    # Filter the data for the area you're interested in
    area_data = data[(data['latitude'] >= 0.0) & (data['longitude'] >= 0.0)]

    # Loop through the data and create a marker for each point
    for index, row in area_data.iterrows():
        tooltip = "Number of students: {}".format(row['number_of_students'])
        folium.Marker(location=[row['latitude'], row['longitude']], tooltip=tooltip).add_to(area_group)

        # Add the FeatureGroupSubGroup to the map
    area_group.add_to(m)

    # Create a heatmap layer from the data
    heat_data = [[row['latitude'], row['longitude']] for index, row in data.iterrows()]
    heatmap = HeatMap(heat_data, name='Heatmap')

    # Add the heatmap layer to the map
    heatmap.add_to(m)
    # text marker

    # Add a layer control to the map
    folium.LayerControl().add_to(m)
    # western line
    folium.PolyLine([(18.9354, 72.8262), (18.9442, 72.8239), (18.9536, 72.8174), (18.9591, 72.8132), (18.9696, 72.8196),
                     (18.9827, 72.8193)
                        , (19.0088, 72.8308)
                        , (19.0111, 72.8403)
                        , (19.0173, 72.8426)
                        , (19.0271, 72.8464)
                        , (19.0395, 72.8445)
                        , (19.0544, 72.8402)
                        , (19.0686, 72.8394)
                        , (19.0814, 72.8416)
                        , (19.0972, 72.8445)
                        , (19.1197, 72.8464)
                        , (19.1365, 72.8497)
                        , (19.1542, 72.8534)
                        , (19.1647, 72.8491)
                        , (19.1867, 72.8486)
                        , (19.204431413672715, 72.85164270837505)
                        , (19.2292, 72.8572)
                        , (19.2502, 72.8592)
                        , (19.2813, 72.8563)
                        , (19.3103, 72.8517)
                        , (19.3465, 72.8545)
                        , (19.3802, 72.8395)
                        , (19.4186, 72.8179)
                        , (19.455235541869268, 72.81211431208968), (19.519096449558383, 72.85036910889094),
                     (19.577117893783946, 72.82171623907293), (19.6982688067134, 72.772179156276),
                     (19.990148370578478, 72.74472504650069)], color="green", tooltip="Western Line", weight=3).add_to(
        m)

    folium.Marker(location=[19.455134379429648, 72.81202848139804],
                  popup=folium.Popup('<i>Western Line</i>'),
                  tooltip='Western Line',
                  icon=folium.DivIcon(html="""Western Line""",
                                      class_name="mapText"),
                  ).add_to(m)

    # inject html into the map html
    m.get_root().html.add_child(folium.Element("""
    <style>
    .mapText {
        white-space: nowrap;
        color:green;
        font-size:medium
    }
    </style>
    """))
    # csmt to kasara
    folium.PolyLine(
        [(18.943888, 72.835991), (18.994736760414902, 72.83299728510069), (19.020330448510123, 72.84365954445657),
         (19.066573611668673, 72.87980951393833), (19.085515812592636, 72.90727222557408),
         (19.18659041458438, 72.97536110837471), (19.19042930746032, 73.02342671394041),
         (19.18871434223293, 73.04228938324867), (19.23571726600612, 73.13078415340435),
         (19.29602463586944, 73.20378245441398), (19.439762665560814, 73.30787021023416),
         (19.64852859016493, 73.47304712558349)], color="blue", tooltip="Central Line").add_to(m)
    # kalyan to khopoli
    folium.PolyLine([(19.23571726600612, 73.13078415340435), (19.16699440588468, 73.23863896084042),
                     (18.91283348037467, 73.3207955409171), (18.789286786303602, 73.34539545440576)], color="blue",
                    tooltip="Central Line").add_to(m)
    folium.Marker(location=[19.23644145356165, 73.13028936975887],
                  popup=folium.Popup('<i>Central Line</i>'),
                  tooltip='Central Line',
                  icon=folium.DivIcon(html="""Central Line""",
                                      class_name="mapText"),
                  ).add_to(m)
    # harbour csmt to panvel
    folium.PolyLine([(18.940295750335533, 72.83575288324467), (18.962173966262736, 72.83900556789912),
                     (18.988393871718458, 72.84329590608344), (19.0162622023617, 72.85879774048796),
                     (19.067444858086915, 72.8800346016453), (19.048343621374624, 72.93196402557346),
                     (19.06339879342969, 72.99882074488211), (19.055727544411585, 73.017959166992),
                     (19.02220959140532, 73.0189194026994), (19.01947799290236, 73.03948562689445),
                     (19.02666691178611, 73.05961378456648), (19.008516434583814, 73.09459223336893),
                     (18.992155097791116, 73.12093264019435)], color="yellow", tooltip="Harbour Line").add_to(m)
    # harbor wadala to goregaon
    folium.PolyLine([(19.0162622023617, 72.85879774048796), (19.041049756832933, 72.84699720172428),
                     (19.056530893119035, 72.83989345615814), (19.068513041300847, 72.8399588909093),
                     (19.164918718417084, 72.84922634833158)], color="yellow", tooltip="Harbour Line").add_to(m)
    # metro line 9 gkp-vsv
    folium.PolyLine([(19.08680000156715, 72.90811058324704), (19.09658860912144, 72.89500762742944),
                     (19.10809761674883, 72.87981916604637), (19.121114420719188, 72.8482312390653),
                     (19.130568159099553, 72.82134052371956)], color="cyan", tooltip="Metro Line 9").add_to(m)
    # thane vashi line
    folium.PolyLine([(19.18675254065755, 72.97540402372054), (19.176037824932855, 72.99472545441198),
                     (19.103518084649536, 73.01215414724949), (19.07580016180758, 73.01782716790103),
                     (19.06339879342969, 72.99882074488211)], color="purple", tooltip="TransHarbour Line").add_to(m)

    # inject html into the map html
    m.get_root().html.add_child(folium.Element("""
    <style>
    .mapText {
        white-space: nowrap;
        color:green;
        font-size:medium
    }
    </style>
    """))
    folium.LayerControl(overlay={
        'Markers': '<span style="color: green">Western Line</span> | <span style="color: blue">Central Line</span> | <span style="color: yellow">Harbour Line</span>',
    }).add_to(m)

    # Save the map to an HTML file
    m.save('heatmap.html')

    return ''
if __name__ == '__main__':
    app.run_server(debug=True)
