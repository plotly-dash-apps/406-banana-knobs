import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import plotly.figure_factory as ff
import pandas as pd
import dash_daq as daq

########### Define a few variables ######

tabtitle = 'Dash DAQ'
sourceurl = 'https://dash.plot.ly/dash-daq'
sourceurl2 = 'https://dash.plot.ly/state'
githublink = 'https://github.com/austinlasseter/dash-daq-state'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

######### Define the figure

x_list=['monkeys', 'bananas']
y_list=[10,5]
myfavoritecolor=['Tan', 'Yellow']
mytitle='zoo time fun'

mydata = [go.Bar(x=x_list,
                y=y_list,
                marker=dict(color=myfavoritecolor))]
mylayout = go.Layout(
    title = mytitle,
    xaxis = dict(title = 'Labels go here!'),
    yaxis = dict(title = 'Numbers go here!'))
myfigure = go.Figure(data=mydata, layout=mylayout)


########### Layout

app.layout = html.Div(children=[
    html.H1('This is the header'),
    dcc.Graph(id='my-graph', figure=myfigure),

    # Footer
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    html.Br(),
    html.A("Data Source", href=sourceurl2),
    ]
)

########### Callback


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
