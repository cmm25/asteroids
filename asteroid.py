import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_SPEED

class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius:float)-> None:
        super().__init__(x, y, radius)
    def draw(self,screen: pygame.Surface)->None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt:float):
        unit_vector= pygame.Vector2(0,1)
        line_vector_speed = unit_vector.rotate(ASTEROID_SPEED*dt)
        self.position +=(self.velocity*dt)

