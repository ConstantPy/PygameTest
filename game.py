import pygame
import input
from player import Player
from sprite import sprites, Sprite
from map import TileKind, Map
from camera import create_screen
from entity import Entity, active_objs

pygame.init()

screen = create_screen(1280, 920, "DJ's Quest")
running = True
clock = pygame.time.Clock()
fps = 60

player = Entity(Player(), Sprite("images/player.png"), x = screen.get_width()/2, y = screen.get_height()/2)

### Print statements of me trying figure out how to reference Sprite("images/player.png") dimensions-
### -to get true image center in the player = entity(x = screen.get_width()/2, y = screen.get_height()/2)
### I assume I have to do and reference something in player.py (or even in entity.py) to achieve this and call it before the player = Entity()
print(player.get(Sprite).image)
print(player.get(Sprite).image.get_width())
print(player.get(Sprite).image.get_height())
# player_sprite = player.get(Sprite).image
# player_sprite_width, player_sprite_height = player_sprite.get_size()
# print(f"Width: {player_sprite_width}, Height: {player_sprite_height}")
print(Player.sprite_dimensions)
print(player.components[0])

# Assigns a tile sprite to it number in a list, this gets completely changed in the tutorial later on
tile_kinds = [
    TileKind("transparent", "images/celiannatilea5/C5-00002.png", False),
    TileKind("playerhousefloor", "images/celiannatilea5/C5-0000040.png", False)
]


tile_kinds_layer = [
    TileKind("transparent", "images/celiannatilea5/C5-00002.png", False),
    TileKind("upmidleft", "images/celiannaclutterwalls2/CCW2-000002.png", False),
    TileKind("upmidright", "images/celiannaclutterwalls2/CCW2-000003.png", False),
    TileKind("dwnmidleft", "images/celiannaclutterwalls2/CCW2-00000014.png", False),
    TileKind("dwnmidright", "images/celiannaclutterwalls2/CCW2-00000015.png", False),
]

# Map class that calls a .map file represented in numbers, assigns the layer, then tile sprite size, as mentioned, this is changed in the tutorial
map = Map("maps/start.map", tile_kinds, 32)
map_layer = Map("maps/start_layer_1.map", tile_kinds_layer, 16)

# For a future collision test
flipped_player = Entity(Sprite("images/playerflipped.png"), x = 32 * 18,y = 32 * 18)

# Game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)
            
    # Update Code
    for a in active_objs:
        a.update()

    # Draw Code
    screen.fill("black")
    map.draw(screen)
    map_layer.draw(screen)
    for s in sprites:
        s.draw(screen)
    
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()




