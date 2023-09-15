import arcade
import random

class Snake(arcade.Sprite):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__()

        self.width = 7
        self.height = 14
        self.color = arcade.color.DARK_MAGENTA
        self.color1 = arcade.color.PALE_GOLD
        self.color2 = arcade.color.BLUE
        self.change_x = -1
        self.change_y = 0
        self.score = 0
        self.center_x = SCREEN_WIDTH//2        
        self.center_y = SCREEN_HEIGHT//2
        self.speed = 7
        self.body = []

    def move(self):

        self.body.append({'x': self.center_x , 'y': self.center_y })

        if len(self.body) > self.score:
            self.body.pop(0)

        self.center_x = self.center_x + self.change_x * self.speed
        self.center_y = self.center_y+ self.change_y * self.speed

    def eat(self):
       self.score += 1
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.height,self.color)
        
        for index, item in enumerate(self.body):
            if index % 2 == 0:
                arcade.draw_circle_filled(item['x'],item['y'],self.width,self.color2)
            else:
                arcade.draw_circle_filled(item['x'],item['y'],self.width,self.color1)

        