class entity(object):
    def __init__(self, position, size):
        self.position = position
        self.size = size

    #return x pos of entity on window
    @property
    def get_x(self):
        return self.position[0]
    
    #return y pos of entity on window
    @property
    def get_y(self):
        return self.position[1]
    
    #return width of entity
    @property
    def get_width(self):
        return self.size[0]

    #return height of entity
    @property
    def get_height(self):
        return self.size[1]
    
    def set_x(self, x):
        self.position[0] = x

    def set_y(self, y):
        self.position[1] = y