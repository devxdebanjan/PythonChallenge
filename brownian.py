import pygame
import numpy as np
import random

# Constants
WIDTH, HEIGHT = 600, 600
BACKGROUND_COLOR = (30, 30, 30)
ROBOT_COLOR = (0, 255, 0)
ROBOT_RADIUS = 10
SPEED = 2

class Robot:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.angle = random.uniform(0, 2 * np.pi)
        self.vx = SPEED * np.cos(self.angle)
        self.vy = SPEED * np.sin(self.angle)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.check_collision()
    
    def check_collision(self):
        if self.x - ROBOT_RADIUS <= 0: 
            self.angle = random.uniform(-np.pi / 2, np.pi / 2)  
        elif self.x + ROBOT_RADIUS >= WIDTH: 
            self.angle = random.uniform(np.pi / 2, 3 * np.pi / 2)  

        if self.y - ROBOT_RADIUS <= 0:
            self.angle = random.uniform(0, np.pi)  
        elif self.y + ROBOT_RADIUS >= HEIGHT: 
            self.angle = random.uniform(np.pi, 2 * np.pi) 

        self.vx = SPEED * np.cos(self.angle)
        self.vy = SPEED * np.sin(self.angle)
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brownian Motion Simulation")
    clock = pygame.time.Clock()
    robot = Robot()
    
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        robot.move()
        pygame.draw.circle(screen, ROBOT_COLOR, (int(robot.x), int(robot.y)), ROBOT_RADIUS)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
