import dash
import dash_core_components as dcc
import dash_html_components as html
import folium

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

m = folium.Map()
folium.map.Marker(['45', '45']).add_to(m)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    dcc.Markdown(children=markdown_text, style={'color': colors['text']}),
    html.Iframe(id='map', srcDoc=m._repr_html_(), width='40%', height=600)
])



if __name__ == '__main__':
    app.run_server(debug=True)