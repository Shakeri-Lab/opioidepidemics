from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
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
    # quality of life map
    html.Div(
        [
            # QoL map
            dcc.Graph(id='qol_map', 
                      figure=qf.plotResourcesMap(), 
                      config={'displayModeBar': True,
                              "displaylogo": False,
                              'modeBarButtonsToRemove': ['pan2d', 'select2d', 'lasso2d']},
                      style={"width": "100%", "height": "550px"}),
        ]),
    # divider
    html.Hr(className="center_text title"),
    html.Br(),
    ], className = "background")

@callback(
   Output(component_id='qol_map', component_property='figure'),
   [Input(component_id='qol_dropdown', component_property='value')])
def show_hide_qol_map(currentMap):

    optsMap = qd.opts['DD_QOL']
    if currentMap == optsMap[0]:
        return qf.plotResourcesMap()
    elif currentMap == optsMap[1]:
        return qf.plotSchoolMap()
    elif currentMap == optsMap[2]:
        return qf.plotTreeMap()
    else:
        return qf.plotResourcesMap()
