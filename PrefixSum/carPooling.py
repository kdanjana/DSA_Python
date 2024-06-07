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
We iterate through every trip and note the changes in passenger numbers at each relevant kilometer mark. 
The kilometerPassengers array in the solution serves as this timeline, with indexes representing kilometer 
marks and values representing the change in the number of passengers at that mark.
When a trip starts (from), we add the number of passengers to the tally at that kilometer mark. 
When the trip ends (to), we subtract the number of passengers from the tally at the drop-off kilometer mark,
since those passengers are no longer in the car.
After tallying all passenger changes, we use the accumulate function to simulate the succession of
passengers over the journey. This function computes a running total that represents the number of passengers
in the car at each kilometer mark. Finally, we check if this running total ever exceeds the car's capacity at 
any point. If it doesn't exceed the capacity, it means that the car can complete all trips successfully. 
Therefore, we return true if the car's capacity is never exceeded, or false if at some point there are too 
many passengers.
"""


def carPooling(trips, capacity):
    # indexes represent kilometer mark, values represents the number of passengers present in car at that kilometer mark
    kilometerPassengers = [0] * 10    #1 <= trips.length <= 1000--given in constraint
    for passengers, fromMark, toMark in trips:
        kilometerPassengers[fromMark] += passengers
        kilometerPassengers[toMark] -= passengers
    print(kilometerPassengers)
    #to calculate the running total of passengers at each location
    prefixSum = [0] * 10
    for i in range(10):
        if i == 0:
            prefixSum[i] = kilometerPassengers[i]
        else:
            prefixSum[i] = prefixSum[i-1] + kilometerPassengers[i]
    print(prefixSum)
    # verify if at any point the number of passengers at mark in prefixSum is exceeded
    # if its <= capacity then the car can complete all trip in trips array succesfully
    if all(NumPassengersAtMark <= capacity for NumPassengersAtMark in prefixSum):
        return True
    else:
        return False
    
print(carPooling([[2,1,5],[3,3,7]],4))
print(carPooling([[2,1,5],[3,3,7]], 5))

    
