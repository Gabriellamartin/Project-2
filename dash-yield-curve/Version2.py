# -*- coding: utf-8 -*-
# Import required libraries
import os

import pandas as pd
import numpy as np
import chart_studio.plotly as py

import flask
from flask_cors import CORS
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


# Setup the app
app = dash.Dash(__name__)
# Flask app
server = app.server 


app.layout = html.Div([
    html.Div(
        [
            dcc.Markdown(
                '''
                ### A View of Spotify Data that shows changing musical trends Year over Year
                [New York Times original](https://www.nytimes.com/interactive/2015/03/19/upshot/3d-yield-curve-economic-growth.html).
                '''.replace('  ', ''),
                className='eight columns offset-by-two'
            )
        ],
        className='row',
        style={'text-align': 'center', 'margin-bottom': '15px'}
    ),
    html.Div(
        [
            html.Div(
                [
                    dcc.Slider(
                        min=0,
                        max=5,
                        value=0,
                        marks= .5,
                        id='slider'
                    ),
                ],
                className='row',
                style={'margin-bottom': '12px'}
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Button('Back', id='back', style={
                                        'display': 'inline-block'}),
                            html.Button('Next', id='next', style={
                                        'display': 'inline-block'})
                        ],
                        className='two columns offset-by-two'
                    ),
                    dcc.Markdown(
                        id='text',
                        className='six columns'
                    ),
                ],
                className='row',
                style={'margin-bottom': '12px'}
            ),
            dcc.Graph(
                id='graph',
                style={'height': '60vh'}
            ),
        ],
        id='page'
    ),
])

# Internal logic
last_back = 0
last_next = 0

df = pd.read_csv("/Users/dhigh/Desktop/Northwestern/Project-2/NYT/dash-yield-curve/data/data_by_year.csv")

xlist = list(df["x"].dropna())
ylist = list(df["y"].dropna())

del df["x"]
del df["y"]

zlist = []
for row in df.iterrows():
    index, data = row
    zlist.append(data.tolist())
TEXTS = {
    0: '''
    #### Music Trends 101
    Spotify music measures individual songs based on a collection of sonic information. 
    >>
    The music is measured across the following variables acousticness, danceability, duration_ms, energy, instrumental, liveness, loudness, speechiness, tempo, valence, and popularity. 
    '''.replace('  ', ''),
    1: '''
    #### What we Found
    Over time the music on spotify is getting more upbeat
    '''.replace('  ', ''),
    2: '''
    #### Our Favorite categories
    Danceability was a fun one to thing of
    >>
    Danceability and Valence are highly correlated
    '''.replace('  ', ''),
    3: '''
    #### How did we get here
    One a long and winding Road
    >>
    To your Door
    >>
    I think I am figuring this out. 
    '''.replace('  ', ''),
    4: '''
    #### AC/DC
    
    '''.replace('  ', ''),
    5: '''
    #### Rock and Roll
    Here is the same chart viewed from above.
    '''.replace('  ', ''),




@app.callback(
    Output("graph", "figure"), 
    [Input("slider", "value")])
def make_graph(value):

    if value is None:
        value = 0

    if value in [0, 2, 3]:
        z_secondary_beginning = [z[1] for z in zlist if z[0] == 'None']
        z_secondary_end = [z[0] for z in zlist if z[0] != 'None']
        z_secondary = z_secondary_beginning + z_secondary_end
        x_secondary = [
            'danceability'] * len(z_secondary_beginning) + ['acousticness'] * len(z_secondary_end)
        y_secondary = ylist
        opacity = 0.7

    elif value == 1:
        x_secondary = xlist
        y_secondary = [ylist[-1] for i in xlist]
        z_secondary = zlist[-1]
        opacity = 0.7

    elif value == 4:
        z_secondary = [z[8] for z in zlist]
        x_secondary = ['tempo' for i in z_secondary]
        y_secondary = ylist
        opacity = 0.25

    if value in range(0, 5):

        trace1 = dict(
            type="surface",
            x=xlist,
            y=ylist,
            z=zlist,
            hoverinfo='x+y+z',
            lighting={
                "ambient": 0.95,
                "diffuse": 0.99,
                "fresnel": 0.01,
                "roughness": 0.01,
                "specular": 0.01,
            },
            colorscale=[[0, "rgb(230,245,254)"], [0.4, "rgb(123,171,203)"], [
                0.8, "rgb(40,119,174)"], [1, "rgb(37,61,81)"]],
            opacity=opacity,
            showscale=False,
            zmax=9.18,
            zmin=0,
            scene="scene",
        )

        trace2 = dict(
            type='scatter3d',
            mode='lines',
            x=x_secondary,
            y=y_secondary,
            z=z_secondary,
            hoverinfo='x+y+z',
            line=dict(color='#444444')
        )

        data = [trace1, trace2]

    else:

        trace1 = dict(
            type="contour",
            x=ylist,
            y=xlist,
            z=np.array(zlist).T,
            colorscale=[[0, "rgb(230,245,254)"], [0.4, "rgb(123,171,203)"], [
                0.8, "rgb(40,119,174)"], [1, "rgb(37,61,81)"]],
            showscale=False,
            zmax=9.18,
            zmin=0,
            line=dict(smoothing=1, color='rgba(40,40,40,0.15)'),
            contours=dict(coloring='heatmap')
        )

        data = [trace1]

        # margin = dict(
        #     t=5,
        #     l=50,
        #     b=50,
        #     r=5,
        # ),

    layout = dict(
        autosize=True,
        font=dict(
            size=12,
            color="#CCCCCC",
        ),
        margin=dict(
            t=5,
            l=5,
            b=5,
            r=5,
        ),
        showlegend=False,
        hovermode='closest',
        scene=dict(
            aspectmode="manual",
            aspectratio=dict(x=2, y=5, z=1.5),
            camera=dict(
                up=UPS[value],
                center=CENTERS[value],
                eye=EYES[value]
        
            xaxis={
                "showgrid": True,
                "title": "",
                "type": "category",
                "zeroline": False,
                "categoryorder": 'array',
                "categoryarray": list(reversed(xlist))
            },
            yaxis={
                "showgrid": True,
                "title": "",
                "type": "date",
                "zeroline": False,
            },
        )
    )

    figure = dict(data=data, layout=layout)
    # py.iplot(figure)
    return figure


# Make annotations
@app.callback(Output('text', 'children'), [Input('slider', 'value')])
def make_text(value):
    if value is None:
        value = 0

    return TEXTS[value]


# Button controls
@app.callback(Output('slider', 'value'),
              [Input('back', 'n_clicks'), Input('next', 'n_clicks')],
              [State('slider', 'value')])
def advance_slider(back, nxt, slider):

    if back is None:
        back = 0
    if nxt is None:
        nxt = 0
    if slider is None:
        slider = 0

    global last_back
    global last_next

    if back > last_back:
        last_back = back
        return max(0, slider - 1)
    if nxt > last_next:
        last_next = nxt
        return min(5, slider + 1)    

# Run the Dash app
if __name__ == '__main__':
    app.server.run()
