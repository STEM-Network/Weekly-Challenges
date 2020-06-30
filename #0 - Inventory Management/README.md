# #0- Inventory Management

A company stores a lot of stock in a fridge. They use Stacks of trays, arranged in a grid. This grid is broken into sections (ex. "Produce", "Deli", "Meat"). 

The aim is to provide a simple back-end for the new inventory management system of this company.

At the start of the day, an employee selects a zone and scans every tray in every stack from top to bottom in each stack & back to front in each row, left to right.

```
Example stack scanning order
[04] [08] [12] [16]
[03] [07] [11] [15]
[02] [06] [10] [14]
[01] [05] [09] [13]
-------FRONT-------
```

The front-end for this has already been created & wishes to send the following events to your implementation.

1. User selects a zone
2. Stream of scanned barcodes for Stack 1
3. User selects next stack OR next row 
4. Repeat from 2 until the zone is finished

The barcodes are of the following format: 

```
12345630062010
123456 - Item ID,
      300620 - Best before date of all items in this tray
      30     - Day
        06   - Month
          20 - Year (2020)
            10 - The number of items in that tray

So in the example above, we have a tray containing 10 of item "123456" expiring on the 30th of June 2020.
```

Your back-end is expected to use these events to form a map of the storage room, containing all of the information from the barcodes. Such that a user, at a later time, can request more stock of a particular item, at which point you should return the location (ZoneName/Row/Stack/height in stack) of the earliest date of that item.

You can choose to implement this in one of three ways

- Event-Stream based
- One function per event, effecting global variables
- One function per event, with a data storage reference also passed

As a quick overview, the required events would be:
 - SelectZone (ZoneName)
 - ScannedBarcode (Barcode)
 - NextStack
 - NextRow
 - FindItem (ItemID)

I look forward to reviewing any submissions & I am more than happy to help!

Just contact ``Azurethi#0788`` on discord.