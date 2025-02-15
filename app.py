import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading1='Potential 2019 World Series Matchup'
tabtitle = "WS 2019"
list_of_al=['astros', 'as', 'rays', 'yankees', 'twins']
list_of_nl=['dodgers', 'nationals', 'brewers', 'braves', 'cardinals']
sourceurl = 'https://dash.plot.ly/getting-started-part-2'
githublink = 'https://github.com/nomsdoms/dash-callbacks-multi-input'


########## Set up the chart

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Div([
            dcc.RadioItems(
                id='pick-a-color',
                options=[
                        {'label':list_of_al[0], 'value':list_of_al[0]},
                        {'label':list_of_al[1], 'value':list_of_al[1]},
                        {'label':list_of_al[2], 'value':list_of_al[2]},
                        {'label':list_of_al[3], 'value':list_of_al[3]},
                        {'label':list_of_al[4], 'value':list_of_al[4]},
                        ],
                value='astros',
                ),
        ],className='two columns'),
        html.Div([
            dcc.RadioItems(
                id='pick-a-number',
                options=[
                        {'label':list_of_nl[0], 'value':list_of_nl[0]},
                        {'label':list_of_nl[1], 'value':list_of_nl[1]},
                        {'label':list_of_nl[2], 'value':list_of_nl[2]},
                        {'label':list_of_nl[3], 'value':list_of_nl[3]},
                        {'label':list_of_nl[4], 'value':list_of_nl[4]},
                        ],
                value='choose',
                ),
        ],className='two columns'),
        html.Div([
            html.Div(id='your_output_here', children=''),
        ],className='eight columns'),
    ],className='twelve columns'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

########## Define Callback

@app.callback(Output('your_output_here', 'children'),
              [Input('pick-a-color', 'value'),
               Input('pick-a-number', 'value')])
def radio_results(color_you_picked, number_you_picked):
    image_you_chose=f'{color_you_picked}-{number_you_picked}.jpg'
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': '25%', 'height': '25%'}),

############ Deploy
if __name__ == '__main__':
    app.run_server()
