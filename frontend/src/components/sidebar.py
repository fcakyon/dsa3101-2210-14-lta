import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State


jam = "https://i.ibb.co/xhwnPXB/JAM-01.png"

navbar = dbc.NavbarSimple(
    children=[
        dbc.Col(html.Img(src=jam, height="47px"), style={"align-content": "left"}),
        dbc.Button("Sidebar", color="secondary", className="mr-1", id="btn_sidebar"),
        
    ],
    brand="JAM TRACKER",
    brand_href="#",
    color="#4F6D7A",
    dark=True,
    fluid=True,
)


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_SHOWN = {
    "position": "fixed",
    "top": 62.5,
    "right": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f8f9fa",
}

SIDEBAR_HIDDEN = {
    "position": "fixed",
    "top": 62.5,
    "right": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_HIDDEN = {
    "height":"90vh", 
    "width":"auto", 
    "transition": "margin-right .5s",
    "padding":0, 
    "margin":0
}

CONTENT_SHOWN = {
    "height":"90vh", 
    "width":"auto",
    "transition": "margin-right .5s",
    "margin-right": "16rem",
    "margin-top":0,
    "margin-left":0,
    "margin-bottom":0,
    "padding":0
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="http://127.0.0.1:8050/", active="exact"),
                dbc.NavLink("Map", href="http://127.0.0.1:8050/map", active="exact"),
                dbc.NavLink("Grid", href="http://127.0.0.1:8050/grid", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_SHOWN,
)


layout = html.Div(
    [
        navbar,
        sidebar,
    ],
)

@callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data")
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_s = SIDEBAR_HIDDEN
            content_s = CONTENT_HIDDEN
            cur_nclick = "HIDDEN"
        else:
            sidebar_s = SIDEBAR_SHOWN
            content_s = CONTENT_SHOWN
            cur_nclick = "SHOW"
    else:
        sidebar_s = SIDEBAR_SHOWN
        content_s = CONTENT_SHOWN
        cur_nclick = 'SHOW'

    return sidebar_s, content_s, cur_nclick


















