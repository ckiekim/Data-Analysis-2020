# conda install -c anaconda flask
from flask import Flask
import folium
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (37.550966, 126.849532)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

@app.route('/marker')
def markerr():
    df = pd.read_csv('address3.csv')
    df['icon'] = ['map-marker', 'cloud', 'gift', 'info-sign', 'ok-circle']
    color_dict = {'Clear': 'blue', 'Snow': 'white', 'Rain': 'gray', 'Extreme': 'red', 'Clouds': 'orange', 'Mist': 'green'}
    mapping = folium.Map(location=[df.lat.mean(), df.lng.mean()],
                    zoom_start=12)
    for i in df.index:
        folium.Marker(
            location=[df.lat[i], df.lng[i]],
            popup=df.bldg[i],
            tooltip=f'{df.desc[i]}, {df.temp[i]}',
            icon=folium.Icon(color=color_dict[df.weather[i]], icon=df.icon[i])
        ).add_to(mapping)
    return mapping._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)
