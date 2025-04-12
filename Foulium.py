import folium
import pandas


def trProvices():
    cityData = pandas.read_excel("myCodes/mapStatistics/tr-cities.xlsx")
    worldMap = folium.Map(tiles="CartoDB Voyager")
    cityList = list(cityData["City"])
    xList = list(cityData["Enlem"])
    yList = list(cityData["Boylam"])
    for x, y, name in zip(xList, yList, cityList):
        worldMap.add_child(folium.Marker(
            location=(x, y), icon=folium.Icon(color="green"), popup=name))
    worldMap.save("myCodes/mapStatistics/Türkiye_ileçeler.html")
# trProvices()

def corona_virus():

    def calculate_radius(case, values, calc):
        if case < values[0]:
            return calc[0]
        elif case < values[1]:
            return calc[1]
        elif case < values[2]:
            return calc[2]
        else:
            return calc[3]

    def calculate_color(case, values, color):
        if case < values[0]:
            return color[0]
        elif case < values[1]:
            return color[1]
        elif case < values[2]:
            return color[2]
        else:
            return color[3]

    cv_data = pandas.read_excel(
        "myCodes/mapStatistics/world_coronavirus_cases.xlsx")

    worldMap = folium.Map(tiles="CartoDB Voyager")
    sum_case_map = folium.FeatureGroup("Toplam vaka sayılar")
    death_rate_map = folium.FeatureGroup("Ölüm oranı")
    active_case_map = folium.FeatureGroup("Aktif vaka dağılımı")
    test_rate_map = folium.FeatureGroup("Test oranı haritası")
    demographic_map = folium.FeatureGroup("Nufus dağılım haritısı")

    x_list = list(cv_data["Enlem"])
    y_list = list(cv_data["Boylam"])
    sum_cases = list(cv_data["Toplam Vaka"])
    death_rates = list(cv_data["Vefat Edenler"])
    active_cases = list(cv_data["Aktif Vakalar"])
    test_counts = list(cv_data["Toplam Test"])
    populations = list(cv_data["Nüfus"])
    colors = ("green", "white", "orange", "red")
    opacity = 0.4
    values = (100000, 300000, 750000)
    radius = (50000, 100000, 200000, 400000)
    raito = (2.5, 5, 7.5)
    raito_radius = (25000, 50000, 100000, 20000)
    for x, y, sum in zip(x_list, y_list, sum_cases):
        sum_case_map.add_child(folium.Circle(
            location=(x, y),
            radius=calculate_radius(
                sum, values, radius),
            color=calculate_color(sum, values, colors),
            fill=calculate_color(sum, values, colors), fill_opacity=opacity))
    for x, y, sum, death_rate in zip(x_list, y_list, sum_cases, death_rates):
        death_rate_map.add_child(folium.Circle(
            location=(x, y),
            radius=calculate_radius(
                ((death_rate/sum)*100), raito, raito_radius),
            color=calculate_color(
                ((death_rate/sum)*100), raito, colors),
            fill=calculate_color(((death_rate/sum)*100), raito, colors), fill_opacity=opacity)
        )
    for x, y, active_case in zip(x_list, y_list, active_cases):
        active_case_map.add_child(folium.Circle(
            location=(x, y),
            radius=calculate_radius(
                active_case, values, radius),
            color=calculate_color(
                active_case, values, colors),
            fill=calculate_color(active_case, values, colors), fill_opacity=opacity))
    for x, y, population, test_count in zip(x_list, y_list, populations, test_counts):
        test_rate_map.add_child(folium.Circle(
            location=(x, y),
            radius=calculate_radius(
                ((test_count/population)*100), raito, raito_radius),
            color=calculate_color(
                ((test_count/population)*100), raito, colors),
            fill=calculate_color(((test_count/population)*100), raito, colors), fill_opacity=opacity)
        )
    demographic_map.add_child(folium.GeoJson(
        data=(open("myCodes/mapStatistics/world.json",
              "r", encoding="utf-8-sig").read()),
        style_function=lambda x: {'fillColor':
                                  calculate_color(x["properties"]["POP2005"],
                                                  (20000000, 50000000, 100000000), colors)
                                  }))
    worldMap.add_child(sum_case_map)
    worldMap.add_child(death_rate_map)
    worldMap.add_child(demographic_map)
    worldMap.add_child(active_case_map)
    worldMap.add_child(test_rate_map)

    worldMap.add_child(folium.TileLayer("OpenStreetMap"))
    worldMap.add_child(folium.TileLayer("Cartodb dark_matter"))

    worldMap.add_child(folium.LayerControl())
    worldMap.save("myCodes/mapStatistics/world_coronavirus.html")


corona_virus()
