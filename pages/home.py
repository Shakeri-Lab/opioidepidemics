from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import srcCode.homeDescs as hd
import srcCode.dashFuncs as df
import srcCode.qolFuncs as qf
import srcCode.qolDescs as qd

layout = html.Div(
    [
    # Navbar
    html.Div([
        df.createTopBar()
    ], className="background"),
    html.Br(),
    html.Div(
        [
            html.Div(
                [
                    df.createDropdown(qd.text['DD_OD'], qd.opts['DD_OD'],
                                    qd.default['DD_OD'], dd_id="od_dropdown",
                                    dd_style={"width": "200px"}, clearable=False,
                                    searchable=False, optionHeight=45),
                ]),
            html.Div(
                [
                    df.createDropdown(qd.text['DD_STATE'], qd.opts['DD_STATE'],
                                    qd.default['DD_STATE'], dd_id="state_dropdown",
                                    dd_style={"width": "200px"}, clearable=False,
                                    searchable=True),
                ]),
        ], className = "grid_container",
        style={'grid-template-columns': 'minmax(600px, 1fr) minmax(600px, 1fr)'}),
    html.Div(
        [
            html.Div([
                dcc.Slider(min=2015, max=2018, step=1, value=2018, 
                        tooltip={"placement": "bottom", "always_visible": True},
                        marks={2015: "2015", 2016: "2016", 2017: "2017", 2018: "2018"},
                        id="odVA_slider_year")
                ], id="odVA_slider_div", style={"width": "90%"}),
            html.Div([
                dcc.Slider(min=2006, max=2020, step=1, value=2020,
                        tooltip={"placement": "bottom", "always_visible": True},
                        marks={2006: "2006", 2008: "2008", 2010: "2010", 2012: "2012",
                               2014: "2014", 2016: "2016", 2018: "2018", 2020: "2020"},
                        id="dispense_slider_year")
                ], id="dispense_slider_div", style={"width": "90%"}),
        ], className = "grid_container",
        style={'grid-template-columns': 'minmax(600px, 1fr) minmax(600px, 1fr)'}),
    html.Div(
        [
            dcc.Graph(id='va_od_chart', figure=qf.plotVDHBar(2018, 'Any Opioids'),
                    style={'overflowY': 'scroll', 'maxHeight': 600},
                    config={'displayModeBar': True,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': ['pan2d', 'lasso2d']}),
            dcc.Graph(id='dispense_chart', figure=qf.plotCDCBar(2018, 'VA'),
                    style={'overflowY': 'scroll', 'maxHeight': 600},
                    config={'displayModeBar': True,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': ['pan2d', 'lasso2d']}),
        ], className="grid_container",
        style={"grid-template-columns": "minmax(600px, 1fr) minmax(600px, 1fr)"}),
    # VDH data suppression disclaimer
    html.Div(html.P([hd.text['SUPPRESSION']]), 
            className="grid_container left_text bodytext",
            style={'grid-template-columns': 'minmax(600px, 1fr) minmax(600px, 1fr)'}),
    html.Br(),
    html.Hr(className="center_text title"),
    html.Br(),
    html.H1(hd.text['TREATMENT_MAP'], className = "center_text title"),
    html.Div(
        [
            # Treatment map
            dcc.Graph(id='va_treatment_map', 
                    figure=qf.plotOfficeMap(), 
                    config={'displayModeBar': True,
                            "displaylogo": False,
                            'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d',
                                                        'toImage']},
                    style={'width': '85%', 'height': '650px'}),
        ], className="center"),
    html.Br(),
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
    Output('va_od_chart', 'figure'),
    Input('odVA_slider_year', 'value'),
    Input('od_dropdown', 'value'))
def update_od_chart(year, drug_class):
    if drug_class == qd.opts['DD_OD'][0]:
        return qf.plotVDHBar(year, drug_class)
    elif drug_class == qd.opts['DD_OD'][1]:
        return qf.plotVDHBar(year, drug_class)
    elif drug_class == qd.opts['DD_OD'][2]:
        return qf.plotVDHBar(year, "N SS S Opioids")
    elif drug_class == qd.opts['DD_OD'][3]:
        return qf.plotVDHBar(year, "Rx N SS Methadone")
    elif drug_class == qd.opts['DD_OD'][4]:
        return qf.plotVDHBar(year, "N SS Opioids")
    elif drug_class == qd.opts['DD_OD'][5]:
        return qf.plotVDHBar(year, "S Opioids No Methadone")
    elif drug_class == qd.opts['DD_OD'][6]:
        return qf.plotVDHBar(year, drug_class)
    elif drug_class == qd.opts['DD_OD'][7]:
        return qf.plotVDHBar(year, drug_class)

@callback(
    Output('dispense_chart', 'figure'),
    Input('dispense_slider_year', 'value'),
    Input('state_dropdown', 'value'))
def update_dispense_chart(year, state):
    return qf.plotCDCBar(year, qd.states[state]['state_abbr'])