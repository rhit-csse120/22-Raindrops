import pygame
import sys
import time  # Note this!
import random  # Note this!
from Raindrop import Raindrop
from Hero import Hero
from Cloud import Cloud


def main():
    """
    Main game loop that creates the sprite objects,
    controls interactions, and draws the screen.
    """
    # DONE 2: Initialize the game, display a caption,
    #  and set   screen   to a 1000 x 600 Screen.
    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000, 600))

    # DONE 3: Make a Clock.
    clock = pygame.time.Clock()

    # DONE 8: As a temporary test, make a new Raindrop
    #  called   test_drop   at x=320 y=10.
    # test_drop = Raindrop(screen, 320, 10)
    # test_drop.speed = 2

    # DONE 9: See the Raindrop class for this TODO.
    # DONE 10: See the Raindrop class for this TODO.

    # DONE 16: Make a Hero, named mike, with appropriate images,
    #    starting at position x=200 y=400.
    #  Also make a Hero, named alyssa, with appropriate images,
    #    starting at position x=700 y=400.
    mike = Hero(screen,200, 400,
                "../media/mike_umbrella.png",
                "../media/mike.png")
    alyssa = Hero(screen, 700, 400,
                  "../media/alyssa_umbrella.png",
                  "../media/alyssa.png")

    # DONE 17: See the Hero class for this TODO.
    # DONE 18: See the Hero class for this TODO.

    # DONE 23: Make a Cloud, named cloud, with an appropriate image file,
    #  starting at position x=300 y=50.
    cloud = Cloud(screen, 300, 50, "../media/cloud.png")

    # DONE 24: See the Cloud class for this TODO.
    # DONE 25: See the Cloud class for this TODO.

    # DONE 4: Enter the game loop, with a clock tick of 60 (or so)
    #  at each iteration.  Indent (tab) all the remaining steps.
    while True:
        clock.tick(60)

        # DONE 5:   Make the pygame.QUIT event stop the game.
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

        # DONE 27: Inside the game loop (AFTER the events loop above),
        #  get the list of keys that are currently pressed.
        #  Then arrange so that the Cloud moves:
        #    - 5 pixels (or 10 pixels) to the right
        #        if the Right Arrow key (pygame.K_RIGHT) is pressed.
        #    - 5 pixels (or 10 pixels) to the left
        #        if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        #    - 5 pixels (or 10 pixels) up
        #        if the Up    Arrow key (pygame.K_UP)    is pressed.
        #    - 5 pixels (or 10 pixels) down
        #        if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        #  DISCUSS: If you want something to happen once per key press,
        #  put it in the events loop above.  If you want something
        #  to continually happen while holding the key,
        #  put it after the events loop.
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x = cloud.x + 5
        if pressed_keys[pygame.K_LEFT]:
            cloud.x = cloud.x - 5
        if pressed_keys[pygame.K_UP]:
            cloud.y = cloud.y - 5
        if pressed_keys[pygame.K_DOWN]:
            cloud.y = cloud.y + 5

        # DONE 28: See the Cloud class for this TODO.

        # DONE 6: Inside the game loop, draw the screen (fill with white).
        screen.fill("white")

        # DONE 13: As a temporary test, move  test_drop.
        #    Note: When you test (i.e., run) this step,
        #    slow the rain down to a speed of 2 to see the result,
        #    then remove that code after doing the testing.
        # test_drop.move()

        # DONE 14: See the Raindrop class for this TODO.

        # DONE 15: As a temporary test, check if test_drop is off screen;
        #  if so reset its y position to 10.
        # if test_drop.off_screen():
        #     test_drop.y = 10

        # DONE 11: As a temporary test, draw  test_drop.
        # test_drop.draw()

        # DONE 12: See the Raindrop class for this TODO.

        # DONE 21: As a temporary test, check if  test_drop  is hitting
        #  Mike or Alyssa; if so set their  last_hit_time.  Print the result.
        #    Note: When you test (i.e., run) this and the next step,
        #    slow the rain down to a speed of 2 to see the result,
        #    then remove that code after doing the testing.
        # print(mike.check_hit_by(test_drop))
        # print(alyssa.check_hit_by(test_drop))

        # DONE 22: See the Hero class for this TODO.

        # DONE 26: Draw the Cloud.
        cloud.draw()

        # DONE 29: Comment-out the temporary  test_drop  code
        #  from this function and refactor it as follows:
        #    - Make the Cloud "rain", then:
        #    - For each Raindrop in the Cloud's list of raindrops:
        #       - move the Raindrop.
        #       - draw the Raindrop.
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            mike.check_hit_by(raindrop)
            alyssa.check_hit_by(raindrop)

        # DONE 30: check if the Hero (Mike or Alyssa) is hit by a raindrop,
        #  and if so, set the Hero's last_time_hit to the current time.
        #      Optional  - if the Raindrop is off the screen or hitting
        #      a Hero, remove it from the Cloud's list of raindrops.
        for k in range(len(cloud.raindrops) - 1, -1, -1):
            raindrop = cloud.raindrops[k]
            if raindrop.off_screen() \
                or mike.check_hit_by(raindrop) \
                or alyssa.check_hit_by(raindrop):
                del cloud.raindrops[k]
        print(len(cloud.raindrops))
        # FIXME: The above calls   check_hit_by  TWICE per frame.  Ugh.

        # DONE 19: Draw the Heroes (Mike and Alyssa).
        mike.draw()
        alyssa.draw()

        # DONE 20: See the Hero class for this TODO.

        # DONE 7: Update the display.
        pygame.display.update()


# DONE 1: Call main.
main()