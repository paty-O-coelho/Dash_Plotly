# import numpy as np
# import plotly.offline as pyo
# import plotly.graph_objs as go
#
# np.random.seed(42)
# random_x = np.random.randint(1,101,100)
# random_y = np.random.randint(1,101,100)
#
# data = [go.Scatter(x=random_x, y=random_y,mode='markers')]
# layout = go.Layout(title='Hello Dash',
#                     xaxis = {'title': 'My X axis'},
#                     yaxis=dict(title='My Yaxis'),
#                     hovermode = 'closest')
# fig = go.Figure(data=data, layout=layout)
#
# pyo.plot(fig,filename='scatter.html')
#######
# This line chart shows U.S. Census Bureau
# population data from six New England states.
######

#######
# This line chart shows U.S. Census Bureau
# population data from six New England states.
# THIS PLOT USES PANDAS TO EXTRACT DESIRED DATA FROM THE SOURCE
######
# import plotly.offline as pyo
# import plotly.graph_objs as go
# import pandas as pd

# df = pd.read_csv('nst-est2017-alldata.csv')
# # Alternatively:
# # df = pd.read_csv('https://www2.census.gov/programs-surveys/popest/datasets/2010-2017/national/totals/nst-est2017-alldata.csv')

# # grab just the six New England states:
# df2 = df[df['DIVISION']=='1']
# # set the index to state name:
# df2.set_index('NAME', inplace=True)
# # grab just the population columns:
# df2 = df2[[col for col in df2.columns if col.startswith('POP')]]

# traces=[go.Scatter(
#     x = df2.columns,
#     y = df2.loc[name],
#     mode = 'markers+lines',
#     name = name
# ) for name in df2.index]

# layout = go.Layout(
#     title = 'Population Estimates of the Six New England States'
# )

# fig = go.Figure(data=traces,layout=layout)
# pyo.plot(fig, filename='line3.html')

import dash_html_components as html

print(help(html.Div))