# Line and bar charts page
from dash import html, register_page, get_asset_url, dcc
import dash_bootstrap_components as dbc
# Add an import to import the line_chart function
from figures import line_chart
# Add an import to import the scatter_geo function
from figures import bar_gender


# register the page in the app
register_page(__name__, name="Charts", title="Charts")

# Variables that define the rows and their contents
dropdown = dbc.Select(
    id="type-dropdown",  # id uniquely identifies the element, will be needed later
    options=[
        {"label": "Events", "value": "events"},
        # The value is in the format of the column heading in the data
        {"label": "Sports", "value": "sports"},
        {"label": "Countries", "value": "countries"},
        {"label": "Athletes", "value": "participants"},
    ],
    value="events"  # The default selection
)

checklist = dbc.Checklist(
    options=[
        {"label": "Summer", "value": "summer"},
        {"label": "Winter", "value": "winter"},
    ],
    value=["summer"],  # Values is a list as you can select both winter and summer
    id="checklist-input",
)

row_one = dbc.Row([
    dbc.Col([html.H1("Charts"), html.P(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce "
        "efficitur posuere metus posuere malesuada. ")
             ], width=12),
])

row_two = dbc.Row([
    dbc.Col(children=[
        dropdown
    ], width=2),
    dbc.Col(children=[
        # see checklist variable defined earlier
        checklist,
    ], width={"size": 2, "offset": 4}),
], align="start")

# Create the Plotly Express line chart object, e.g. to show number of sports
line = line_chart("sports")
bar = bar_gender("Summer")

row_three = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="line", figure=line),
    ], width=6),
    dbc.Col(children=[
        dcc.Graph(id="bar", figure=bar),
    ], width=6),
], align="start")

# Add an HTML layout to the Dash app.
# The layout is wrapped in a DBC Container()
layout = dbc.Container([
    row_one,
    row_two,
    row_three
])
