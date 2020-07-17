import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

tab2_content = dbc.Card(
    dbc.CardBody(
        [

        	dbc.Row([
        		dbc.Col([
        			html.Div([dcc.Graph(id='education_level',style={"height" : "400px", "width" : "600px"}),],),
        			]),
        		dbc.Col([
        			html.P("This is tab 2!", className="card-text"),
            		dbc.Button("Don't click here", color="danger"),
            		]),]),
        ] ,  #style={"height" : "400px", "width" : "600px"}
    ),
    className="mt-3",
)





