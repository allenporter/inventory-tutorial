#!/usr/bin/python3

import pytest
from inventory.inventory import compute_inventory

def test_compute_inventory():
    elements = [327, 120]
    lights = [100, 20, 7]

    assert compute_inventory(elements, lights) == {100: 4, 20: 2, 7: 1}
