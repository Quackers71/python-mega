import folium
map = folium.Map(location=[53.977048, -1.559376], zoom_start=14, tiles = "Stamen Terrain")

map.add_child(folium.Marker(location=[53.977048, -1.559376], popup="Hi, I am a Marker", icon=folium.Icon('green')))

map.save("Map2.html")
