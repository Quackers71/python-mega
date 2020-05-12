import folium
map = folium.Map(location=[53.977048, -1.559376], zoom_start=14, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[53.977048, -1.559376], popup="40 Beckwith Rd", icon=folium.Icon('green')))
map.add_child(fg)

map.save("Map2.html")
