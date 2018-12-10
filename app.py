# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
#import plotly
import plotly.plotly as py
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('JIRA.csv')

assignee = df['Assignee'].value_counts()
status = pd.crosstab(df.Assignee,df.Status)
status_backlog = status['Backlog']
status_inprogress = status['In Progress']
status_checkedin = status['Checked-in']
status_qa = status['QA']
status_passqa = status['Pass QA']
status_done = status['Done']

#data_x = assignee.index
data_y = assignee[assignee.index]

data_x = status.index
data_backlog = status_backlog[status_backlog.index]
data_inprogress = status_inprogress[status_inprogress.index]
data_checkedin = status_checkedin[status_checkedin.index]
data_qa = status_qa[status_qa.index]
data_passqa = status_passqa[status_passqa.index]
data_done = status_done[status_done.index]

trace1 = go.Bar(
    x = data_x,
    y = data_backlog,
    name = 'Back log',
    text = data_backlog,
    textposition='auto'
)
trace2 = go.Bar(
    x = data_x,
    y = data_inprogress,
    name = 'In Progress',
    text = data_backlog,
    textposition = 'auto'
)
trace3 = go.Bar(
    x = data_x,
    y = data_checkedin,
    name = 'Checked In',
    text = data_checkedin,
    textposition = 'auto'
)
trace4 = go.Bar(
    x = data_x,
    y = data_qa,
    name = 'QA',
    text = data_qa,
    textposition = 'auto'
)
trace5 = go.Bar(
    x = data_x,
    y = data_passqa,
    name = 'Pass QA',
    text = data_passqa,
    textposition = 'auto'
)
trace6 = go.Bar(
    x = data_x,
    y = data_done,
    name = 'Done',
    text = data_done,
    textposition = 'auto'
)


data=[trace1, trace2, trace3, trace4, trace5, trace6]
#layout = go.Layout(barmode='stack')

#fig = go.Figure(data=data, layout=layout)
#py.iplot(fig, filename='grouped-bar')

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6],
                               layout=go.Layout(barmode='stack'))
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
