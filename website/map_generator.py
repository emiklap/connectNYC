import folium

mapObj = folium.Map(location=[40.73112880602221, -73.89060974121095], tiles="Cartodb Positron", zoom_start=10)

tooltip = folium.GeoJsonTooltip(fields=["neighborhood"])

html = '''<a href="website/templates/home">Select</a>'''

iframe = folium.IFrame(html, width=100, height=100)

popup = folium.Popup(iframe, max_width=100)

folium.GeoJson("website/pediacitiesnycneighborhoods.geojson", name="nyc", zoom_on_click=True, popup=popup, tooltip=tooltip, 
               highlight_function=lambda feature: {"fillColor": ("green")}).add_to(mapObj)

mapObj.save(outfile="website/templates/out_map.html")