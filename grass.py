from pico2d import load_image


class Grass:
    def __init__(self,x,y):
        self.image = load_image('grass.png')
        self.x, self.y = x, y

    def draw(self):
        #self.image.draw(400, 30)
        self.image.draw(self.x, self.y)

    def update(self):
        pass
