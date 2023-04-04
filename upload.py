import csv
import os
import base64
import io
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
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
])

def check_columns(df):
    # Define your column conditions here
    # For example, if your CSV file should have columns 'A', 'B', and 'C'
    # you can check that with the following code:
    required_columns = ['sid', 'stream', 'name', 'mob_no', 'email', 'gender', 'x_perc', 'xii_perc', 'cet_perc', 'physics_xii', 'chem_xii', 'maths_xii', 'jee_perc', 'father_name', 'father_occupation', 'mother_name', 'mother_occupation', 'parent_income', 'pincode', 'year', 'sector', 'quota', 'longitude', 'latitude', 'line', 'hmap']
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
    dash.dependencies.Output('output-data-upload', 'children'),
    [dash.dependencies.Input('upload-data', 'contents')],
    [dash.dependencies.State('upload-data', 'filename')]
)
def update_output(contents, filename):
    if contents is None:
        raise PreventUpdate
    try:
        message = save_file(contents, filename)
        return html.Div([
            html.Div('File uploaded successfully!'),
            html.Br(),
            html.Div(message)
        ])
    except Exception as e:
        return html.Div([
            html.Div('An error occurred while uploading the file:'),
            html.Br(),
            html.Div(str(e))
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
