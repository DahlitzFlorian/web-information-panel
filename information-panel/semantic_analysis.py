import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(csrf_protect=False)

app.layout = html.Div(children=[
    html.Header(children=[
        html.Div(children="Informations-Panel", id="logo"),
        html.Nav(children=[
            html.Ul(children=[
                html.Li(children=[html.A(children="Startseite", href="http://localhost:8000/")]),
                html.Li(children=[html.A(children="Semantische Analysen", href="http://127.0.0.1:8050/")]),
                html.Li(children=[html.A(children="Themen-Recherche", href="#")]),
                html.Li(children=[html.A(children="Vorgeschlagene Themen", href="#")])
            ])
        ])
    ]),
    html.Article(children=[
        html.H1(children="Semantische Analysen"),
        html.Form(children=[
            html.Label("Suchbegriff - Term"),
            dcc.Input(id="term", type="text", value=""),
            html.Div(children=[], id="some", style={"display":"none"})
        ], id="sem_ana_form")
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)