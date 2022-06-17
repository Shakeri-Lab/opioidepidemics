import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = dbc.Container(
    [
        navbar,
        html.H1("Title"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col("row 1, column 1 content", md=6),
                dbc.Col("row 1, column 2 content", md=6),
            ],
        ),
    ],
    fluid=True,
)


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)
