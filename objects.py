import pygame
from components.entity import Entity
from components.sprite import Sprite
from components.player import Player
from components.physics import Body
from components.teleporter import Teleporter
from components.spritegifs import SpriteAnimated

entity_factories = [

    lambda args: Entity(Player(), Sprite("DJIcon.png"), Body(0, 0, 31, 31)),

    lambda args: Entity(Sprite("playerflipped.png", has_rotation=True), Body(0, 0, 100, 139)),

    lambda args: Entity(Sprite("wd_gaster.png"), Body(0, 0, 38, 96)),

    lambda args: Entity(Teleporter(args[3], args[4], args[5]), Sprite("celiannatilea5/C5-000016.png")),

    lambda args: Entity(SpriteAnimated("beavis.gif"), Body(0, 0, 242, 498)),

]

def create_entity(id, x, y, data=None):
    factory = entity_factories[id]
    e = factory(data)
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