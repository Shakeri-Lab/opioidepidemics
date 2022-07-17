# ------------------Neighborhood page------------------#
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import srcCode.toolbarDescs as tb
import srcCode.resourcesDescs as rd
import srcCode.dashFuncs as df


layout = html.Div(
    [
        # Navbar
        html.Div([
            df.createTopBar()
        ], className="background"),
        html.Div(
        [
                html.H3(rd.text['MAIN_TITLE'], className = "center_text title"),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col([], width=4),
                        dbc.Col([
                            html.Span(rd.text["QOL_MAP"], className="left_text bodytext"),
                            df.createArrowLink(rd.text['OD'], rd.links['OD']),
                            df.createArrowLink(rd.text['RX'], rd.links['RX']),
                        ], width = 8),
                        dbc.Col([], width=4)
                    ]
                ),
                html.Br(),
                html.Br(),
                html.Br()
        ])
    ], className = "background")
