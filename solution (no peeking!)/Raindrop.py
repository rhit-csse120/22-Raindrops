import random
import pygame


class Raindrop:
    def __init__(self, screen, x, y):
        """
        Creates a Raindrop sprite that travels down at a random speed.
        """
        # DONE 9: Initialize this Raindrop, as follows:
        #   - Store the screen.
        #   - Set the initial position of the Raindrop to x and y.
        #   - Set the initial speed to a random integer between 5 and 15.
        #  Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)

    def move(self):
        """
        Move the  self.y  value of the Raindrop down the screen
        (y increases) at the  self.speed.
        """
        # DONE 12: Change the  y  position of this Raindrop by its speed.
        self.y = self.y + self.speed

    def off_screen(self):
        """
        Returns True if the Raindrop y value is not shown on the screen;
        otherwise returns False.
        """
        # Note: this method will be used for testing but not used
        # in the final version of the code, for the sake of simplicity.
        # DONE 14: Return  True  if the  y  position of this Raindrop
        #  is greater than the screen's height.
        return self.y > self.screen.get_height()

    def draw(self):
        """Draws this sprite onto the screen."""
        # DONE 10: Draw a vertical line that is 5 pixels long and
        #  2 pixels thick, from the current position of this Raindrop
        #  (use either a black or blue color).
        pygame.draw.line(self.screen,
                         (0, 0, 255),
                         (self.x, self.y),
                         (self.x, self.y + 5),
                         2)

