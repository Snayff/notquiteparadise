from typing import List, Tuple, Union

import pygame
import pytest  # type: ignore

from scripts.engine.core import utility
from scripts.engine.internal.constant import IMAGE_NOT_FOUND_PATH, Shape, ShapeType, TILE_SIZE

test_get_image_returns_image_parameters = [
    (TILE_SIZE, TILE_SIZE),  # normal
    (-TILE_SIZE, -TILE_SIZE),  # negative
    (TILE_SIZE * 10, TILE_SIZE * 10),  # large
    (TILE_SIZE, TILE_SIZE * 2),  # not square
]


@pytest.mark.parametrize("desired_dimensions", test_get_image_returns_image_parameters)
def test_get_image_returns_image(benchmark, desired_dimensions: Tuple[int, int]):
    img_path = str(IMAGE_NOT_FOUND_PATH)
    image = benchmark(utility.get_image, img_path, desired_dimensions)
    assert isinstance(image, pygame.Surface)


def test_get_image_returns_copy():
    img_path = str(IMAGE_NOT_FOUND_PATH)
    image = utility.get_image(img_path, (TILE_SIZE, TILE_SIZE))
    copy_image = utility.get_image(img_path, (TILE_SIZE, TILE_SIZE), True)
    assert image is not copy_image


def test_get_images_returns_images():
    img_paths = [str(IMAGE_NOT_FOUND_PATH), str(IMAGE_NOT_FOUND_PATH), str(IMAGE_NOT_FOUND_PATH)]
    images = utility.get_images(img_paths, (TILE_SIZE, TILE_SIZE))

    assert isinstance(images, list)
    assert len(images) == 3


def test_flatten_images(benchmark):
    img_paths = [str(IMAGE_NOT_FOUND_PATH), str(IMAGE_NOT_FOUND_PATH), str(IMAGE_NOT_FOUND_PATH)]
    images = utility.get_images(img_paths)
    image = benchmark(utility.flatten_images, images)

    assert isinstance(image, pygame.Surface)


def test_build_sprites_from_paths(benchmark):
    from scripts.engine.internal.definition import TraitSpritePathsData
    trait_paths = TraitSpritePathsData(
        icon=str(IMAGE_NOT_FOUND_PATH),
        idle=str(IMAGE_NOT_FOUND_PATH),
        attack=str(IMAGE_NOT_FOUND_PATH),
        hit=str(IMAGE_NOT_FOUND_PATH),
        dead=str(IMAGE_NOT_FOUND_PATH),
        move=str(IMAGE_NOT_FOUND_PATH),
    )
    trait_paths2 = TraitSpritePathsData(
        icon=str(IMAGE_NOT_FOUND_PATH),
        idle=str(IMAGE_NOT_FOUND_PATH),
        attack=str(IMAGE_NOT_FOUND_PATH),
        hit=str(IMAGE_NOT_FOUND_PATH),
        dead=str(IMAGE_NOT_FOUND_PATH),
        move=str(IMAGE_NOT_FOUND_PATH),
    )

    _trait_paths = [trait_paths, trait_paths2]

    # this func uses get_images which has already tested diff sizes
    trait_sprites = benchmark(utility.build_sprites_from_paths, _trait_paths, (TILE_SIZE, TILE_SIZE))

    from scripts.engine.internal.definition import TraitSpritesData
    assert isinstance(trait_sprites, TraitSpritesData)


test_clamp_parameters = [
    (1, 0, 10),  # positive int
    (-1, -10, 0),  # negative int
    (1.0, 0.0, 10.0),  # positive float
    (-1.0, -10.0, 0.0),  # negative float
]


@pytest.mark.parametrize("value, min_value, max_value", test_clamp_parameters)
def test_clamp(value: Union[int, float], min_value: Union[int, float], max_value: Union[int, float]):
    result = utility.clamp(value, min_value, max_value)

    assert result <= max_value
    assert result >= min_value


test_is_close_parameters = [
    ((1, 1), (1.025, 1.025), 0.05),  # positive int, default delta
    ((-1, -1), (-1.025, -1.025), 0.05),  # negative int, default delta
    ((2.0, 2.0), (2.025, 2.025), 0.05),  # positive float, default delta
    ((-2.0, -2.0), (-2.025, -2.025), 0.05),  # negative float, default delta
    ((1.0, 1.0), (4.0, 4.0), 8.0)
]


@pytest.mark.parametrize("current_pos, target_pos, delta", test_is_close_parameters)
def test_is_close(current_pos: Tuple[float, float], target_pos: Tuple[float, float], delta: float):
    result = utility.is_close(current_pos, target_pos, delta)

    assert result


test_is_not_close_parameters = [
    ((1, 1), (2, 2), 0.05),  # positive int, default delta
    ((-1, -1), (-2, -2), 0.05),  # negative int, default delta
    ((1.0, 1.0), (2.0, 2.0), 0.05),  # positive float, default delta
    ((-1.0, -1.0), (-2.0, -2.0), 0.05),  # negative float, default delta
    ((1.0, 1.0), (10.0, 10.0), 8.0)
]


@pytest.mark.parametrize("current_pos, target_pos, delta", test_is_not_close_parameters)
def test_is_not_close(current_pos: Tuple[float, float], target_pos: Tuple[float, float], delta: float):
    result = utility.is_close(current_pos, target_pos, delta)

    assert not result


test_get_coordinates_from_shape_parameters = [
    (Shape.SQUARE, 1, (0, 0), [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]),
    (Shape.CIRCLE, 1, (0, 0), [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]),
    (Shape.CROSS, 1, (0, 0), [(0, 0), (1, -1), (-1, 1), (-1, -1), (1, 1)]),
    (Shape.TARGET, 1, (0, 0), [(0, 0)]),
    (Shape.CONE, 1, (0, 1), [(0, 0), (1, 1), (0, 1), (-1, 1)]),
    (Shape.CONE, 1, (0, -1), [(0, 0), (1, -1), (0, -1), (-1, -1)]),
    (Shape.CONE, 1, (1, 0), [(0, 0), (1, -1), (1, 1), (1, 0)]),
    (Shape.CONE, 1, (-1, 0), [(0, 0), (-1, 1), (-1, 0), (-1, -1)]),
]


@pytest.mark.parametrize("shape, size, direction, expected", test_get_coordinates_from_shape_parameters)
def test_get_coordinates_from_shape(benchmark, shape: ShapeType, size: int, direction: Tuple[int, int],
        expected: List[Tuple[int, int]]):
    coordinates = benchmark(utility.get_coords_from_shape, shape, size, direction)
    assert set(coordinates) == set(expected)
