import folium
import pandas


def create_geo_json():
    """ Create GeoJson multi polygon that adds a contour (polygon) surrounding the countries """
    multi_polygon_map_file = open("world.json", "r", encoding="utf-8-sig").read()

    return folium.GeoJson(
        data=multi_polygon_map_file,
        style_function=lambda x: {'fillColor': style_function(x)}
    )


def style_function(x):
    """ get color according to 2005 population """
    population = x['properties']['POP2005']

    if population > 50000000:
        return 'orange'

    if population > 20000000 :
        return 'yellow'

    return 'green'


def create_map():
    """ Create folium Map centralized in the middle of USA """
    latitude = 39.725715  # Range: from -90 to 90
    longitude = -101.905926  # Range: from -180 to 180

    return folium.Map(
        location=[latitude, longitude],
        zoom_start=4,
        tiles="Mapbox Bright",
        height="100%",
        width="100%",
        position="absolute"
    )


def get_volcanoes_coordinates():
    """ Based on text file return USA volcanoes coordinates, elevation and name """
    lines = pandas.read_csv('Volcanoes_USA.txt')  # This return a pandas.DataFrame

    return zip(
        lines['NAME'],
        lines['ELEV'],
        lines['LAT'],
        lines['LON']
    )


def create_marker(name, elevation, latitude, longitude):
    """ Create a Marker for folium map """
    icon_color = 'green'

    if elevation > 2000:
        icon_color = 'orange'

    if elevation > 3000:
        icon_color = 'red'

    popup = folium.Popup(
        "Name: " + str(name) + "\nElevation: " + str(elevation) + "m",
        parse_html=True
    )

    if elevation < 1500:
        return folium.CircleMarker(
            location=[latitude, longitude],
            popup=popup,
            radius=6,
            fill=True,
            color='grey',
            fill_color=icon_color,
            fill_opacity=0.5
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


feature_group_volcanoes = folium.FeatureGroup(name="Volcanoes")

for name, elevation, latitude, longitude in get_volcanoes_coordinates():
    feature_group_volcanoes.add_child(create_marker(name, elevation, latitude, longitude))


feature_group_multi_polygons = folium.FeatureGroup(name="Countries multi polygons")
feature_group_multi_polygons.add_child(create_geo_json())

layer_control = folium.LayerControl(position='topright', collapsed=False)

map = create_map()
map.add_child(feature_group_volcanoes)
map.add_child(feature_group_multi_polygons)
map.add_child(layer_control)

map.save("map1.html")