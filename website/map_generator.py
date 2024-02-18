import folium

mapObj = folium.Map(location=[40.73112880602221, -73.89060974121095], tiles="Cartodb Positron", zoom_start=10)

tooltip = folium.GeoJsonTooltip(fields=["neighborhood"])

folium.GeoJson("website/pediacitiesnycneighborhoods.geojson", name="nyc", zoom_on_click=True, tooltip=tooltip, 
               highlight_function=lambda feature: {"fillColor": ("green")}).add_to(mapObj)

mapObj.save(outfile="website/templates/out_map.html")