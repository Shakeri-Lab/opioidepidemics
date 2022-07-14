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
            # OD map
            dcc.Graph(id='va_map', 
                    figure=qf.plotVDHMap(2018, 'Any Opioids'), 
                    config={'displayModeBar': True,
                            "displaylogo": False,
                            'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d',
                                                        'toImage']},
                    style={"width": "100%", "height": "550px"}),
            html.Div([
                html.Div([
                    dcc.Slider(min=2015, max=2018, step=1, value=2018, 
                            tooltip={"placement": "bottom", "always_visible": True},
                            marks={2015: "2015", 2016: "2016", 2017: "2017", 2018: "2018"},
                            id="odVA_slider_year")
                    ], id="odVA_slider_div", style={"width": "100%"}),
                html.Div([
                    dcc.Slider(min=2006, max=2020, step=1, value=2020,
                                tooltip={"placement": "bottom", "always_visible": True},
                                marks={2006: "2006", 2008: "2008", 2010: "2010", 2012: "2012",
                                        2014: "2014", 2016: "2016", 2018: "2018", 2020: "2020"},
                                id="dispenseVA_slider_year")
                    ], id="dispenseVA_slider_div", style={"display": "none"}),
                # Map type dropdown
                df.createDropdown(qd.text['DD_QOL'], qd.opts['DD_QOL'],
                                qd.default['DD_QOL'], dd_id="map_dropdown", 
                                dd_style={"width": "200px"}, clearable=False, searchable=False),
                ], className="grid_container", style={"grid-template-columns": "minmax(600px, 4fr) 2fr"}),
        ], className="subcontainer"),
    # divider
    html.Br(),
    html.Hr(className="center_text title"),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(html.P([hd.text['SUPPRESSION']]), className="subcontainer left_text bodytext"),
    html.Br(),
    html.Br(),
    html.Br(),
    ], className = "background")

@callback(
    Output('va_map', 'figure'),
    Output('odVA_slider_div', 'style'),
    Output('dispenseVA_slider_div', 'style'),
    Input('map_dropdown', 'value'),
    Input('odVA_slider_year', 'value'),
    Input('dispenseVA_slider_year', 'value'))
def update_va_plot(viewSelection, odYear, dispenseYear):
    if viewSelection == qd.opts['DD_QOL'][0]:
        return (qf.plotVDHMap(odYear, 'Any Opioids'),
                {'display': 'block', "width": "100%"}, 
                {'display': 'none'})
    elif viewSelection == qd.opts['DD_QOL'][1]:
        return (qf.plotCDCMap(dispenseYear), 
                {'display': 'none'},
                {'display': 'block', "width": "100%"})
