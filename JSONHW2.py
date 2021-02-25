import json

infile = open("US_fires_9_14.json", "r")


# json load converts data
fire_data = json.load(infile)

# list_of_fires = fire_data["features"]
bright, lons, lats = [], [], []

for fire in fire_data:
    bright_level = fire["brightness"]
    lon = fire["longitude"]
    lat = fire["latitude"]

    if int(bright_level) >= 450:
        bright.append(bright_level)
        lons.append(lon)
        lats.append(lat)

# print(mags[:10])
# print(lons[:10])
# print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# data = [Scattergeo(lon=lons, lat=lats)]
data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "color": bright,
            "colorscale": "viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="US Fires - 9/14/20-9/20/20")
fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="California_Fires_Second_Half.html")