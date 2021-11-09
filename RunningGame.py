from re import T
from ursina import *
from ursina import texture
import random
class Camera(Entity):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            position = position,
            visible = False)
        
class Sphere(Entity):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            position = position,
            model = 'sphere',
            color = color.cyan,
            scale = (0.8))
                
            
class Ground(Entity):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            position = position,
            model = 'cube',
            color = color.lime,
            scale = (1,0.5,1),
            texture = 'white_cube')

class Obstacle(Entity):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            position = position,
            model = 'cube',
            color = color.white,
            scale = (1,2,1),
            texture = 'white_cube')
    
def update():
    if held_keys['a']:
        player.x -= 3*time.dt
    if held_keys['d']:
        player.x += 3*time.dt
    
    if player.z <= 195:
        player.z += 10*time.dt
        vision.z += 10*time.dt
    
    camera.position = (vision.x,vision.y+1,vision.z)
    

app = Ursina()
window.fps_counter.enabled = False
vision = Camera(position=(2,2,-25))

player = Sphere(position= (2,0,0))


    

for i in range (20):
        randmx = random.randint(0,4)
        rndmz = random.randint(0,20)
        obstacle = Obstacle(position=(randmx, 0, rndmz*10))

for x in range (5):
        for z in range (200):
            ground = Ground(position=(x,-1,z))
        

app.run()

