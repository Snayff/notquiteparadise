from __future__ import annotations

import dataclasses
import logging
from typing import TYPE_CHECKING, Dict, List, Tuple

import pygame

from scripts.engine.core.constants import (
    ASSET_PATH,
    ICON_SIZE,
    IMAGE_NOT_FOUND_PATH,
    TILE_SIZE,
    DirectionType,
    Shape,
    ShapeType,
)
from scripts.engine.core.definitions import TraitSpritePathsData, TraitSpritesData

if TYPE_CHECKING:
    from typing import Any, Dict, List, Optional, Tuple, Type, Union

__all__ = [
    "get_image",
    "get_images",
    "flatten_images",
    "recursive_replace",
    "recursive_find_in_dict",
    "get_class_members",
    "lerp",
    "clamp",
    "get_coords_from_shape",
    "is_close",
    "value_to_member",
    "convert_tile_string_to_xy",
    "convert_direction_to_name",
    "build_sprites_from_paths",
]


################################### IMAGES ########################################


def get_image(
    img_path: str, desired_dimensions: Tuple[int, int] = (TILE_SIZE, TILE_SIZE), copy: bool = False
) -> pygame.Surface:
    """
    Get the specified image and resize if dimensions provided. Dimensions are in (width, height) format. If img
    path is "none" then a blank surface is created to the size of the desired dimensions, or TILE_SIZE if no
    dimensions provided.
    """
    from scripts.engine.core.data import store  # circular import in testing.

    # check if image path provided
    if img_path.lower() != "none":

        if f"{img_path}{desired_dimensions}" in store.images:
            image = store.images[f"{img_path}{desired_dimensions}"]
        else:
            try:
                # try and get the image provided
                image = pygame.image.load(str(ASSET_PATH / img_path)).convert_alpha()

            except:
                image = pygame.image.load(str(IMAGE_NOT_FOUND_PATH)).convert_alpha()
                logging.warning(
                    f"Get_image: Tried to use {img_path} but it wasn`t found. Used the not_found image instead."
                )
    else:
        image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        image.set_alpha(0)

    # resize if needed - should only need to resize if we havent got it from storage
    if image.get_width() != desired_dimensions[0] or image.get_height() != desired_dimensions[1]:
        width, height = desired_dimensions
        image = pygame.transform.smoothscale(image, (width, height))

        # add to storage
        store.images[f"{img_path}{desired_dimensions}"] = image

    # return a copy if requested
    if copy:
        return image.copy()
    else:
        return image


def get_images(
    img_paths: List[str], desired_dimensions: Tuple[int, int] = (TILE_SIZE, TILE_SIZE), copy: bool = False
) -> List[pygame.Surface]:
    """
    Get a collection of images.
    """
    images = []

    for path in img_paths:
        images.append(get_image(path, desired_dimensions, copy))

    return images


def flatten_images(images: List[pygame.Surface]) -> pygame.Surface:
    """
    Flatten a list of images into a single image. All images must be the same size. Images are blitted in order.
    """

    biggest_image: Optional[pygame.Surface] = None
    biggest_image_index = -1
    for i in range(len(images)):
        img = images[i]
        if (biggest_image is None) or (
            img.get_width() > biggest_image.get_width() and img.get_height() > biggest_image.get_height()
        ):
            biggest_image = img
            biggest_image_index = i

    base: pygame.Surface = biggest_image
    for image in images[0:biggest_image_index] + images[biggest_image_index:]:
        if image != biggest_image:
            base.blit(image, (0, 0))

    return base


def build_sprites_from_paths(
    sprite_paths: List[TraitSpritePathsData], desired_size: Tuple[int, int] = (TILE_SIZE, TILE_SIZE)
) -> TraitSpritesData:
    """
    Build a TraitSpritesData class from a list of TraitSpritePathsData. For each member in TraitSpritePathsData,
    combines the sprites from each TraitSpritePathsData in the  list and flattens to a single surface.
    """
    paths: Dict[str, List[str]] = {}
    sprites: Dict[str, List[pygame.Surface]] = {}
    flattened_sprites: Dict[str, pygame.Surface] = {}

    # bundle into cross-trait sprite path lists
    for sprite_path in sprite_paths:
        char_dict = dataclasses.asdict(sprite_path)
        for name, path in char_dict.items():
            if name != "render_order":
                # check if key exists
                if name in paths:
                    paths[name].append(path)
                # if not init the dict
                else:
                    paths[name] = [path]

    # convert to sprites
    for name, path_list in paths.items():
        # override size for icon
        if name == "path":
            desired_size = (ICON_SIZE, ICON_SIZE)

        sprites[name] = get_images(path_list, desired_size, True)  # make sure to get copies

    # flatten the images
    for name, surface_list in sprites.items():
        flattened_sprites[name] = flatten_images(surface_list)

    # convert to dataclass
    converted = TraitSpritesData(**flattened_sprites)
    return converted


################################### QUERY TOOLS ########################################


def recursive_replace(obj: Union[Dict, List], key: str, value_to_replace: Any, new_value: Any):
    """
    Check through any number of nested dicts or lists for the specified key->value pair and replace the value.
    """
    if isinstance(obj, dict):
        # Break the dict out and run recursively against the elements
        for k, v in obj.items():
            if k == key:
                # The value may be a list so handle it if so
                if isinstance(v, list):
                    # Loop the list and replace the required value
                    for index, item in enumerate(v):
                        if item == value_to_replace:
                            v[index] = new_value
                elif v == value_to_replace:
                    obj[key] = new_value
            else:
                recursive_replace(v, key, value_to_replace, new_value)

    elif isinstance(obj, list):
        # Break the list out and run recursively against the elements
        for element in obj:
            recursive_replace(element, key, value_to_replace, new_value)


