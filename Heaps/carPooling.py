""" 
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and 
drive west). You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi]
indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them 
off are fromi and toi respectively. The locations are given as the number of kilometers due east from 
the car's initial location. Return true if it is possible to pick up and drop off all passengers for all 
the given trips, or false otherwise.
Intution:
A car has a certain number of empty seats (given by capacity), and it can only drive in one direction—east.
We are provided with an array trips, where each element is a trip described by three integers: numPassengers, 
from, and to. These respectively represent the number of passengers for that trip, the kilometer mark where
the passengers will be picked up, and the kilometer mark where they will be dropped off. Our task is to 
determine if the car can successfully complete all the given trips without ever exceeding its seating capacity.
Imagine a timeline where each point is a kilometer mark where some action takes place—a pick-up or a drop-off.
TC-O(nlogn)
"""

import heapq


def carPooling(trips,capacity):
    # key in minheap is tuple (pickup, number of passengers added to car) or(drop point, number of passengers removed from car)
    minHeap = []
    for passengers, pickup, drop in trips:
        heapq.heappush(minHeap, (pickup, passengers))
        heapq.heappush(minHeap, (drop, -passengers))
    #number of passengers at any given moment
    numPassengers = 0
    while minHeap:
        trip = heapq.heappop(minHeap)
        numPassengers += trip[1]
        if numPassengers > capacity:
            return False
    return True


print(carPooling([[2,1,5],[3,3,7]], 5))
print(carPooling([[2,1,5],[3,3,7]], 4))
        
        
    