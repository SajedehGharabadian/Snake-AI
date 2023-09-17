import arcade
import pandas as pd
from arcade.sprite_list.spatial_hash import check_for_collision
from snake import Snake
from apple import Apple
from function_generate_dataset import generate_data 
import numpy as np


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
        self.Data = []
        self.Direction = []
        

    def on_draw(self):
        arcade.start_render()
        
        self.snake.draw()
        self.apple.draw()
        arcade.draw_text('Score:' + str(self.snake.score),self.start_x,self.start_y,arcade.color.BLACK,15)


        
    def on_update(self, delta_time: float):
        self.snake.move()
        data = generate_data(SCREEN_WIDTH,SCREEN_HEIGHT,self.snake,self.apple,40)
        
        
        if check_for_collision(self.snake,self.apple):
            self.snake.eat()
            self.snake.move()
            self.apple = Apple(SCREEN_WIDTH,SCREEN_HEIGHT,self.wall)


        if self.snake.center_x > self.apple.center_x:
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.Direction.append(3)
        
        elif self.snake.center_x < self.apple.center_x:
            self.snake.change_x = 1
            self.snake.change_y = 0
            self.Direction.append(1)


        elif self.snake.center_y < self.apple.center_y:
            self.snake.change_x = 0
            self.snake.change_y = 1
            self.Direction.append(0)

        elif self.snake.center_y > self.apple.center_y:
            self.snake.change_x = 0
            self.snake.change_y = -1
            self.Direction.append(2)

        self.Data.append(data)
        
        self.snake.on_update()
        self.apple.on_update()

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.Q:
            columns_names =['a_center_x','a_center_y','snake_center_x','snake_center_y'
                            ,'a_up','a_right','a_down','a_left',
                            'b_up','b_right','b_down','b_left']
            dataframe = pd.DataFrame(self.Data,columns=columns_names)

            column_name_label = ['direction']
            labels = pd.DataFrame(self.Direction,columns=column_name_label)

            dataframe.to_csv('Dataset/Dataset.csv',index=False)
            labels.to_csv('Dataset/Labels.csv',index=False)

            arcade.finish_render()
            exit(0)


if __name__ == "__main__":
    game = Game()
    game.run()
 
