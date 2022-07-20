from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import srcCode.homeDescs as hd
import srcCode.dashFuncs as df
import srcCode.qolFuncs as qf
import srcCode.qolDescs as qd

db, lisa = qf.getLISAframes(2018, target = 'od', drug_class='Any Opioids')

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
                    df.createDropdown(qd.text['DD_LISA'], qd.opts['DD_LISA'],
                                    qd.default['DD_LISA'], dd_id="lisa_dropdown",
                                    dd_style={"width": "200px"}, clearable=False,
                                    searchable=False),
                ]),
            html.Div([
                dcc.Slider(min=2015, max=2018, step=1, value=2018, 
                        tooltip={"placement": "bottom", "always_visible": True},
                        marks={2015: "2015", 2016: "2016", 2017: "2017", 2018: "2018"},
                        id="od_slider_year")
                ], id="odVA_slider_div", style={"width": "90%"}),
            html.Div([
                dcc.Slider(min=2006, max=2020, step=1, value=2020,
                        tooltip={"placement": "bottom", "always_visible": True},
                        marks={2006: "2006", 2008: "2008", 2010: "2010", 2012: "2012",
                               2014: "2014", 2016: "2016", 2018: "2018", 2020: "2020"},
                        id="rx_slider_year")
                ], id="dispense_slider_div", style={"display": "none"}),
        ], className = "grid_container",
        style={'grid-template-columns': 'minmax(600px, 1fr) minmax(600px, 1fr)'}),
    html.Div(
        [
            dcc.Graph(id='moran_scatter', figure=qf.plotMoran(db, target = 'od'),
                    config={'displayModeBar': True,
                            "displaylogo": False,
                            'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d',
                                                        'toImage']}),
            dcc.Graph(id='moran_rug', figure=qf.plotKDE(lisa),
                    config={'displayModeBar': True,
                            "displaylogo": False,
                            'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d',
                                                        'toImage']}),
        ], className="grid_container",
        style={"grid-template-columns": "minmax(600px, 1fr) minmax(600px, 1fr)"}),
    html.Div(
        [
            html.Img(id='image', style={'height':'70%', 'width':'70%'},
                     src='data:image/png;base64,{}'.format(qf.plotClusters(db, lisa).decode()))
        ], className="center"),
    html.Br(),
    html.Br(),
    # VDH data suppression disclaimer
    html.Div(html.P([hd.text['SUPPRESSION']]), 
            className="grid_container left_text bodytext",
            style={'grid-template-columns': 'minmax(600px, 1fr) minmax(600px, 1fr)'}),
    html.Br(),
    html.Br(),
    html.Br(),
    ], className = "background")

@callback(
    Output('moran_scatter', 'figure'),
    Output('moran_rug', 'figure'),
    Output('image', 'src'),
    Output('odVA_slider_div', 'style'),
    Output('dispense_slider_div', 'style'),
    Input('lisa_dropdown', 'value'),
    Input('od_slider_year', 'value'),
    Input('rx_slider_year', 'value'))
def update_dispense_chart(lisaSelection, yearOD, yearRX):
    if lisaSelection == qd.opts['DD_LISA'][0]:
        db, lisa = qf.getLISAframes(yearOD, target = 'od', drug_class='Any Opioids')
        return qf.plotMoran(db, target = 'od'), \
            qf.plotKDE(lisa), \
            'data:image/png;base64,{}'.format(qf.plotClusters(db, lisa).decode()), \
            {'display': 'block', 'width': '90%'}, \
            {'display': 'none'}
    else:
        db, lisa = qf.getLISAframes(yearRX, target = 'rx')
        return qf.plotMoran(db, target = 'rx'), \
            qf.plotKDE(lisa), \
            'data:image/png;base64,{}'.format(qf.plotClusters(db, lisa).decode()), \
            {'display': 'none'}, \
            {'display': 'block', 'width': '90%'}