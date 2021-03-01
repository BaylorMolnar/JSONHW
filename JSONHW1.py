import json

# program for fires 9/1-9/13
infile = open("US_fires_9_1.json", "r")


# json load converts data
fire_data = json.load(infile)

# list_of_fires = fire_data["features"]
bright, lons, lats = [], [], []

# pull data from json and only append to list if greater than 450 brightness
for fire in fire_data:
    bright_level = fire["brightness"]
    lon = fire["longitude"]
    lat = fire["latitude"]

    if int(bright_level) >= 450:
        bright.append(bright_level)
        lons.append(lon)
        lats.append(lat)

# import plotly

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# data list
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
# formatting
my_layout = Layout(title="US Fires - 9/1/20-9/13/20")
fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="California_Fires_First_Half.html")