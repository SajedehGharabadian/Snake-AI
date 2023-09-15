import arcade
import random


class Apple(arcade.Sprite):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT,wall_width):
        super().__init__()
        self.width = 14
        self.height = 14
        self.r = 14
        self.color = arcade.color.RED
        
        self.center_x  = random.randint(wall_width, SCREEN_WIDTH-wall_width) //7 * 7
        self.center_y = random.randint(wall_width, SCREEN_HEIGHT-wall_width) //7 * 7

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)  
