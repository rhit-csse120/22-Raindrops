class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around."""
        # TODO 24: Initialize this Cloud, as follows:
        #   - Store the screen.
        #   - Set the initial position of this Cloud to x and y.
        #   - Set the image of this Cloud to the given image filename.
        #   - Create a list for Raindrop objects as an empty list.
        #   - Use instance variables:
        #        screen   x  y   image   raindrops.
        pass

    def draw(self):
        """Draws this sprite onto the screen."""
        # TODO 25: Draw (blit) this Cloud's image at its current position.
        pass

    def rain(self):
        """Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining."""
        # TODO 28: Append a new Raindrop to this Cloud's list of raindrops,
        #   where the new Raindrop starts at:
        #     - x is a random integer between this Cloud's x
        #         and this Cloud's x + 300.
        #     - y is this Cloud's y + 100.
        pass
