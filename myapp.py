import dash
from dash import Dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = px.data.gapminder()
countries = df['country'].drop_duplicates()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("GDP per Capita Growth by Country"),

    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'  # initial value
    ),

    dcc.Graph(id='gdp-growth')
])

@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f"GDP per Capita Over Time: {selected_country}"
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)

app = Dash(__name__)
server = app.server
