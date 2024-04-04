# Line and bar charts page
from dash import html, register_page, get_asset_url, dcc
import dash_bootstrap_components as dbc
# Add an import to import the line_chart function
from figures import line_chart

# register the page in the app
register_page(__name__, name='Events', title='Events', path="/",)

def create_card(event_id):
    """
    Generate a card for the event specified by event_id.

    Uses the REST API route.

    Args:
        event_id:

    Returns:
        card: dash boostrap components card for the event
    """
    # Use python requests to access your REST API on your localhost
    # Make sure you run the REST APP first and check your port number if you changed it from the default 5000
    url = f"http://127.0.0.1:5000/events/{event_id}"
    event_response = requests.get(url)
    ev = event_response.json()

    # Variables for the card contents
    logo = f'logos/{ev['year']}_{ev['host']}.jpg'
    dates = f'{ev['start']} to {ev['end']}'
    host = f'{ev['host']} {ev['year']}'
    highlights = f'Highlights: {ev['highlights']}'
    participants = f'{ev['participants']} athletes'
    events = f'{ev['events']} events'
    countries = f'{ev['countries']} countries'

    card = dbc.Card([
        dbc.CardBody(
            [
                html.H4([html.Img(src=app.get_asset_url(logo), width=35, className="me-1"),
                         host]),
                html.Br(),
                html.H6(dates, className="card-subtitle"),
                html.P(highlights, className="card-text"),
                html.P(participants, className="card-text"),
                html.P(events, className="card-text"),
                html.P(countries, className="card-text"),
            ]
        ),
    ],
        style={"width": "18rem"},
    )
    return card

# Set to display event 12, this will be changed next week using a callback
card = create_card(12)

row_one = html.Div(
    dbc.Row([
        dbc.Col([html.H1("Event Details"), html.P(
            "Event details. Select a marker on the map to display the event highlights and summary data.")
                 ], width=12),
    ]),
)

row_two = html.Div(
    dbc.Row([
        dbc.Col(children=[
            html.Img(src=get_asset_url('map-placeholder.png'), className="img-fluid"),
        ], width=8),
        dbc.Col(children=[
            card,
        ], width=4),
    ], align="start")
)

# Add an HTML layout to the Dash app.
# The layout is wrapped in a DBC Container()
layout = dbc.Container([
    row_one,
    row_two,
])
