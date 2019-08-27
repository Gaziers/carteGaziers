import folium
import geopandas as gpd
import pandas as pd

gaziers = {
    'Martin': {
        'lon': 6.770380,
        'lat':43.424881,
        'icon':'chien',
    },
    'Panda': {
        'lon': 3.876716,
        'lat':43.610767,
        'icon':'panda',
    },
    'Mathieu': {
        'lon': 5.369780,
        'lat':43.296482,
        'icon':'gnou',
    },
    'Antoine': {
        'lon': 4.4527778,
        'lat':45.4027778,
        'icon':'papillon',
    },
    'Gaspard': {
        'lon':-73.567253,
        'lat': 45.501690,
        'icon':'singe',
    },
    'Baptiste': {
        'lon': 151.209290,
        'lat':-33.868820,
        'icon':'kangourou',
    },
    'Thibaut': {
        'lon':-4.486076,
        'lat': 48.390392,
        'icon':'poule_femelle',
    },
    'Kevin': {
        'lon': 2.352222,
        'lat':48.856613,
        'icon':'renard',
    }
}

gaziers_df = pd.DataFrame(gaziers).T

m = folium.Map()
gaziers_groupe = folium.FeatureGroup(name='Gaziers').add_to(m)
for nom, gazier in gaziers_df.iterrows():
    gaziers_groupe.add_child(folium.features.Marker(
        location=[gazier.lat, gazier.lon],
        tooltip=nom,
        icon = folium.features.CustomIcon('Icons/{animal}.png'.format(animal=gazier.icon),
                                          icon_size=(40, 40))
    ))

folium.features.Marker(
    location=[gaziers_df.lat.mean(), gaziers_df.lon.mean()],
    tooltip='Point central'
).add_to(m)
m.save('/home/kevin/Programmation/Dash/index.html')
