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

#print(read_garda_stations_tuples())


#Anagram = two list that contain same elements but in different order.

stations = read_garda_stations_tuples()
print(stations)


'''*********************** Question 2 (i) *************************'''


'''def lin_search(l):
    user = input("Enter station you would like to find. >>>>")
    for tuple in l:
        if user == tuple[0]:
            print(tuple)
            break
    else:
        print("This station does not exist.")

lin_search(stations)'''

'''*********************** Question 2 (ii)*************************'''
#def binary_search(l2):




binary_search(stations)