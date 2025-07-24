class Moveable:
    def move(self, current_position: dict[str, float], dx:float, dy:float)->None:
        """
        Move the current position by dx and dy.

        :param current_position: The current position of the object.
        :param dx: The change in x position.
        :param dy: The change in y position.
        """
        current_position['x'] += dx
        current_position['y'] += dy
