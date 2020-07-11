import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success", id="button1"),
            html.Div(id='result'),
            html.Div(id='result2'),


        ]
    ),
    className="mt-3",
)