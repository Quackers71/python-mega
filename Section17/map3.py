import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[37.7749, -122.4194], zoom_start=6, tiles = "Stamen Terrain") # San Francisco

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="My Markers", icon=folium.Icon('green')))

map.add_child(fg)

map.save("Map3.html")