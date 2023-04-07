import csv
import os
import base64
import io
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.exceptions import PreventUpdate
import plotly.graph_objs as go

app = dash.Dash(__name__)
df =pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/slider.csv")

# Define the layout of the app
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Upload File', children=[
            html.H1("Upload Your CSV File"),
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '50%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=False
            ),
            html.Div(id='output-data-upload')
        ]),
        dcc.Tab(label='View Data', id='view-tab', disabled=True, children=[
            html.H1('View Data'),
            html.Div(id='table-container'),
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
        ])
    ])
])


def check_columns(df):
    # Define your column conditions here
    # For example, if your CSV file should have columns 'A', 'B', and 'C'
    # you can check that with the following code:
    required_columns = ['sid', 'stream', 'name', 'mob_no', 'email', 'gender', 'x_perc', 'xii_perc', 'cet_perc',
                        'physics_xii', 'chem_xii', 'maths_xii', 'jee_perc', 'father_name', 'father_occupation',
                        'mother_name', 'mother_occupation', 'parent_income', 'pincode', 'year', 'sector', 'quota',
                        'longitude', 'latitude', 'line', 'hmap']
    missing_columns = set(required_columns) - set(df.columns)
    if len(missing_columns) > 0:
        return False
    return True


def save_file(contents, filename):
    # Decode the contents of the uploaded file
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    # Convert the decoded bytes into a pandas dataframe
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    # Check if the file satisfies the column conditions
    if not check_columns(df):
        raise ValueError('Uploaded CSV file does not meet the required column conditions')
    # Save the file as slider.csv in the server's file system
    file_path = os.path.join(os.getcwd(), 'slider.csv')
    df.to_csv(file_path, index=False)
    file_path = os.path.join(os.getcwd(), 'slider.csv')
    if os.path.exists(file_path):
        # Append the new data to the existing file
        existing_df = pd.read_csv(file_path)
        df = pd.concat([existing_df, df], ignore_index=True)
    df.to_csv(file_path, index=False)
    return f'Successfully saved {filename} as slider.csv'


@app.callback(
    [dash.dependencies.Output('output-data-upload', 'children'),
     dash.dependencies.Output('view-tab', 'disabled')],
    [dash.dependencies.Input('upload-data', 'contents')],
    [dash.dependencies.State('upload-data', 'filename')]
)
def update_output(contents, filename):
    if contents is None:
        raise PreventUpdate
    try:
        message = save_file(contents, filename)
        return [html.Div([html.Div('File uploaded successfully!'), html.Br(), html.Div(message)]), False]
    except Exception as e:
        return [html.Div([
            html.Div('An error occurred while uploading the file:'),
            html.Br(),
            html.Div(str(e))
        ]), True]

    @app.callback(Output('bar_graph', 'figure'),
                  [Input('select_years', 'value')])
    def update_graph(value):
        dfnew=pd.read_csv("C:/Users/adity/PycharmProjects/pythonProject1/slider.csv")
        df3 = dfnew.groupby(['stream', 'year'])['jee_perc'].max().reset_index()
        df4 = df3[df3['year'] == value]

        return {
            'data': [
                go.Bar(
                    x=df4['stream'],
                    y=df4['jee_perc'],
                    width=[0.4, 0.4, 0.4, 0.4],
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

if __name__ == '__main__':
        app.run_server(debug=True)
