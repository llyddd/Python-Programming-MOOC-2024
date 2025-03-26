# tee ratkaisu tänne
# Write your solution here

import math

def formula(longitude1,latitude1,longitude2, latitude2):
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def get_station_data(filename: str):
    stations = {}
    with open(filename) as new_file:

        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(';')
            
            if parts[6] == "id":
                continue
            longitude = parts[0]
            latitude = parts[1]
            name = parts [3]
            
            stations[name] = (float(longitude), float(latitude))
        return stations
def distance(stations: dict, station1: str, station2: str):
    for name, (longitude, latitude) in stations.items():
        if name == station1:
            longitude,latitude = stations[name]
            longitude1 = longitude
            latitude1 = latitude

        elif name == station2:
            longitude,latitude = stations[name]
            longitude2 = longitude
            latitude2  = latitude
    
    #print(longitude1, latitude1)
    distance_km = formula(longitude1,latitude1,longitude2, latitude2)
    return distance_km



def greatest_distance(stations: dict):
    
    keys_list = []
    for key in stations:
        keys_list.append(key)
    #print(keys_list)
    distance = []
    station_list = []
    result = ()
    # Iterate through each pair of keys and multiply their values
    for i in range(len(keys_list)):
        #print(i)
        for j in range(i + 1, len(keys_list)):
            #
            station1 = keys_list[i]
            station2 = keys_list[j]
            longitude1, latitude1 = stations[station1]
            longitude2, latitude2 = stations[station2]
            station_list.append([station1,station2])
            distance.append(formula(longitude1,latitude1,longitude2, latitude2))
           
    
    greatest_distance = max(distance)
    
    index = distance.index(greatest_distance)
    for item in range(len(distance)):
            if item == index:
                first_station, second_station = station_list[item]
                result = result + ((first_station, second_station, greatest_distance))
                return result
    #return 
if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)

    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)


    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)