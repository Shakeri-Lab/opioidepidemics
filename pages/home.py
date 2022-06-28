from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import srcCode.homeDescs as hd
import srcCode.dashFuncs as df
import srcCode.qolFuncs as qf
import srcCode.qolDescs as qd

# Neighborhood dropdown texts

layout = html.Div(
    [
    # Navbar
    html.Div([
        df.createTopBar()
    ], className="background"),
    # Dropdown for quality of life map
    html.Div([
        df.createLeftAlignDropdown(qd.text['DD_QOL'], qd.opts['DD_QOL'],
                          qd.default['DD_QOL'], dd_id='qol_dropdown',
                          dd_style={'width': '150px'}, 
                          clearable=False, searchable=False),
    ]),
    # overdose deaths in VA map
    html.Div(
        [
            # OD map
            dcc.Graph(id='odVA_map', 
                      figure=qf.plotVDHMap(2018, 'Any Opioids'), 
                      config={'displayModeBar': True,
                              "displaylogo": False,
                              'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d']},
                      style={"width": "100%", "height": "550px"}),
            html.Div([
                    html.Div([
                        dcc.Slider(min=2015, max=2018, step=1, value=2018, 
                                   tooltip={"placement": "bottom", "always_visible": True},
                                   #marks={1945: "1945", 1950: "", 1955: "1955", 1960: "", 1965: "1965", 1970: "",
                                   #       1975: "1975", 1980: "", 1985: "1985", 1990: "", 1995: "1995", 2000: "",
                                   #       2005: "2005", 2010: "", 2015: "2015", 2020: "2020"},
                                   id="odVA_slider_year")
                    ], style={"width": "100%"}),
        ])]),

    # divider
    html.Hr(className="center_text title"),
    html.Br(),
    ], className = "background")

@callback(
   Output(component_id='odVA_map', component_property='figure'),
   [Input(component_id='odVA_slider_year', component_property='value')])
def update_od_map(year):

    return qf.plotVDHMap(year, 'Any Opioids')
