# #2- Air Traffic Control

You have been tasked with developing a collision detection system for a local airfield.

The system on which your software will be running is attached to three ground based radar stations which will report the following for every aircraft in the airspace, once per second, in order of signal strength:
 - azimuth angle to craft
 - elevation angle to craft
 - reflected signal strength from craft

The signal strength is determined by the objects angular size from the radars point of view (it is proportional to both distance from the radar, and size of the craft). 

The ground stations are placed in an equilateral triangle, with side length 1KM, equidistant from the tower of the airfield, with one ground station directly north. This system covers all airspace over ground < 500KM from the tower.

All aircraft must maintain a minimum safe separation distance of 5KM, and will travel in a straight line at constant speed until instructed otherwise.

Your software must provide advanced warning, given two samples from each ground station, of any impending separation issues, ordered soonest first.

Allowed assumptions:
 - the closest points between consecutive radar scans are the same aircraft.
 - the visible cross sectional area of each craft is the same from all radar station.
 - Ground stations will ignore (not report) any craft not in the controlled airspace.
 - All ground stations have enough range to cover the entire controlled airspace.

### Optional read:
<details>
    <summary> A rough breakdown of the problem into more manageable steps</summary>

     1 Associate signals between ground stations, in order to determine all crafts position in space
        (The first signal from each ground station wont necessarily be from the same aircraft)

     2 Do the above for two radar scans, and associate the points in each which are from the same craft.
        (Note the first allowed assumption)

     3 Determine the velocity of all craft in the airspace from the above position sample set.

     4 list any pairs of craft that will become closer than 5KM in the near future.

     5 Order that list by time until collision.
</details>