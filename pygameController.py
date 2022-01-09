import pygame
import move
import time

def initialiseJoysticks():
    """Initialise all joysticks, returning a list of pygame.joystick.Joystick"""
    joysticks = []              # for returning

    # Initialise the Joystick sub-module
    pygame.joystick.init()
    screen = pygame.display.set_mode([240, 160])

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range( joystick_count ):
        joystick = pygame.joystick.Joystick( i )
        joystick.init()
        # NOTE: Some examples discard joysticks where the button-count
        #       is zero.  Maybe this is a common problem. 
        joysticks.append( joystick )

    # TODO: Print all the statistics about the joysticks
    if ( len( joysticks ) == 0 ):
        print( "No joysticks found" )
    else:
        for i,joystk in enumerate( joysticks ):
            print("Joystick %d is named [%s]" % ( i, joystk.get_name() ) )
            # etc.

    return joysticks

all_joysticks = initialiseJoysticks()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            print(event.axis)

        elif event.type == pygame.JOYBUTTONDOWN:
            print( "Joystick button pressed." )
            pass
        elif event.type == pygame.JOYBUTTONUP:
            print( 'joystick: %d, button: %d' % ( event.joy, event.button ) )