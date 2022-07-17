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
    html.Br(),
    html.Div(
        [
            df.createDropdown(hd.text['DROPDOWN_MAP'], qd.opts['DD_QOL'],
                              qd.default['DD_QOL'], dd_id="map_dropdown",
                              dd_style={"width": "200px"}, clearable=False,
                              searchable=False),
        ], className="subcontainer map_drop"),
    html.Div(
        [
            # OD map
            dcc.Graph(id='va_od_map', 
                    figure=qf.plotVDHMap('Any Opioids'), 
                    config={'displayModeBar': True,
                            "displaylogo": False,
                            'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d',
                                                        'toImage']},
                    style={"width": "100%", "height": "650px"}),
            # Dispense map
            dcc.Graph(id='va_dispense_map', 
                    figure=qf.plotCDCMap(), 
                    config={'displayModeBar': True,
                            "displaylogo": False,
                            'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d',
                                                        'toImage']},
                    style={'display': 'none'}),
        ], className="subcontainer"),
    html.Br(),
    # VDH data suppression disclaimer
    html.Div(html.P([hd.text['SUPPRESSION']]), className="subcontainer left_text bodytext"),
    html.Br(),
    html.Hr(className="center_text title"),
    html.Br(),
    html.Div([
        # Line plots for national data
        dcc.Graph(id='national_lineplots', 
                figure=qf.plotUSALineplots(), 
                config={'displayModeBar': True,
                        "displaylogo": False,
                        'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d']},
                style={"width": "100%", "height": "650px"}),
    ], className = "subcontainer"),
    html.Br(),
    html.Br(),
    html.Br(),
    ], className = "background")

@callback(
    Output('va_od_map', 'style'),
    Output('va_dispense_map', 'style'),
    Input('map_dropdown', 'value'))
def update_va_plot(viewSelection):
    if viewSelection == qd.opts['DD_QOL'][0]:
        return ({'display': 'block', "width": "100%", 
                 "height": "650px"}, {'display': 'none'})
    elif viewSelection == qd.opts['DD_QOL'][1]:
        return ({'display': 'none'},
                {'display': 'block', "width": "100%", 
                 "height": "650px"})
