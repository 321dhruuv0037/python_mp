import pandas as pd
import folium
from folium.plugins import HeatMap

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv('hmap.csv')

# Create a map centered on a specific location
m = folium.Map(location=[18.932245, 72.826439], zoom_start=6)

# Create a heatmap layer from the data
heat_data = [[row['latitude'], row['longitude']] for index, row in data.iterrows()]
heatmap = HeatMap(heat_data, name='Heatmap')

# Add the heatmap layer to the map
heatmap.add_to(m)
#text marker


# Add a layer control to the map
folium.LayerControl().add_to(m)
#western line
folium.PolyLine([(18.9354, 72.8262),(18.9442, 72.8239),(18.9536, 72.8174),(18.9591, 72.8132),(18.9696, 72.8196),(18.9827, 72.8193)
,(19.0088, 72.8308)
,(19.0111, 72.8403)
 ,(19.0173, 72.8426)
 ,(19.0271, 72.8464)
 ,(19.0395, 72.8445)
 ,(19.0544, 72.8402)
 ,(19.0686, 72.8394)
 ,(19.0814, 72.8416)
 ,(19.0972, 72.8445)
 ,(19.1197, 72.8464)
,(19.1365, 72.8497)
,(19.1542, 72.8534)
,(19.1647, 72.8491)
,(19.1867, 72.8486)
,(19.204431413672715, 72.85164270837505)
,(19.2292, 72.8572)
,(19.2502, 72.8592)
 ,(19.2813, 72.8563)
 ,(19.3103, 72.8517)
 ,(19.3465, 72.8545)
 ,(19.3802, 72.8395)
 ,(19.4186, 72.8179)
,(19.455235541869268, 72.81211431208968),(19.519096449558383, 72.85036910889094),(19.577117893783946, 72.82171623907293),(19.6982688067134, 72.772179156276),(19.990148370578478, 72.74472504650069)],color="green",tooltip="Western Line",weight=3).add_to(m)

folium.Marker(location=[19.455134379429648, 72.81202848139804],
              popup=folium.Popup('<i>Western Line</i>'),
              tooltip='Western Line',
              icon=folium.DivIcon(html="""Western Line""",
                                  class_name="mapText"),
              ).add_to(m)

# inject html into the map html
m.get_root().html.add_child(folium.Element("""
<style>
.mapText {
    white-space: nowrap;
    color:green;
    font-size:medium
}
</style>
"""))
#csmt to kasara
folium.PolyLine([(18.943888,72.835991),(18.994736760414902, 72.83299728510069),(19.020330448510123, 72.84365954445657),(19.066573611668673, 72.87980951393833),(19.085515812592636, 72.90727222557408),(19.18659041458438, 72.97536110837471),(19.19042930746032, 73.02342671394041),(19.18871434223293, 73.04228938324867),(19.23571726600612, 73.13078415340435),(19.29602463586944, 73.20378245441398),(19.439762665560814, 73.30787021023416),(19.64852859016493, 73.47304712558349)],color="blue",tooltip="Central Line").add_to(m)
#kalyan to khopoli
folium.PolyLine([(19.23571726600612, 73.13078415340435),(19.16699440588468, 73.23863896084042),(18.91283348037467, 73.3207955409171),(18.789286786303602, 73.34539545440576)],color="blue",tooltip="Central Line").add_to(m)
folium.Marker(location=[19.23644145356165, 73.13028936975887],
              popup=folium.Popup('<i>Central Line</i>'),
              tooltip='Central Line',
              icon=folium.DivIcon(html="""Central Line""",
                                  class_name="mapText"),
              ).add_to(m)
#harbour csmt to panvel
folium.PolyLine([(18.940295750335533, 72.83575288324467),(18.962173966262736, 72.83900556789912),(18.988393871718458, 72.84329590608344),(19.0162622023617, 72.85879774048796),(19.067444858086915, 72.8800346016453),(19.048343621374624, 72.93196402557346),(19.06339879342969, 72.99882074488211),(19.055727544411585, 73.017959166992),(19.02220959140532, 73.0189194026994),(19.01947799290236, 73.03948562689445),(19.02666691178611, 73.05961378456648),(19.008516434583814, 73.09459223336893),(18.992155097791116, 73.12093264019435)],color="yellow",tooltip="Harbour Line").add_to(m) 
#harbor wadala to goregaon
folium.PolyLine([(19.0162622023617, 72.85879774048796),(19.041049756832933, 72.84699720172428),(19.056530893119035, 72.83989345615814),(19.068513041300847, 72.8399588909093),(19.164918718417084, 72.84922634833158)],color="yellow",tooltip="Harbour Line").add_to(m)
#metro line 9 gkp-vsv
folium.PolyLine([(19.08680000156715, 72.90811058324704),(19.09658860912144, 72.89500762742944),(19.10809761674883, 72.87981916604637),(19.121114420719188, 72.8482312390653),(19.130568159099553, 72.82134052371956)],color="cyan",tooltip="Metro Line 9").add_to(m)
#thane vashi line
folium.PolyLine([(19.18675254065755, 72.97540402372054),(19.176037824932855, 72.99472545441198),(19.103518084649536, 73.01215414724949),(19.07580016180758, 73.01782716790103),(19.06339879342969, 72.99882074488211)],color="purple",tooltip="TransHarbour Line").add_to(m)

# inject html into the map html
m.get_root().html.add_child(folium.Element("""
<style>
.mapText {
    white-space: nowrap;
    color:green;
    font-size:medium
}
</style>
"""))
folium.LayerControl(overlay={
    'Markers': '<span style="color: green">Western Line</span> | <span style="color: blue">Central Line</span> | <span style="color: yellow">Harbour Line</span>',
}).add_to(m)




# Save the map to an HTML file
m.save('heatmap.html')
