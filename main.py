import folium

m = folium.Map(location=[37.774929, -122.419418], zoom_start=4)
folium.Marker(location=[27.717245, 85.323959], popup='Kathmandu', tooltip='Click for more info', icon=folium.Icon(icon='envelope', color='lightgreen')).add_to(m)
folium.Marker(location=[34.052235, -118.243683], popup='Los Angeles', tooltip='Click for more info', icon=folium.Icon(icon='cloud')).add_to(m)
folium.Marker(location=[41.878113, -87.629799], popup='Chicago', tooltip='Click for more info', icon=folium.Icon(icon='envelope', color='red')).add_to(m)

m