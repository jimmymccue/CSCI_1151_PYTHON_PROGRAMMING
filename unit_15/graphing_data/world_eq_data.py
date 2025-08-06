from pathlib import Path
import json
import plotly.express as px

# Read a file from Json
path = Path('eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
easier_to_read_eq_data = json.loads(contents)

# Write a file to Json
# path = Path('easy_to_read_eq_data.json')
# new_contents = json.dumps(easier_to_read_eq_data, indent=4)
# path.write_text(new_contents)

all_eq_data = easier_to_read_eq_data['features']

# Extract the magnatude, coordinates
mags = []
longs = []
lats = []
eq_titles = []

for eq_data in all_eq_data:
    try :
        mag = eq_data['properties']['mag']
        eq_title = eq_data['properties']['title']
        long = eq_data['geometry']['coordinates'][0]
        lat = eq_data['geometry']['coordinates'][1]
        # print(mag, long, lat)
    except ValueError as e:
        print('Error with data')
    else:
        mags.append(mag)
        longs.append(long)
        lats.append(lat)
        eq_titles.append(eq_title)

title = 'Global Earthquakes in 30 Days'
fig = px.scatter_geo(lon = longs, 
    lat = lats, 
    title = title, 
    size=mags, 
    color=mags,
    color_continuous_scale='hot',
    projection='natural earth',
    labels={'color': 'Magnitude'},
    hover_name=eq_titles)
fig.show()