def recursive_find_in_dict(obj: Union[Dict, List], key: str) -> Any:
    """
    Check through any number of nested dicts for the specified key and return the value. Returns after
    finding the first key.
    """
    if isinstance(obj, dict):
        # Break the dict out and run recursively against the elements
        for k, v in obj.items():
            if k == key:
                return v
            else:
                # go a layer down
                recursive_find_in_dict(v, key)


def get_class_members(cls: Type[Any]) -> List[str]:
    """
    Get a class' members, excluding special methods e.g. anything prefixed with '__'. Useful for use with dataclasses.
    """
    members = []

    for member in cls.__dict__.keys():
        if member[:2] != "__":
            members.append(member)

    return members


################################### MATHS ########################################


def lerp(initial_value: float, target_value: float, lerp_fraction: float) -> float:
    """
    Linear interpolation between initial and target by amount. Fraction clamped between 0 and 1.
    """
    clamped_lerp_fraction = clamp(lerp_fraction, 0, 1)

    if clamped_lerp_fraction >= 0.99:
        return target_value
    else:
        return initial_value * (1 - clamped_lerp_fraction) + target_value * clamped_lerp_fraction


def clamp(value, min_value, max_value):
    """
    Return the value, clamped between min and max.
    """
    return max(min_value, min(value, max_value))


def is_close(current_pos: Tuple[float, float], target_pos: Tuple[float, float], delta=0.05) -> bool:
    """
    returns true if the absolute distance between both coordinates is less than delta
    """
    return abs(current_pos[0] - target_pos[0]) <= delta and abs(current_pos[1] - target_pos[1]) <= delta


################################### SHAPES  ########################################


def get_coords_from_shape(shape: ShapeType, size: int, direction: Optional[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Get a list of coordinates from a shape, size and direction.
    """
    if shape == Shape.TARGET:
        return [(0, 0)]  # single target, centred on selection

    elif shape == Shape.SQUARE:
        return _calculate_square_shape(size)

    elif shape == Shape.CIRCLE:
        return _calculate_circle_shape(size)

    elif shape == Shape.CROSS:
        return _calculate_cross_shape(size)

    elif shape == Shape.CONE:
        if direction:
            return _calculate_cone_shape(size, direction)
        else:
            logging.error(f"No direction passed to get_coords_from_shape for a Cone.")
            raise KeyError("No direction for Cone.")

    logging.error(f"Unknown shape '{shape}' passed to get_coords_from_shape")
    raise KeyError(f"Unknown shape '{shape}'")


def _calculate_square_shape(size: int) -> List[Tuple[int, int]]:
    """
    Calculate all the tiles in the range of a square
    """
    coord_list = []
    width = size
    height = size

    for x in range(-width, width + 1):
        for y in range(-height, height + 1):
            coord_list.append((x, y))
    return coord_list


def _calculate_circle_shape(size: int) -> List[Tuple[int, int]]:
    """
    Calculate all the tiles in the range of a circle
    """
    coord_list = []
    radius = (size + size + 1) / 2

    for x in range(-size, size + 1):
        for y in range(-size, size + 1):
            if x * x + y * y < radius * radius:
                coord_list.append((x, y))

    return coord_list


def _calculate_cross_shape(size: int) -> List[Tuple[int, int]]:
    """
    Calculate all the tiles in the range of a cross
    """
    coord_list = [(0, 0)]
    x_coords = [-1, 1]

    for x in x_coords:
        for y in range(-size, size + 1):

            # ignore 0's to ensure no duplication when running through the range
            # the multiplication of x by y means they are always both 0 if y is
            if y != 0:
                coord_list.append((x * y, y))

    return coord_list


def _calculate_cone_shape(size: int, direction: Tuple[int, int]) -> List[Tuple[int, int]]:
    # we need a direction since cones are not symmetric
    coord_list = []
    last_row = [(0, 0)]
    # each size means 1 expansion of the cone
    for iteration in range(size):
        # use a set so we don't add the same coord multiple times
        new_row = set()
        for coord in last_row:
            new_coord = (coord[0] + direction[0], coord[1] + direction[1])
            new_row.add(new_coord)
            # calculate the perpendiculars in both directions
            perpendiculars = [(direction[1], direction[0]), (-direction[1], -direction[0])]
            for perpendicular_direction in perpendiculars:
                perpendicular = (new_coord[0] + perpendicular_direction[0], new_coord[1] + perpendicular_direction[1])
                new_row.add(perpendicular)

        coord_list += list(last_row)
        # FIXME - Incompatible types in assignment (expression has type "Set[Tuple[int, int]]", variable has type
        #  "List[Tuple[int, int]]")
        last_row = new_row  # type: ignore
    return coord_list + list(last_row)


################################### CONVERSIONS ########################################


def value_to_member(value: Any, cls: Type[Any]) -> str:
    """
    Get a member of a class that matches the value given
    """
    members = get_class_members(cls)

    for member in members:
        if getattr(cls, member) == value:
            return member

    return "No member with value found."


def convert_tile_string_to_xy(tile_pos_string: str) -> Tuple[int, int]:
    """
    Convert a tile position string to (x, y)
    """
    _x, _y = tile_pos_string.split(",")
    x = int(_x)  # str to int
    y = int(_y)
    return x, y


def convert_direction_to_name(direction: DirectionType) -> str:
    """
    Get the direction name from the direction. (0,1) = 'up' etc.
    """
    directions = {
        (0, 1): "up",
        (0, -1): "down",
        (1, 0): "right",
        (-1, 0): "left",
        (1, 1): "up_right",
        (-1, 1): "up_left",
        (1, -1): "down_right",
        (-1, -1): "down_left",
    }

    try:
        direction_name = directions[direction]
    except KeyError:
        direction_name = "centre"

    return direction_name
