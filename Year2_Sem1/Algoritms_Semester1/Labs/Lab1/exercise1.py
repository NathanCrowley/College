import time

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

'''************************* Q1 - First function ***************************'''
def first_function(list):
    start = time.time()
    empty_list =[]
    counter = 0
    for tuple in list:
        empty_list.append(tuple)
        counter +=1
    time_taken = time.time() - start
    return time_taken,counter,empty_list

print(first_function(stations))


'''************************* Q2 - Second function ***************************'''
def second_function(list2):


    start2 = time.time()
    second_list = []
    index = len(list2)-1
    counter =0
    for tuple2 in list2:
        second_list.append(list2[index])
        index -= 1
        counter +=1
    time_taken2 = time.time() - start2
    return time_taken2,counter,second_list


    '''second_list = stations
    second_list.reverse()'''

print(second_function(stations))



'''************************* Q3 - Third function ***************************'''

def thrid_function(list3):

    start_time3 =time.time()
    third_list = [None]
    index =0
    counter = 0
    for tuple3 in list3:
        #third_list.append(None)
        third_list.insert(index,tuple3)
        index +=1
        counter +=1
    time_taken3 = time.time() - start_time3

    return time_taken3,counter,third_list
print(thrid_function(stations))





