import plotly.express as px
import pandas as pd

df = pd.read_csv('slider.csv')
max_df = df.groupby(['year', 'stream'])['jee_perc'].mean().reset_index()
fig = px.line(max_df, x='year', y='jee_perc', color='stream', title='Average Percentile by Year and Stream')

fig.show()