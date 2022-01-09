from os import POSIX_FADV_NOREUSE
import pygame
import move
import turn
import time

screen = pygame.display.set_mode([240, 160])
move.setup()
moving = False
while 1:
    for event in pygame.event.get():
        
        forward = pygame.key.get_pressed()[pygame.K_q]
        backward = pygame.key.get_pressed()[pygame.K_a]
        left = pygame.key.get_pressed()[pygame.K_o]
        right = pygame.key.get_pressed()[pygame.K_p]

        if forward:
            print('FORWARD')
            move.setup()
            speed_set = 100
            move.move(speed_set, 'forward', 'no', 0.8)
            moving = True

        if backward:
            print('BACKWARD')
            move.setup()
            speed_set = 100
            move.move(speed_set, 'backward', 'no', 0.8)
            moving = True

        if moving and (not forward) and (not backward):
            print('STOP')
            move.motorStop()
            move.destroy()
            moving = False

        if left:
            turn.turn_left()
            print('left')

        if right:
            turn.turn_right()
            print('right')

        if not left and not right:
            turn.straight()
            print('straight')

        time.sleep(0.01)
