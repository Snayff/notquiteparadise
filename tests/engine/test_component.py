from typing import List, Tuple

import pytest  # type: ignore

from scripts.engine.core.component import Position

class TestPosition:
    test_position_outmost_parameters = [
        [[(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (0, -1)], (1, 0), (1, 0)],
        [[(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (0, -1)], (-1, 0), (-1, 0)],
        [[(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (0, -1)], (0, -1), (0, -1)],
        [[(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (0, -1)], (0, 1), (0, 1)],
    ]

    def test_position_detect_top_left(self):
        """
        Test the Position component
        """
        pos = Position((6, 6), (6, 5), (5, 5), (5, 6))
        assert pos.x == 5 and pos.y == 5

    def test_position_coordinates(self):
        """
        Test the Position coordinates
        """
        coordinates = [(6, 6), (6, 5), (5, 5), (5, 6)]
        pos = Position(*coordinates)
        assert set(coordinates) == set(pos.coordinates)

    def test_position_centers(self):
        """
        Test the Position centers correctly
        """
        pos = Position((5, 5), (6, 5), (6, 6), (5, 6))
        assert set(pos.offsets) == {(0, 0), (1, 0), (1, 1), (0, 1)}

    @pytest.mark.parametrize("coordinates, direction, expected", test_position_outmost_parameters)
    def test_position_outmost(self, coordinates: List[Tuple[int, int]], direction: Tuple[int, int], expected: Tuple[int, int]):
        """
        Test the Position outmost function
        """
        pos = Position(*coordinates)
        assert pos.get_outermost(direction) == expected
