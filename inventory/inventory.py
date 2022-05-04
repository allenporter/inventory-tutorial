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

    for element in elements:
        _LOGGER.debug(f"Evaluating element of size {element}")
        found = {}
        remaining = element
        while remaining > 0:
            # Find first light that can partially satisfy what the element needs
            found_light = next(( light for light in lights if light <= remaining ), None)
            if not found_light:
                raise ValueError(f"Could not satisfy remaining {remaining} of elmennet {element}")
            _LOGGER.debug(f"Using inventory light {found_light}")
            # Mark this light in the desired inventory and reduce the amount of
            # elements needed from the inventory
            found[found_light] = found.get(found_light, 0) + 1
            remaining -= found_light
        _LOGGER.debug(f"Used lights {found} to build element {element}")
        for k, v in found.items():
            result[k] = result.get(k, 0) + v
    return result


