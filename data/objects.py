import pygame    # Currently not being utilized
from components.entity import Entity
from components.sprite import Sprite
from components.player import Player
from components.physics import Body
from components.teleporter import Teleporter
from components.spritegifs import SpriteAnimated

# Some notes, entity(Player()) is bound to the tile size of 32x32, going any higher results in collision irregularites, been trying to figure out how to be able to go beyond 32 x 32
# Update the Body() to match the corresponding image size and width (last two of the four)
entity_factories = [

    lambda args: Entity(Player(), Sprite("player image goes here"), Body(0, 0, 0, 0)),

    lambda args: Entity(Sprite("image file goes here", Body(0, 0, 0, 0)),

    lambda args: Entity(Sprite("image file goes here"), Body(0, 0, 0, 0)),

    lambda args: Entity(Teleporter(args[3], args[4], args[5]), Sprite("image file for teleporter goes here")),

    lambda args: Entity(SpriteAnimated("gif file goes here"), Body(0, 0, 242, 498)),

]

def create_entity(id, x, y, data=None):
    factory = entity_factories[id]
    e = factory(data)
    # The if statements here align the objects to be given a somewhat "true center" instead of following pythons center being top left 0,0
    if id == 0:
        e.x = (x * 32) - int(100/2)
        e.y = (y * 32)
    elif id == 2:
        e.x = (x * 32) - int(38/2)
        e.y = (y * 32)
    elif id == 3:
        e.x = (x * 32) - int(32/2)
        e.y = (y * 32)
    else:
        e.x = x * 32
        e.y = y * 32

    return e

