from __future__ import annotations

import pygame
from pygame.locals import *

__all__ = []


# some string conversion functions (since looking up strings in a dict is pretty fast performance-wise)
def point_str(point):
    return str(point[0]) + ';' + str(point[1])


def line_str(line, point):
    return point_str(line[point]) + ';' + str(line[2][0]) + ';' + str(line[2][1])


def str_point(string):
    return [int(v) for v in string.split(';')[:2]]


# accepts a list of "air" tiles and adds walls to the designated light box
def generate_walls(light_box, map_data, tile_size):
    # looking up a string in a dict is significantly quicker than looking up in a list
    map_dict = {}
    lines = []

    # generate a dict with all of the tiles
    for tile in map_data:
        map_dict[str(tile[0]) + ';' + str(tile[1])] = 1

    # add all the walls by checking air tiles for bordering solid tiles (solid tiles are where there are no tiles in
    # the dict)
    for air_tile in map_data:
        # check all sides for each air tile
        if point_str([air_tile[0] + 1, air_tile[1]]) not in map_dict:
            # generate line in [p1, p2, [vertical, inside/outside]] format
            lines.append([[air_tile[0] * tile_size + tile_size, air_tile[1] * tile_size],
                             [air_tile[0] * tile_size + tile_size, air_tile[1] * tile_size + tile_size], [0, -1]])
        if point_str([air_tile[0] - 1, air_tile[1]]) not in map_dict:
            lines.append([[air_tile[0] * tile_size, air_tile[1] * tile_size],
                             [air_tile[0] * tile_size, air_tile[1] * tile_size + tile_size], [0, 1]])
        if point_str([air_tile[0], air_tile[1] + 1]) not in map_dict:
            lines.append([[air_tile[0] * tile_size, air_tile[1] * tile_size + tile_size],
                             [air_tile[0] * tile_size + tile_size, air_tile[1] * tile_size + tile_size], [1, -1]])
        if point_str([air_tile[0], air_tile[1] - 1]) not in map_dict:
            lines.append([[air_tile[0] * tile_size, air_tile[1] * tile_size],
                             [air_tile[0] * tile_size + tile_size, air_tile[1] * tile_size], [1, 1]])

    # reformat the data into a useful form for the geometry tricks later
    # this adds each endpoint to a dict as a key with the associated endpoint being in the list of associated values
    # (so 1 point can link to 2 bordering points where lines are connected)
    # it keys with respect to the vertical/horizontal aspect and the inward/outward aspect, so all lines that use the
    # same keys are part of a single joined line
    line_dict = {}
    for line in lines:
        for i in range(2):
            if line_str(line, i) in line_dict:
                line_dict[line_str(line, i)].append(line_str(line, 1 - i))
            else:
                line_dict[line_str(line, i)] = [line_str(line, 1 - i)]

    final_walls = []
    # keep track of the processed points so that those keys can be ignored (we add 4 points per line since each point
    # must be a key once and a value once)
    processed_points = []
    for point in line_dict:
        # the length of the items in this dict are the number of connected points
        # so if there's only 1 connected point, that means it's the end of a line
        # we can then follow the line's points to calculate the single line based off the connections
        if point not in processed_points:
            # look for the end of the line and skip all the others (since anything else must be connected to an end
            # due to the respect to direction)
            if len(line_dict[point]) == 1:
                # add this point to the list to ignore
                processed_points.append(point)
                offset = 1
                p1 = str_point(point)
                p2 = str_point(line_dict[point][0])
                # calculate the direction based on the 2 points
                direction = [(p2[0] - p1[0]) // tile_size, (p2[1] - p1[1]) // tile_size]
                # loop through the connected points until the other end is found
                while 1:
                    # generate the string for the next point
                    target_pos = str(p1[0] + direction[0] * offset * tile_size) + ';' + str(
                        p1[1] + direction[1] * offset * tile_size) + ';' + point.split(';')[2] + ';' + point.split(';')[
                                     3]
                    # when the connected point only links to 1 point, you've found the other end of the line
                    processed_points.append(target_pos)
                    if len(line_dict[target_pos]) == 1:
                        break
                    offset += 1
                # append to the walls list based on the last point found and the starting point
                final_walls.append([p1, str_point(target_pos), int(point.split(';')[2]), int(point.split(';')[3])])

    # generate Wall objects
    final_walls = [Wall(*wall) for wall in final_walls]
    # apply walls
    light_box.add_walls(final_walls)

    # return the list just in case it's needed for something
    return final_walls


# the class for lights
# just stores some attributes and an image
class Light:
    def __init__(self, pos, radius, light_img):
        self.position = pos
        self.radius = radius
        self.light_img = pygame.transform.scale(light_img, (radius * 2, radius * 2))


# the core class that handles/contains everything
# the name "LightBox" comes from the idea that the lighting is only rendered within the "box" of the display (or
# whatever use you may have)
class LightBox:
    def __init__(self, size):
        """
        Size is the dimensions of the area that light is processed in
        """
        self.vision_box_r = pygame.Rect(0, 0, size[0], size[1])
        self.walls = []
        self.lights = {}

        # keeps track of IDs for lights so that each new light has a different ID
        self.light_id = 0

    # a function for adding walls
    def add_walls(self, walls):
        self.walls += walls

    # deletes all walls
    def clear_walls(self):
        self.walls = []

    # create a new light with a light object (returns the associated ID for later use)
    def add_light(self, light):
        self.light_id += 1
        self.lights[str(self.light_id)] = light
        return str(self.light_id)

    # get a light object based on ID so you can modify the position
    def get_light(self, light_id):
        return self.lights[light_id]

    # delete a light based on the ID
    def del_light(self, light_id):
        del self.lights[light_id]

    # a useful internal function (used to determine max range for calculations)
    def get_max_light_radius(self):
        max_radius = 0
        for light in self.lights:
            max_radius = max(max_radius, self.lights[light].radius)

        return max_radius

    # the core rendering function that renders onto a target surface with a specified terrain offset (aka scroll)
    def render(self, target_surf, offset=[0, 0]):
        # get the max light radius to determine which lights need to be rendered
        # if a light center is farther away from the viewing range than its radius, it's off the screen
        # if the light's modifications don't reach onto the screen, then its shadows won't have an effect,
        # so it's not necessary to process
        max_radius = self.get_max_light_radius()

        # define an updated render_box rect with respect to the terrain offset and the light range to determine which
        # walls needs to be processed
        render_box_r = pygame.Rect(-max_radius + offset[0], -max_radius + offset[1],
                                   self.vision_box_r.width + max_radius * 2, self.vision_box_r.height + max_radius * 2)

        # generate list of walls that are visible and adjust for offset to get the "shown position"
        valid_walls = [wall.clone_move([-offset[0], -offset[1]]) for wall in self.walls if
            wall.rect.colliderect(render_box_r)]

        # redefine the render_box rect with the terrain offset removed since the walls have been moved
        render_box_r = pygame.Rect(-max_radius, -max_radius, self.vision_box_r.width + max_radius * 2,
                                   self.vision_box_r.height + max_radius * 2)

        # generate a Surface to render the lighting mask onto
        rendered_mask = pygame.Surface(self.vision_box_r.size)

        # iterate through all of the lights
        for light in self.lights:
            light = self.lights[light]
            # apply the terrain offset
            light_pos = [light.position[0] - offset[0], light.position[1] - offset[1]]
            # check for visibility (don't forget that the current rect is adjusted for the radii of the lights)
            if render_box_r.collidepoint(light_pos):
                # create surface to render the shadow polygons and the lighting image onto
                light_instance_surf = pygame.Surface(rendered_mask.get_size())
                # apply lighting image
                light_instance_surf.blit(light.light_img, (light_pos[0] - light.radius, light_pos[1] - light.radius))
                # draw over the light image with the shadows of each wall (the draw_shadow function only draws if
                # applicable, so a polygon isn't drawn every time)
                for wall in valid_walls:
                    wall.draw_shadow(light_instance_surf, light_pos, render_box_r, (0, 0, 0))

                # blit lighting mask onto main surface with RGBA_ADD so that the lighting can accumulate
                rendered_mask.blit(light_instance_surf, (0, 0), special_flags=BLEND_RGBA_ADD)

        # blit the final lighting mask onto the target surface
        target_surf.blit(rendered_mask, (0, 0), special_flags=BLEND_RGBA_ADD)

        # return the list of visible walls in case they need to be used for anything
        return valid_walls


# the wall class that makes up the core of the lighting system (since the walls cast shadows)
class Wall():
    def __init__(self, p1, p2, vertical, direction, color=(255, 255, 255)):
        self.p1 = p1
        self.p2 = p2
        # vertical is whether or not the face of the wall points vertically (in other words, the wall's line is
        # horizontal)
        self.vertical = vertical
        # direction is determined by the direction the wall faces with respect to the standard coordinate system (
        # left and up are negative while down and right are positive)
        self.direction = direction
        self.color = color
        # generate the rect for light_box collisions
        self.update_rect()

    # a function used to create a duplicate with an offset (used during rendering by the light box)
    def clone_move(self, offset):
        return Wall([self.p1[0] + offset[0], self.p1[1] + offset[1]], [self.p2[0] + offset[0], self.p2[1] + offset[1]],
                    self.vertical, self.direction, self.color)

    # generate a rect based on the points in the wall
    def update_rect(self):
        r_p1 = [min(self.p1[0], self.p2[0]), min(self.p1[1], self.p2[1])]
        r_p2 = [max(self.p1[0], self.p2[0]), max(self.p1[1], self.p2[1])]
        # +1 in the x_size and y_size because straight walls have a width or height of 0
        self.rect = pygame.Rect(r_p1[0], r_p1[1], r_p2[0] - r_p1[0] + 1, r_p2[1] - r_p1[1] + 1)

    def check_cast(self, source, vision_box):
        # the line below is useful if the colliding walls aren't precalculated
        # if vision_box.collidepoint(self.p1) or vision_box.collidepoint(self.p2):

        # will return 1 (or True) if the direction/position of the wall logically allows a shadow to be cast
        if (source[self.vertical] - self.p1[self.vertical]) * self.direction < 0:
            return 1
        else:
            return 0

    # determine the point on the vision_box's edge that is collinear to the light and the endpoint of the wall (this
    # must be called for each endpoint of the wall)
    def determine_cast_endpoint(self, source, point, vision_box):
        difx = source[0] - point[0]
        dify = source[1] - point[1]
        try:
            slope = dify / difx
        # questionable, but looks alright
        except ZeroDivisionError:
            slope = 999999
        if slope == 0:
            slope = 0.000001

        # since the vision_box's edges are being treated as lines, there are technically 2 collinear points on the
        # vision box's edge
        # one must be a horizontal side and the other must be vertical since the 2 points must be on adjacent sides

        # determine which horizontal and which vertical sides of the vision box are used (top/bottom and left/right)
        cast_hside = 0
        cast_vside = 0
        if difx < 0:
            cast_hside = 1
        if dify < 0:
            cast_vside = 1

        # calculate the collinear points with quick mafs
        if cast_hside:
            hwall_p = [vision_box.right, slope * (vision_box.right - source[0]) + source[1]]
        else:
            hwall_p = [vision_box.left, slope * (vision_box.left - source[0]) + source[1]]
        if cast_vside:
            vwall_p = [(vision_box.bottom - source[1]) / slope + source[0], vision_box.bottom]
        else:
            vwall_p = [(vision_box.top - source[1]) / slope + source[0], vision_box.top]

        # calculate closer point out of the 2 collinear points and return side used
        if (abs(hwall_p[0] - source[0]) + abs(hwall_p[1] - source[1])) < (
                abs(vwall_p[0] - source[0]) + abs(vwall_p[1] - source[1])):
            # horizontal sides use numbers 2 and 3
            return hwall_p, cast_hside + 2
        else:
            # vertical sides use numbers 0 and 1
            return vwall_p, cast_vside

    # a function for getting the corner points for the polygon
    # if the casted shadow points for walls are on different vision_box sides, the corners between the points must be
    # added
    def get_intermediate_points(self, p1_side, p2_side, vision_box):
        # the "sides" refer to the sides of the vision_box that the wall endpoints casted onto
        # 0 = top, 1 = bottom, 2 = left, 3 = right
        sides = [p1_side, p2_side]
        sides.sort()
        # return the appropriate sides based on the 2 sides
        # the first 4 are the cases where the 2 shadow points are on adjacent sides
        if sides == [0, 3]:
            return [vision_box.topright]
        elif sides == [1, 3]:
            return [vision_box.bottomright]
        elif sides == [1, 2]:
            return [vision_box.bottomleft]
        elif sides == [0, 2]:
            return [vision_box.topleft]
        # these 2 are for when the shadow points are on opposite sides (normally happens when the light source is
        # close to the wall)
        # the intermediate points depend on the direction the shadow was cast in this case (they could be on either
        # side without knowing the direction)
        elif sides == [0, 1]:
            if self.direction == -1:
                return [vision_box.topleft, vision_box.bottomleft]
            else:
                return [vision_box.topright, vision_box.bottomright]
        elif sides == [2, 3]:
            if self.direction == -1:
                return [vision_box.topleft, vision_box.topright]
            else:
                return [vision_box.bottomleft, vision_box.bottomright]
        # this happens if the sides are the same, which would mean the shadow doesn't cross sides and has no
        # intermediate points
        else:
            return []

    # the master shadow casting function
    def draw_shadow(self, surf, source, vision_box, color):
        # check if a shadow needs to be casted
        if self.check_cast(source, vision_box):
            # create the list of points for drawing the polygon
            # start with the 2 endpoints of the wall
            shadow_points = [self.p1, self.p2]

            # calculate the endpoints of the shadow when casted on the edge of the vision_box
            p1_shadow, p1_side = self.determine_cast_endpoint(source, self.p1, vision_box)
            p2_shadow, p2_side = self.determine_cast_endpoint(source, self.p2, vision_box)

            # calculate the intermediate points of the shadow (see the function for a more detailed description)
            intermediate_points = self.get_intermediate_points(p1_side, p2_side, vision_box)

            # arange the points of the polygon
            points = [self.p1] + [p1_shadow] + intermediate_points + [p2_shadow] + [self.p2]

            # draw the polygon
            pygame.draw.polygon(surf, color, points)

    # a render function just used for rendering the line that makes up the wall
    # mostly just useful for debug
    def render(self, surf, offset=[0, 0]):
        pygame.draw.line(surf, self.color, self.p1, self.p2)


# just a function for generating boxes
# might be useful for custom wall generation
def box(pos, size):
    walls = []
    walls.append(Wall([pos[0], pos[1]], [pos[0] + size[0], pos[1]], 1, -1))
    walls.append(Wall([pos[0], pos[1]], [pos[0], pos[1] + size[1]], 0, -1))
    walls.append(Wall([pos[0] + size[0], pos[1]], [pos[0] + size[0], pos[1] + size[1]], 0, 1))
    walls.append(Wall([pos[0], pos[1] + size[1]], [pos[0] + size[0], pos[1] + size[1]], 1, 1))
    return walls
