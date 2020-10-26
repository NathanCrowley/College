def read_garda_stations_tuples():
    """ Read and return a list of garda stations. """
    all_stations = []
    file = open('garda_stations.txt', 'r')
    for line in file:
        line = line.replace('\n','')
        new_tuple = tuple(line.split('\t'))
        all_stations.append(new_tuple)
    file.close()
    return all_stations

print(read_garda_stations_tuples())


#Anagram = two list that contain same elements but in different order.

stations = read_garda_stations_tuples()

"----------------------------------------------------------------------------------"


def my_sort(list):
    for tuple in list:
        incident_count = tuple[len(tuple)-1]
        print(incident_count)


my_sort(stations)

