def find_station(stations, name):
    for i in range (len(stations)):
        if stations[i] == name:
            return i
    return -1


def count_stops(stations, start, stop):
    starting = find_station(stations, start)
    ending = find_station(stations, stop)

    if starting == -1 or ending == -1:
        return -1
    
    if starting > ending :
        return starting - ending
    else :
        return ending - starting 
    


