class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self, side=0):
        self._side = side
        
    def get_side(self):
        """Return the side of the Cube"""
        if self._side < 0:
            self._side = self._side * (-1)
        else:
            self._side = self._side
            
        return self._side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = new_side
        
    side = property(get_side, set_side)   