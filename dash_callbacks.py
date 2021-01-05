import dash
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output
from pandas._config.config import options
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd 

df = pd.read_csv('gapminderDataFiveYear.csv')

app =  dash.Dash()

year_option = []
for year in df['year'].unique():
    year_option.append({'label':str(year), 'value':year})

app.layout = html.Div([
        dcc.Graph(id='graph'),
        dcc.Dropdown(id='year-picker', options=year_option,
                     value=df['year'].min() )
])
                
@app.callback(Output('graph', 'figure'),
             [Input('year-picker', 'value')])
def update_figure(selected_year):
    df = pd.read_csv('gapminderDataFiveYear.csv')
    filtered_df = df[df['year'] == selected_year]
    fig = go.Figure()
    traces = []
    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name]
        traces.append(go.Scatter(
        x = df_by_continent['gdpPercap'],
        y = df_by_continent['lifeExp'],
        mode = 'markers',
        opacity = 0.7,
        marker = {'size': 15},
        name = continent_name
        )    
     )
    
    return {'data':traces,
           'layout':go.Layout(title = 'My Plot',
                             xaxis={'title':'GDP Per Cap','type':'log'},
                             yaxis = {'title': 'Life Expectancy'})}
'''
        fig = px.line(df, x=df_by_continent['gdpPercap'], y=df_by_continent['lifeExp'], title='Life expectancy in Canada')
    return [fig]
'''

if __name__ == '__main__':
    app.run_server()