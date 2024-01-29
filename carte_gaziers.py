import folium
import numpy as np

class gazier :
    def __init__(self, name : str, latitude : float, longitude : float, image : str) -> None:
        self.name = name
        self.latitude = latitude
        self.longitude =longitude
        self.image = image

gaziers = [
    gazier('Panda', 43.2990, 5.3749, 'https://dl2.macupdate.com/images/icons256/52971.png'),
    gazier('Martin', 43.5600, 6.9629, 'https://pupuphooray.com/wp-content/uploads/2019/03/dog-icon.png'),
    gazier('Thibaut', 45.9070, 6.1084, 'https://images.emojiterra.com/twitter/v12/512px/1f414.png'),
    gazier('Gaspard', 45.7633, 4.8624, 'https://www.pngrepo.com/png/232688/170/baboon.png'),
    gazier('Mathieu', 43.2875, 5.3621, 'https://cdn1.iconfinder.com/data/icons/animal-flat-2/128/animal_buffalo-u-zoo-512.png'),
    gazier('Baptiste', 43.7053, 7.2656, 'https://cdn2.iconfinder.com/data/icons/animals-92/28/animal_lineal_color-19-512.png'),
    gazier('Antoine', 48.1246, 5.1417, 'https://www.pngrepo.com/png/256208/512/butterfly.png'),
    gazier('Kevin', 43.6075, 3.8740, 'https://cdn.iconscout.com/icon/premium/png-256-thumb/fox-91-563338.png')
]

# Compute epicenter coordinates
epicenter = [np.mean([gazier.latitude for gazier in gaziers]), np.mean([gazier.longitude for gazier in gaziers])]

# Initialize map with focus on epicenter
fmap = folium.Map(location=epicenter, zoom_start=6)

# Add the epicenter to the map
icon = folium.Icon(color="green") # Use default folium icon
folium.Marker(location=epicenter, popup="Centre des Gaziers", icon=icon).add_to(fmap) # Add to map

# Add the different gaziers to the map
for gazier in gaziers:
    icon = folium.features.CustomIcon(gazier.image, icon_size=40) # Create custom icon
    folium.Marker(location=[gazier.latitude, gazier.longitude], icon=icon, popup=gazier.name).add_to(fmap) # Add to map

fmap.save("index.html") # Generate html file
