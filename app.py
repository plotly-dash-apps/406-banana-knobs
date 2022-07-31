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

colorlist=['Pale Yellow', 'Deep Yellow', 'Brown',  'Leaf Green', 'Jungle Green', 'Violet']
palette=['#fffbc9',  '#fbec5d', '#6b3e26', '#38bc1c', '#004b49', '#b323f6']

def make_my_cool_figure(input1, input2, drop1, drop2, knob1, knob2):
    drop1=int(drop1)
    drop2=int(drop2)
    myfavoritecolors=[palette[drop1], palette[drop2]]
    x_list=[input1, input2]
    y_list=[knob1, knob2]
    mytitle=f"Let's talk about {input1} and {input2}!"
    mydata = [go.Bar(x=x_list,
                    y=y_list,
                    marker=dict(color=myfavoritecolors))]
    mylayout = go.Layout(
        title = mytitle,
        xaxis = dict(title = 'Categories'),
        yaxis = dict(title = 'Counts'))
    myfigure = go.Figure(data=mydata, layout=mylayout)
    return myfigure

########### Layout

app.layout = html.Div(children=[
    html.Div([
        html.H4(['Build a figure!'], className='six columns'),
        html.Div([html.Button(id='submit-button', n_clicks=0, children='Submit')], className='six columns'),
    ], className='twelve columns'),


    html.Div([
        # Input 1
        html.Div([
            html.H6('Category 1:'),
                html.Div([
                    dcc.Input(id='input-1', type='text', value='Monkeys'),
                    dcc.RadioItems(
                        id='drop-1',
                        options=[{'label': j, 'value': k} for j, k in zip(colorlist, range(0,6))],
                        value=2
                    ),
                ], className='four columns'),
                html.Div([
                    daq.Knob(
                          id='knob-1',
                          max=10,
                          value=5,
                          min=0
                        ),
                ], className='two columns'),
        ], className='six columns', style={'padding': '12px','border': 'thin black solid',}),

        # Input 2
        html.Div([
            html.H6('Category 2:'),
                html.Div([
                    dcc.Input(id='input-2', type='text', value='Bananas'),
                    dcc.RadioItems(
                        id='drop-2',
                        options=[{'label': j, 'value': k} for j, k in zip(colorlist, range(0,6))],
                        value=1
                    ),
                ], className='four columns'),
                html.Div([
                    daq.Knob(
                          id='knob-2',
                          max=10,
                          value=8,
                          min=0
                        ),
                ], className='two columns'),
        ], className='six columns', style={'padding': '12px','border': 'thin black solid',}),
    ], className='twelve columns'),


        # Output
    html.Div(
        [dcc.Graph(id='my-graph'),
        # Footer
        html.Br(),
        html.A('Code on Github', href=githublink),
        html.Br(),
        html.A("Data Source", href=sourceurl),
        html.Br(),
        html.A("Data Source", href=sourceurl2),
    ], className='twelve columns'),



    ]
)

########### Callback

@app.callback(Output('my-graph', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1', 'value'),
               State('input-2', 'value'),
               State('drop-1', 'value'),
               State('drop-2', 'value'),
               State('knob-1', 'value'),
               State('knob-2', 'value'),
               ])
def update_output(n_clicks, input1, input2, drop1, drop2, knob1, knob2):
    return make_my_cool_figure(input1, input2, drop1, drop2, knob1, knob2)

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
