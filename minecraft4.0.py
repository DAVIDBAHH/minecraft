from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from numpy import floor
from random import randrange
app = Ursina()
sky = load_texture("images/sky.png")
music = Audio("music\Danny.mp3")
inventory = [load_texture("images/grass.jpg"),
            load_texture("images/stone.png"),
            load_texture("images/brick.png"),
            load_texture("images/gold_block.png"),
            load_texture("images/Diamond_block.png"),
            load_texture("images/leaves.png"),
            load_texture("images/glass.png"),
            load_texture("images/wood.png"),
            load_texture("images\dirt.jpg"),
            load_texture("images\quartz.png"),
            load_texture("images\water.png"),
            load_texture("images\lava.png"),
            load_texture("images/stone_brick.png"),
            load_texture("images\cobblestone.png"),
            load_texture("images/plank1.jpg"),
            ]
texture = 0
music.loop = True   
music.play()
window.position = 0,0
window.collider_counter.enabled = False
window.entity_counter.enabled = False
window.fps_counter.enabled = False
window.fullscreen = True
window.set_title("Minecraft")
current_texture = inventory[texture]
def active():
    mini_block.rotation = (90,-10,0)
    mini_block.position=(0.30,-0.20,0.5)
def pasive():
    mini_block.rotation=(-15,-30,-5)
    mini_block.position=(0.35,-0.25,0.5)
def click():
    if held_keys['left mouse']:
        cursor.color = color.white
        active()
    elif held_keys['right mouse']:
        active()
    else:
        cursor.color = color.white
        pasive()
def key():
    if held_keys['r']:
        player.position = (0, 0, 0)
    elif held_keys["q"]:
        quit()
def input(key):
    global current_texture,texture
    if key == 'c':
        if texture == len(inventory) - 1:
            texture = 0     
        else:
            texture += 1
    if key == 'v':
        if texture == 0:
            texture = len(inventory)-1    
        else:
            texture -= 1
    current_texture = inventory[texture]
def update():
    key()
    click()
    mini_block.texture=current_texture
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=inventory[0]):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, 255),
            highlight_color=color.hex("#e0e0e0"))

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position=self.position + mouse.normal, texture=current_texture)

            if key == 'left mouse down':
                destroy(self)
Sky(texture=sky)
seed = randrange(1,10000000000000000000000000)
noise = PerlinNoise(octaves=2, seed=seed)
freq = 24
amp = 5
terrain_width = 20
for i in range(terrain_width * terrain_width):
    block = Voxel(position=(floor(i / terrain_width), 0, floor(i % terrain_width)))
    block.y = floor(noise([block.x / freq, block.z / freq]) * amp)
    block.parent = scene
mini_block = Entity(parent=camera,model="cube",scale=0.2,texture=current_texture,position=(0.35,-0.25,0.5),rotation=(-15,-30,-5))
player = FirstPersonController(origin_y=.5,speed = 5,origin_x=6)
cursor = player.cursor
app.run()