import folium
import pandas

latitude = 39.725715  # Range: from -90 to 90
longitude = -101.905926  # Range: from -180 to 180

map = folium.Map(
    location=[latitude, longitude],
    zoom_start=4,
    tiles="Mapbox Bright",
    height="100%",
    width="100%",
    position="absolute"
)


def get_volcanoes_coordinates():
    lines = pandas.read_csv('Volcanoes_USA.txt')  # This return a pandas.DataFrame

    return zip(
        lines['NAME'],
        lines['ELEV'],
        lines['LAT'],
        lines['LON']
    )


def create_marker(name, elevation, latitude, longitude):
    icon_color = 'green'

    if elevation > 2000:
        icon_color = 'orange'

    if elevation > 3000:
        icon_color = 'red'

    popup = folium.Popup(
        "Name: " + str(name) + "\nElevation: " + str(elevation) + "m",
        parse_html=True
    )

    icon = folium.Icon(
        color=icon_color,
        icon_color="yellow",
        icon='info-sign',
        angle=0
    )

    return folium.Marker(
        location=[latitude, longitude],
        popup=popup,
        icon=icon
    )


feature_group = folium.FeatureGroup(
    name="May Map"
)


for name, elevation, latitude, longitude in get_volcanoes_coordinates():
    feature_group.add_child(create_marker(name, elevation, latitude, longitude))

map.add_child(feature_group)

map.save("map1.html")