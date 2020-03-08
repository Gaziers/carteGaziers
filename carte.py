import folium


gaziers = {
    "Antoine": {
        "icon": "butterfly.png",
        "lat": 45.245892 ,
        "lon": 4.273893
    },
    "Baptiste": {
        "icon": "australia.png",
        "lat": -27.468968,
        "lon": 153.023499
    },
    "Gaspard": {
        "icon": "boar.png",
        "lat": 45.497216,
        "lon": -73.610364
    },
    "Kevin": {
        "icon": "fox.png",
        "lat": 48.856697,
        "lon": 2.351462
    },
    "Mathieu": {
        "icon": "buffalo.png",
        "lat": 43.296174 ,
        "lon": 5.369953
    },
    "Martin": {
        "icon": "dog.png",
        "lat": 45.227385579475566,
        "lon": 4.084994458593769
    },
    "Panda": {
        "icon": "panda.png",
        "lat": 45.21374639731457,
        "lon": 3.968264722265644
    },
    "Thibault": {
        "icon": "chicken.png",
        "lat": 48.390528,
        "lon": -4.486009
    }

}

fmap = folium.Map(location=(45, 4), zoom_start=4)

center = [0, 0]

for gazier in gaziers:
    folium.map.Marker(
        location=(gaziers[gazier]["lat"], gaziers[gazier]["lon"]),
        popup=gazier,
        tooltip=gazier,
        icon=folium.features.CustomIcon(
            gaziers[gazier]["icon"],
            icon_size=[30, 30]

        )
    ).add_to(fmap)

    center = [center[0]+gaziers[gazier]["lat"]/8, center[1]+gaziers[gazier]["lon"]/8]
    
folium.map.Marker(
        location=center,
        popup="Centre des gaziers",
        tooltip="Centre des aziers"
    ).add_to(fmap)

fmap.save("index.html")