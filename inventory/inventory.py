#!/usr/bin/python3

from __future__ import annotations

import copy
import heapq
import logging

_LOGGER = logging.getLogger(__name__)


def compute_inventory(elements: list[int], lights: list[int]) -> dict[int, int]:
    """Compute needed inventory.

    Given a set of element sizes (e.g. 327, 120) and a set of sizes of available
    lights in the inventory (e.g. 100, 20, 7) compute the amount of each light
    size in the inventory that is needed (e.g. 4x100, 2x20, 1x7).
    """

    # Make the element list into a heap , 
    _LOGGER.debug(f"Elements: {elements}")
    result = {}
    lights.sort(reverse=True)
    remaining_elements = copy.copy(elements)
    while remaining_elements:
        remaining_elements.sort()
        # Get biggest element
        element = remaining_elements.pop()
        _LOGGER.debug(f"Evaluating element of size {element}")
        # Find first light that can partially satisfy what the element needs
        found_light: int | None = None
        for light in lights:
            if light <= element:
                found_light = light
                break
        if not found_light:
            raise ValueError(f"Could not satisfy element of remaining size {element}")

        _LOGGER.debug(f"Using inventory light {found_light}")
        # Mark this light in the desired inventory and reduce the amount of
        # elements needed from the inventory
        result[found_light] = result.get(found_light, 0) + 1
        element -= found_light
        if element > 0:
            # The element isn't "complete" yet so put it back in the list
            remaining_elements.append(element)
    return result


