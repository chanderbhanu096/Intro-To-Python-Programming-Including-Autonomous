import numpy as np

# A one-lane road, represented by an array
# Here is a 1x7 road
road = np.array(['r', 'r', 'r', 'r', 'r', 's', 'r'])
def find_stop_index(road):
    length = len(road)
    stop=0
    for index in range(0, length):
        value = road[index]
        print("",index)
        if value == "s" :
            stop=index-1
            print("",stop)
            break
    ## TODO: Iterate through the road array
    ## TODO: Check if a stop sign ('s') is found in the array
    ## If one is, break out of your iteration
    ## and return the value of the index that is *right before* the stop sign
    ## Change the stop_index value
    stop_index = index
    return stop_index

find_stop_index(road)