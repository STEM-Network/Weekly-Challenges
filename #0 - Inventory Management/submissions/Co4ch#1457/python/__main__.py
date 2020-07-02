from typing import List, Tuple, Dict
from datetime import date


def select_zone(zones: List[str], zone_name: str) -> bool:
    """Select an appropriate zone from the list of available zones

    Args:
        zones (List[str]): The zones inside the store house
        zone_name (str): The zone name we wish to search through
    
    Return:
        int: The index of the requested zone (-1 if invalid)
    """
    return zone_name in zones


def obtain_barcode(stack: List[str], depth: int) -> str:
    """Provided a row and column for a tray, retrieve the barcode for the item

    Args:
        stack (List[str]): The current stack being viewed
        int (int): The column of a tray

    Returns:
        str: The barcode for a tray at the provided row and column
    """
    return stack[depth]


def move_stacks(zone: List[List[str]],
                stack: List[str]) -> Union[List[str], None]:
    """Looking at a current stack, provide the next stack to be viewed

    Args:
        zone (List[List[str]]): The zone being searched through
        stack (List[str]): The stack being viewed

    Returns:
        Union(List[str], None): The next stack to be viewed, None if the last row

    There's definitely a better way to do this...
    """
    for row, trays in enumerate(zone[:-1]):
        if trays[0] == stack[0]:
            return zone[row + 1]
    return None


def move_rows(stack: List[str], depth: int) -> int:
    """Provided a current position in a stack, move to the next location

    Args:
        stack (List[str]): The current stack being viewed
        depth (int): The position in the stack currently being viewed

    Returns:
        int: The position to be viewed next, -1 at the end of the stack
    """
    if (next := depth + 1) >= len(stack):  # I am the walrus
        next = -1
    return next


def find_item(
              item_id: str, 
              warehouse: Dict[str, List[List[str]]]
              ) -> Tuple[bool, Union[date, None], int]:
    """Provided an id for an item, find the item inside a provided zone

    Args:
        item_id (str): The id to find
        zone (List[List[str]]): The zone to search

    Returns:
        bool: Whether the item exists
        date: The expiration date, None if the item is invalid
        int: How many items are in the tray

    Would like to shorten this if possible.
    """
    name = input('Select a zone to search')
    if not select_zone(name) or len((zone := warehouse[name])[name]) == 0:
        return (False, None, 0)
    current = zone[0]
    depth = 0
    count = 0
    are_searching = True
    found = False
    last_day = None
    while are_searching:
        bc = obtain_barcode(current, depth)
        if bc[:len(item_id)] == item_id:
            are_searching = False
            found = True
            count = bc[-2:]
            exp = bc[len(item_id):-2]
            last_day = date(exp[-2:], exp[2:-2], exp[:2])
            print(f'Found a matching item ID {item_id} for barcode {bc}. \
                    Number of items in the tray: {count} \
                    Expiration Date: {str(last_day)}')
        print(f'{bc} is not a match. You are viewing tray {depth + 1} \
                 of {len(current)}.')
        if depth + 1 == len(current):
            print('This is the last tray, viewing next stack')
            current, depth = determine_movement(zone, current, depth, 's')
        else:
            current, depth = determine_movement(zone, current, depth)
        if not current:  # if we just completed the last stack
                print(f'Item id {item_id} not found in this zone')
    return (found, last_day, count)


def determine_movement(
                       zone: List[List[str]],
                       stack: List[str],
                       depth: int,
                       resp: str = None) -> Tuple[Union[List[str], None], int]:
    """Determine whether the user wants to move to the next tray or stack

    Args:
        zone (List[List[str]]): The zone being viewed
        stack (List[str]): The stack being viewed

    Returns:
        str: s or t for moving to the next stack or tray
    """
    while not resp or 's' not in resp or 't' not in resp:
        resp = input('Would you like to move to the next (t)ray \
                            or the next (s)tack? ').lower()
        print('Invalid option, try again')
    if 's' in resp:
        c_stack = move_stacks(zone, stack)
        return (c_stack, 0)
    elif 't' in resp:
        depth = move_rows(stack, depth)
        return (stack, depth)
