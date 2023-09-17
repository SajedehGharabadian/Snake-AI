import tensorflow as tf
import arcade
from arcade.sprite_list.spatial_hash import check_for_collision
from snake import Snake
from apple import Apple
from tensorflow import keras
from keras.models import load_model
import numpy as np
from function_generate_dataset import generate_data

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 560




class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title="Snake Game")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.wall = 20
        self.apple = Apple(SCREEN_WIDTH,SCREEN_HEIGHT,self.wall)
        self.start_x = 0
        self.start_y = 10
        self.model = load_model('model/weight_snake.h5')

    def on_draw(self):
        arcade.start_render()
        
        self.snake.draw()
        self.apple.draw()
        arcade.draw_text('Score:' + str(self.snake.score),self.start_x,self.start_y,arcade.color.BLACK,15)

        if  self.snake.center_x < self.wall or self.snake.center_x > SCREEN_WIDTH-self.wall or self.snake.center_y < self.wall or self.snake.center_y > SCREEN_HEIGHT-self.wall:
            arcade.draw_text('GAME OVER',SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2,arcade.color.BLACK,25)
            arcade.exit()


        
    def on_update(self, delta_time: float):

        a_center_x,a_center_y,snake_center_x,snake_center_y,a_up,a_right,a_down,a_left,b_up,b_right,b_down,b_left = generate_data(SCREEN_WIDTH,SCREEN_HEIGHT,self.snake,self.apple,self.wall)        

        data = np.array([[a_center_x,a_center_y,snake_center_x,snake_center_y,a_up,a_right,a_down,a_left,b_up,b_right,b_down,b_left]])
        
        output = self.model.predict(data)

        direction = np.argmax(output)

        print (direction)
        
        
        if direction == 0 and self.snake.change_y != -1:
            self.snake.change_x = 0 
            self.snake.change_y = 1
            
        elif direction == 1 and self.snake.change_x != -1:
            self.snake.change_x = 1
            self.snake.change_y = 0
            

        elif direction == 2 and self.snake.change_y != 1:
            self.snake.change_x = 0
            self.snake.change_y = -1
            
        elif direction == 3 and self.snake.change_x != 1:
            self.snake.change_x = -1
            self.snake.change_y = 0


        self.snake.on_update(delta_time)
        self.apple.on_update()
        self.snake.move()
        
        if check_for_collision(self.snake,self.apple):
            self.snake.eat()
            self.snake.move()
            self.apple = Apple(SCREEN_WIDTH,SCREEN_HEIGHT,self.wall)

        

    def on_key_release(self, key: int, modifiers: int):
        pass


if __name__ == "__main__":
    game = Game()
    game.run()
 
