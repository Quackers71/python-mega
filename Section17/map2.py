import folium
map = folium.Map(location=[53.977048, -1.559376], zoom_start=14, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[53.977048, -1.559376],[53.977048, -1.555376]]:
    fg.add_child(folium.Marker(location=coordinates, popup="My Markers", icon=folium.Icon('green')))

map.add_child(fg)

map.save("Map2.html")
