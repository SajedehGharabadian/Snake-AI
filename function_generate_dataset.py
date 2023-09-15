import numpy as np


def generate_data(SCREEN_WIDTH,SCREEN_HEIGHT,snake,apple,wall_width):

    b_up = 0
    b_right = 0
    b_down = 0
    b_left = 0 
    a_up = 0
    a_right = 0
    a_down = 0
    a_left = 0

    # w_up = snake.center_y   
    # w_right = SCREEN_WIDTH - snake.center_x
    # w_down = SCREEN_HEIGHT - snake.center_y
    # w_left = snake.center_x  
    a_center_x = apple.center_x
    a_center_y = apple.center_y
    snake_center_x = snake.center_x
    snake_center_y = snake.center_y


    

    if snake.center_x == apple.center_x and snake.center_y < apple.center_y:
        distance_x = snake.center_x - apple.center_x 
        distance_y = snake.center_y - apple.center_y
        a_up = np.linalg.norm(distance_x-distance_y)
       
    else:
        a_up = 0

    if snake.center_x == apple.center_x and snake.center_y > apple.center_y:
        distance_x = snake.center_x - apple.center_x 
        distance_y = snake.center_y - apple.center_y
        a_down = np.linalg.norm(distance_x-distance_y) #np.sqrt(np.sum((distance_x - distance_y)**2))
        
    else:
        a_down = 0

    if snake.center_x > apple.center_x and snake.center_y == apple.center_y:
        distance_x = snake.center_x - apple.center_x 
        distance_y = snake.center_y - apple.center_y
        a_left = np.linalg.norm(distance_x-distance_y)  #np.sqrt(np.sum((distance_x - distance_y)**2))
       

    else:
        a_left = 0

    if snake.center_x < apple.center_x and snake.center_y == apple.center_y:
        distance_x = snake.center_x - apple.center_x 
        distance_y = snake.center_y - apple.center_y
        a_right = np.linalg.norm(distance_x-distance_y) #np.sqrt(np.sum((distance_x - distance_y)**2))
        
    else:
        a_right = 0


    for part in snake.body:
        distance_part_x = snake.center_x - part['x'] 
        distance_part_y = snake.center_y - part['y']
        if snake.center_x == part['x'] and snake.center_y > part['y']:
            b_down = np.linalg.norm(distance_part_x - distance_part_y)
            

        else:
            b_down = 0
            
    for part in snake.body:
        distance_part_x = snake.center_x - part['x'] 
        distance_part_y = snake.center_y - part['y']
        if snake.center_x == part['x'] and snake.center_y < part['y']:
            b_up = np.linalg.norm(distance_part_x - distance_part_y) #np.sqrt(np.sum((distance_part_x - distance_part_y)**2))
            
        else:
            b_up = 0

        for part in snake.body:
            distance_part_x = snake.center_x - part['x'] 
            distance_part_y = snake.center_y - part['y']
           
            if snake.center_x > part['x'] and snake.center_y ==  part['y']:
                b_left = np.linalg.norm(distance_part_x - distance_part_y) #np.sqrt(np.sum((distance_part_x - distance_part_y)**2))
               
            else:
                b_left = 0

        for part in snake.body:
            distance_part_x = snake.center_x - part['x'] 
            distance_part_y = snake.center_y - part['y']
            if snake.center_x < part['x'] and snake.center_y ==  part['y']:
                b_right = np.linalg.norm(distance_part_x - distance_part_y) #np.sqrt(np.sum((distance_part_x - distance_part_y)**2))

            else:
                b_right = 0



    return np.array([a_center_x,a_center_y,snake_center_x,snake_center_y,
                     a_up,a_right,a_down,a_left,b_up,b_right,b_down,b_left]
                    ,dtype=np.float32)


