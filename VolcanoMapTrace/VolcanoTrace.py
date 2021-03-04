import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
el = list(data["ELEV"])

map = folium.Map(location=[32.085328, 34.811698],zoom_start= 10)

fgv = folium.FeatureGroup(name="Volcanoes")


def colorpick(elevation):
    if  1000 <= elevation <=2000:
        return "green"
    elif 1000 <= elevation <= 3000:
        return "orange"
    else: return "red"

for lat1, lon1, el1 in zip(lat, lon,el):
    fgv.add_child(folium.CircleMarker(location=(lat1, lon1), radius=6, popup=str(el1), color =(colorpick(el1))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
             style_function= lambda x: {"fillColor" : "green" if x["properties"]["POP2005"] < 10000000 else
                                        "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("RGmap.html")