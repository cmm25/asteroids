import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius:float)-> None:
        super().__init__(x, y, radius)
    def draw(self,screen: pygame.Surface)->None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt:float):
        self.position +=(self.velocity*dt)
    def split(self):
        self.kill() #kill main one
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
        
            """
                the main idea is after killing the main big one,
                create a random number to determine rotation axis of children
                noting velocity = vector direction * time
                then
                calculate the new smaller radii
                then 2 asteroid instances with x, y of original parent as origin and new radii
            """
            log_event("asteroid_split")
            random_number = random.uniform(20, 50)
            first_aster_direction_vector = self.velocity.rotate(random_number)
            second_aster_direction_vector = self.velocity.rotate(-random_number)
            new_radius_small_first_second = self.radius -ASTEROID_MIN_RADIUS
            first_aster_velocity = first_aster_direction_vector *1.2
            second_aster_velocity = second_aster_direction_vector *1.2
            first_asteroid = Asteroid(self.position.x,self.position.y, new_radius_small_first_second)
            first_asteroid.velocity = first_aster_velocity
            second_asteroid = Asteroid(self.position.x,self.position.y, new_radius_small_first_second)
            second_asteroid.velocity = second_aster_velocity
                        




