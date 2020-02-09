from dot import Dot


class Dots:
    """A collection of dots."""

    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 50
        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [Dot(self.SPACING * i, self.TH)
                        for i in range(self.WIDTH//self.SPACING + 1)]
        self.bottom_row = [Dot(self.SPACING * i, self.BH)
                           for i in range(self.WIDTH//self.SPACING + 1)]
        self.left_col = [Dot(self.LV, self.SPACING * i)
                         for i in range(self.HEIGHT//self.SPACING + 1)]
        self.right_col = [Dot(self.RV, self.SPACING * i)
                          for i in range(self.HEIGHT//self.SPACING + 1)]

    def display(self):
        """Calls each dot's display method"""
        for i in range(0, len(self.top_row)):
            self.top_row[i].display()
        for i in range(0, len(self.bottom_row)):
            self.bottom_row[i].display()
        for i in range(0, len(self.left_col)):
            self.left_col[i].display()
        for i in range(0, len(self.right_col)):
            self.right_col[i].display()

    # TODO:
    # PROBLEM 3: implement dot eating
    # BEGIN CODE CHANGES
    # You might want/need to pass arguments here.
    def eat(self, pacman_x, pacman_y):
        if(abs(pacman_x - self.LV) <= self.EAT_DIST):
            for i in range(0, len(self.left_col)):
                if(abs(self.left_col[i].y - pacman_y) <= self.EAT_DIST):
                    if(i == len(self.left_col)-1):
                        self.left_col = self.left_col[:i]
                    else:
                        self.left_col = self.left_col[:i]+self.left_col[i+1:]
                    break

        elif(abs(pacman_x - self.RV) <= self.EAT_DIST):
            for i in range(0, len(self.right_col)):
                if(abs(self.right_col[i].y - pacman_y) <= self.EAT_DIST):
                    if(i == len(self.right_col)-1):
                        self.right_col = self.right_col[:i]
                    else:
                        self.right_col = self.right_col[:i] + \
                            self.right_col[i+1:]
                    break

        if(abs(pacman_y - self.TH) <= self.EAT_DIST):
            for i in range(0, len(self.top_row)):
                if(abs(self.top_row[i].x-pacman_x) <= self.EAT_DIST):
                    if(i == len(self.top_row)-1):
                        self.top_row = self.top_row[:i]
                    else:
                        self.top_row = self.top_row[:i]+self.top_row[i+1:]
                    break

        elif(abs(pacman_y-self.BH) <= self.EAT_DIST):
            for i in range(0, len(self.bottom_row)):
                if(abs(self.bottom_row[i].x-pacman_x) <= self.EAT_DIST):
                    if(i == len(self.bottom_row)):
                        self.bottom_row = self.bottom_row[:i]
                    else:
                        self.bottom_row = self.bottom_row[:i] + \
                            self.bottom_row[i+1:]
                    break

    # END CODE CHANGES

    def dots_left(self):
        """Returns the number of remaing dots in the collection"""
        return (len(self.top_row) +
                len(self.bottom_row) +
                len(self.left_col) +
                len(self.right_col))
