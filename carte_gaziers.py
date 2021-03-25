import folium
import numpy as np

gaziers = [{"nom": "Panda", "lat": 45.45, "lon": -73.55, "image": "https://dl2.macupdate.com/images/icons256/52971.png"},
{"nom": "Martin", "lat": 43.55, "lon": 6.93, "image": "https://pupuphooray.com/wp-content/uploads/2019/03/dog-icon.png"},
{"nom": "Thibault", "lat": 47.216307, "lon": -1.558252, "image": "https://images.emojiterra.com/twitter/v12/512px/1f414.png"},
{"nom": "Gaspard", "lat": 45.5182122, "lon": -73.5727788, "image": "https://www.pngrepo.com/png/232688/170/baboon.png"},
{"nom": "Mathieu", "lat": 43.3, "lon": 5.4, "image": "https://cdn1.iconfinder.com/data/icons/animal-flat-2/128/animal_buffalo-u-zoo-512.png"},
{"nom": "Baptiste", "lat": -33.818398, "lon": 150.972911, "image": "https://cdn2.iconfinder.com/data/icons/animals-92/28/animal_lineal_color-19-512.png"},
{"nom": "Antoine", "lat": 45.246792, "lon": 4.260668, "image": "https://i.pinimg.com/originals/ce/76/b8/ce76b874769fa0c3761bc0a9bc064309.png"},
{"nom": "Kévin", "lat": 43.60750775047381, "lon": 3.8740151541513663, "image": "https://cdn.iconscout.com/icon/premium/png-256-thumb/fox-91-563338.png"}
]

epicentre = [np.mean([gazier["lat"] for gazier in gaziers]),
np.mean([gazier["lon"] for gazier in gaziers])]
fmap = folium.Map(location=epicentre, zoom_start=2)
icon = folium.Icon(color="green")
folium.Marker(location=epicentre, popup="Centre des Gaziers", icon=icon).add_to(fmap)  #adding it to the map

for gazier in gaziers:
    icon = folium.features.CustomIcon(gazier["image"],icon_size=40)  # Creating a custom Icon
    folium.Marker(location=[gazier["lat"], gazier["lon"]],icon=icon, popup=gazier["nom"]).add_to(fmap)  #adding it to the map

fmap.save("index.html")
