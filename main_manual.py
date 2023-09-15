import arcade
from arcade.sprite_list.spatial_hash import check_for_collision
from snake import Snake
from apple import Apple
from function_generate_dataset import generate_data 
import pandas as pd


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title="Snake Game")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.wall = 80
        #self.snake.body.append(self.snake)
        self.apple = Apple(SCREEN_WIDTH,SCREEN_HEIGHT,self.wall)
        self.start_x = 0
        self.start_y = 10
       

    def on_draw(self):
        arcade.start_render()
        
        self.snake.draw()
        self.apple.draw()
        arcade.draw_text('Score:' + str(self.snake.score),self.start_x,self.start_y,arcade.color.BLACK,15)


        
    def on_update(self, delta_time: float):
        self.snake.move()
        if check_for_collision(self.snake,self.apple):
            self.snake.eat()
            self.snake.move()
            self.apple = Apple(SCREEN_WIDTH,SCREEN_HEIGHT,self.wall)

        

    def on_key_release(self, key: int, modifiers: int):
        
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
            
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif key == arcade.key.UP:
            self.snake.change_x = 0   #jologiri az harekat movarab mar
            self.snake.change_y = 1

        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1




if __name__ == "__main__":
    game = Game()
    game.run()
 