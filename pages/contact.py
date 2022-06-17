# ------------------Contact page----------------------#
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import srcCode.toolbarDescs as tb
import srcCode.contactDescs as cd
import srcCode.dashFuncs as df


layout = html.Div(
    [
        # Navbar
        html.Div([
            df.createTopBar()
        ], className="background"),
        html.Div(
        [
                html.H3(cd.text['MAIN_TITLE'], className = "center_text title"),
                html.Br(),
                html.Div([
                    html.A([
                        html.Img(src = 'assets/christian.png', style={'height':'150px', 'width': '150px'}, 
                                 className="circular--square"),
                    ], href=cd.links['CHRISTIAN'], target="_blank", className = "ctct_elem1"),
                    html.A([
                        html.Img(src = 'assets/nour.png', style={'height':'150px', 'width': '150px'}, 
                                 className="circular--square"),
                    ], href=cd.links['NOUR'], target="_blank", className = "ctct_elem2"),
                    html.A([
                        html.Img(src = 'assets/evan.jpg', style={'height':'150px', 'width': '150px'}, 
                                 className="circular--square"),
                    ], href=cd.links['EVAN'], target="_blank", className = "ctct_elem3"),
                    html.A([
                        html.Img(src = 'assets/Heman_001.png', style={'height':'150px', 'width': '150px'}, 
                                 className="circular--square"),
                    ], href=cd.links['HEMAN'], target="_blank", className = "ctct_elem4"),
                ], className = "grid_contact"),
                html.Div([
                    html.Span(cd.text['CHRISTIAN'], className="ctct_elem1 center_text bodytext"),
                    html.Span(cd.text['NOUR'], className="ctct_elem2 center_text bodytext"),
                    html.Span(cd.text['EVAN'], className="ctct_elem3 center_text bodytext"),
                    html.Span(cd.text['HEMAN'], className="ctct_elem4 center_text bodytext"),
                ], className = "grid_contact"),
                html.Div([
                    html.Span(cd.text['STUDENT'], className="ctct_elem1 center_text bodytext"),
                    html.Span(cd.text['STUDENT'], className="ctct_elem2 center_text bodytext"),
                    html.Span(cd.text['MENTOR'], className="ctct_elem3 center_text bodytext"),
                    html.Span(cd.text['ADVISOR'], className="ctct_elem4 center_text bodytext"),
                ], className = "grid_contact"),
                html.Br(),
                html.Br(),
                html.Span(cd.text['TEAM'], className="center_text subtitle"),
                html.Br(),
                html.Br(),
                html.H3(cd.text['SUPPORT'], className = "center_text title"),
                html.Br(),
                html.A(cd.text['ISSUES'], href=cd.links['ISSUES'], target="_blank",
                       className = "center_text links_text"),
                html.Br(),
                html.Br(),
                #dcc.Link('Take me back up', href='#', className = "left_text links_text"),
        ])
    ], className = "background")
