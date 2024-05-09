# Dash imports
import dash
from dash import html, dcc, Input, Output, State
from dash import register_page, callback
from dash import ctx, no_update, ALL
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

# Dash extensions
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from affichage import query11, query12,query13,query14, query15,query16, results_4,results_5
from test5 import results_6


question = "5. Triggers (suite) : Automatisez au maximum les calculs de population quand une nouvelle année de recensement est ajoutée au niveau des communes. Factorisez au maximum le code avec des procédures stockées."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

card_style = {
    'padding': '20px',
    'border': '2px solid #D3D3D3',
    'border-radius': '10px',
    'margin': '20px',
    'background-color': '#670907',
}


def layout():
    return html.Div([
        # Div pour afficher les résultats des requêtes
        html.Div(id='query-results5')
    ])

def display_query_results():
    children = []
    children.append(html.Div([
        html.H1('4. Triggers (suite)', style={'textAlign': 'center',
                'color': '#F8F9FA', 'font-size': '2.5em'})
    ], style=card_style))
    children.append(html.Div([
        html.H3("On souhaite ajouter les 3 années de données supplémentaires. Automatisez au maximum les calculs de population quand une nouvelle année de recensement est ajoutée au niveau des communes."),
        html.P("Nous avons importer les nouvelles données dans la table Pop_Commune. Puis, nous avons ajouté une colonne par année supplémentaire dans les tables Région et Département. Ensuite, nous avons utilisé des procédure stokées et un trigger pour mettre à jour automatiquement les tables Région et Département."),
        html.H4("Procédure stockée pour calculer la population des départements des 3 nouvelles années :"),
        html.Pre(query11),
        html.H4("Procédure stockée pour calculer la population des régions des 3 nouvelles années :"),
        html.Pre(query12),
        html.H4("Procédure pour mettre à jour les populations de toutes les années si il ya des modifications dans Pop_communes :"),
        html.Pre(query13),
        html.H4("Trigger qui déclanche la procédure précédente :"),
        html.Pre(query14),
        html.H4("Après ajout des 3 années dans Pop_Commune, nous pouvons voir que les données pour les 3 années se sont bien ajoutés :"),
        html.Pre(query15),
        html.Pre(query16),
        html.Ul([
            html.Li(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[6]} - {row[7]} - {row[8]} - {row[9]} - {row[10]}") for row in results_4
        ]),
        html.H4("Avant la mise à jour dans Pop_Commune pour l'année 2020 de la commune 01009 qui appartient à la region Auvergne-Rhône-Alpes :"),
        html.Ul([
            html.Li(f"{row[0]} - {row[1]} - {row[2]}") for row in results_5
        ]),
        html.H4("Après la mise à jour dans Pop_Commune pour l'année 2020 de la commune 01009 qui appartient à la region Auvergne-Rhône-Alpes :"),
        html.Ul([
            html.Li(f"{row[0]} - {row[1]} - {row[2]}") for row in results_6
        ]),
        html.P("Nous pouvons voir que la valeur de Auvergne-Rhône-Alpes pour l'année 2020 s'est mise à jour.")
    ]))

    return children


@callback(
    Output('query-results5', 'children'),
    [Input('query-results5', 'id')]  
)
def update_query_results(trigger):
    return display_query_results()
