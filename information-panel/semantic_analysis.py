import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import os

# global variables
location = "P:/python/information-panel/"

# basic functions
def delete_term_files():
    for file in os.listdir(location):
        if os.path.basename(file).endswith(".term"):
            os.remove(location + file)

def save_term(term):
    delete_term_files()
    open(location + term + ".term", "a").close()

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
        html.Label("Suchbegriff - Term"),
        dcc.Input(id="term", type="text", value=""),
        html.Div(children=[], id="some", style={"display":"none"}),
        html.Button(value="Suchen", id="submit")
    ])
])

@app.callback(
    Output("some", "children"), 
    [Input("submit", "n_clicks")],
    state=[State("term", "value")])

def run_analysis(n_clicks, term):
    save_term(term)
    delete_term_files()

if __name__ == "__main__":
    app.run_server(debug=True)