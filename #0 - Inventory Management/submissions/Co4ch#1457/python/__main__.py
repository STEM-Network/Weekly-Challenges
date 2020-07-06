from typing import List, Tuple, Dict
from datetime import date
from collections import namedtuple

Tray = namedtuple('Tray', ['id', 'exp', 'count'])


def select_zone(
                zone_name: str,
                zones: Dict[str, List[List[List[Tray]]]] = {}
               ) -> Union[List[List[List[Tray]]], None]:
    """Select an appropriate zone from the list of available zones

    Args:
        zone_name (str): The zone name we wish to search through
        zones (Dict[str, List[List[List[Tray]]]]): The zone names in the warehouse
    
    Return:
        Union[List[List[List[str]]], None]: The zone to be viewed,
                                      none if it does not exist
    """
    return zones.get(zone_name)


def scanned_barcode(barcode: str, stack: List[List[Tray]], depth: int) -> List[List[Tray]]:
    """Provided a scanned code, return the components of the code

    Args:
        barcode (str): The barcode of the scanned item
        stack (List[List[Tray]]): The stack of boxes being viewed
        depth (int): The row we are viewing

    Returns:
        str: The id of the item scanned
        date: The expiration date
        int: The number of trays in the scanned item
    """
    count = int(barcode[-2:])
    exp = barcode[6:-2]
    last_day = date(exp[-2:], exp[2:-2], exp[:2])
    item_id = barcode[:6]
    t = Tray(item_id, last_day, count)
    stack[depth].add(t)
    return stack


def next_stack(zone: List[List[List[Tray]]],
                stack: List[List[Tray]]) -> Union[List[List[Tray]], None]:
    """Looking at a current stack, provide the next stack to be viewed

    Args:
        zone (List[List[List[Tray]]]): The zone being searched through
        stack (List[List[Tray]]): The stack being viewed

    Returns:
        Union(List[List[Tray]], None): The next stack to be viewed, None if the last row

    There's definitely a better way to do this...
    """
    try:
        pos = zone.index(stack)
    except ValueError:
        return None
    return zone[pos + 1] if pos == len(stack) - 1 else None


def next_row(stack: List[List[Tray]], depth: int) -> int:
    """Provided a current position in a stack, move to the next location

    Args:
        stack (List[List[Tray]]): The current stack being viewed
        depth (int): The position in the stack currently being viewed

    Returns:
        int: The position to be viewed next, -1 at the end of the stack
    """
    if (next := depth + 1) >= len(stack):  # I am the walrus
        next = -1
    return next


def find_item(
              item_id: str, 
              zone_input: str,
              warehouse: Dict[str, List[List[List[Tray]]]]
              ) -> Tuple[bool, Union[date, None], int]:
    """Provided an id for an item, find the item inside a provided zone

    Args:
        item_id (str): The id to find
        zone_input (str): The zone to search
        warehouse (Dict[str, List[List[List[Tray]]]]): The dict containing all zones

    Returns:
        bool: Whether the item exists
        date: The expiration date, None if the item is invalid
        int: How many items are in the tray

    Would like to shorten this if possible.
    """
    if not (zone := select_zone(zone_input, warehouse)) or len(zone) == 0:
        return (False, None, 0)
    current = zone[0]
    depth = 0
    count = 0
    are_searching = True
    found = False
    last_day = None
    while are_searching:
        bc = current[depth]
        curr_id, d, count = scanned_barcode(current[depth])
        if curr_id == item_id:
            are_searching = False
            found = True
            print(f'Found a matching item ID {item_id} for barcode {bc}. \
                    Number of items in the tray: {count} \
                    Expiration Date: {str(last_day)}')
        print(f'{bc} is not a match. You are viewing tray {depth + 1} \
                 of {len(current)}.')
        if depth + 1 == len(current):
            print('This is the last tray, viewing next stack')
            current, depth = next_stack, 0
        else:
            depth = next_row(current, depth)
        if not current:  # if we just completed the last stack
                print(f'Item id {item_id} not found in this zone')
                are_searching = False
    return (found, last_day, count)