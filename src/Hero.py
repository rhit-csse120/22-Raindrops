class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """
        Creates a Hero sprite (Mike/Alyssa) that does not move.
        If hit by rain they'll put up their umbrella.
        """
        # TODO 17: Initialize this Hero, as follows:
        #   - Store the screen.
        #   - Set the initial position of this Hero to x and y.
        #   - Create an image of this Hero WITH an umbrella
        #       from the given   with_umbrella_filename.
        #   - Create an image of this Hero WITHOUT an umbrella
        #       from the given   without_umbrella_filename.
        #   - Initialize the image to the image WITH an umbrella.
        #   - Set the "last hit time" to 0.
        #  Use instance variables:
        #    screen  x  y  image_umbrella  image_no_umbrella  image  last_hit_time.

    def draw(self):
        """Draws this sprite onto the screen."""
        # TODO 22:
        #    If the current time is greater than this Hero's
        #    last_hit_time + 1, set self.image to the image of this Hero
        #    WITHOUT an umbrella; otherwise set self.image to the image
        #    of this Hero WITH an umbrella.

        # TODO 18: Draw (blit) this Hero, at this Hero's position,
        #   using the current image.

    def check_hit_by(self, raindrop):
        """
        If the given raindrop is hitting this Hero, sets this Hero's
        last_hit_time  to the current time and returns True.
        Otherwise, returns False.
        """
        # TODO 20: If this Hero is currently colliding
        #  with the given Raindrop, set this Hero's  last_hit_time
        #  to the current time and return True; else return False.
