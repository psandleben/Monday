import arcade

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCALE: float = 0.5
SCREEN_TITLE: str = "snake"
MOVEMENT_SPEED: int = 16
STARTING_DIRECTION: str = "south"

SNAKEBODYEND_PATH = "Snake2/snake_body_end.png"
SNAKEBODY_PATH = "Snake2/snake_body.png"
SNAKEHEAD_PATH = "Snake2/snake_head.png"

"""----------------------------------------------------------------"""

class SnakeBody(arcade.Sprite):
    def __init__(self, filename: str, bodybefore, scale: float = 1.0, center_x: int = 0, center_y: int = 0):
        super().__init__(filename, scale) 
        self.bodybefore = bodybefore
        self.center_x = center_x
        self.center_y = center_y
    
    def move(self):
        self.center_x = self.bodybefore.get_center_x()
        self.center_y = self.bodybefore.get_center_y()

    def get_center_x(self):
        return self.center_x
    def get_center_y(self):
        return self.center_y
    
"""----------------------------------------------------------------"""

class SnakeHead(arcade.Sprite):
    def __init__(self, filename: str, scale: float = 1.0, direction: str = "south"): 
        super().__init__(filename, scale) 
        self.direction = direction

    def move(self):
            if self.direction == "south":
                self.center_y += MOVEMENT_SPEED #runter bewegen
            elif self.direction == "north":
                self.center_y -= MOVEMENT_SPEED #hoch bewegen
            elif self.direction == "west":
                self.center_x -= MOVEMENT_SPEED #links bewegen
            elif self.direction == "east":
                self.center_x += MOVEMENT_SPEED #rechts bewegen
    
    def set_direction_left(self):
        if self.direction == "south":
            self.direction = "west"
        elif self.direction == "west":
            self.direction = "north"
        elif self.direction == "north":
            self.direction = "east"
        elif self.direction == "east":
            self.direction = "south"

    def set_direction_right(self):
        if self.direction == "south":
            self.direction = "east"
        elif self.direction == "east":
            self.direction = "north"
        elif self.direction == "north":
            self.direction = "west"
        elif self.direction == "west":
            self.direction = "south"
        
    def get_center_x(self):
        return self.center_x
    def get_center_y(self):
        return self.center_y

"""----------------------------------------------------------------"""

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.snake_list = None

        self.time = None
        self.total_time = None
        self.esc_timer = None
        self.snake_list_length = None
        self.last_snake_list_body = None

    def setup(self):
        self.time = 0
        self.total_time = 0
        self.esc_timer = -1
        self.snake_list_length = 3

        self.snake_list = arcade.SpriteList()
        self.snakehead = SnakeHead(SNAKEHEAD_PATH, SCALE, STARTING_DIRECTION)
        self.snakehead.center_x = SCREEN_WIDTH / 2
        self.snakehead.center_y = SCREEN_HEIGHT / 2
        self.snake_list.append(self.snakehead)
        
        snakebody_1 = SnakeBody(SNAKEBODY_PATH, self.snakehead, SCALE)
        snakebody_1.center_x = SCREEN_WIDTH / 2 
        snakebody_1.center_y = SCREEN_HEIGHT / 2 - 16*1
        self.snake_list.append(snakebody_1)

        snakebody_2 = SnakeBody(SNAKEBODY_PATH, snakebody_1, SCALE)
        snakebody_2.center_x = SCREEN_WIDTH / 2
        snakebody_2.center_y = SCREEN_HEIGHT / 2 - 16*2
        self.snake_list.append(snakebody_2)
        self.last_snake_list_body = snakebody_2
        
        
    def on_draw(self):
        self.clear()
        self.snake_list.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        self.snake_list.update()
        self.time += delta_time
        self.total_time += delta_time
        
        if self.time >= 0.5: 
            i = self.snake_list_length -1
            while i >= 0:
                self.snake_list[i].move()
                i -= 1
            
            self.time = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ESCAPE:
            self.esc_timer = self.total_time
        if key == arcade.key.LEFT:
            self.snakehead.set_direction_left()
        if key == arcade.key.RIGHT:
            self.snakehead.set_direction_right()
        if key == arcade.key.A:
            snakebody = SnakeBody(SNAKEBODY_PATH, self.last_snake_list_body, SCALE)
        snakebody.center_x = self.last_snake_list_body.get_center_x()
        snakebody.center_y = self.last_snake_list_body.get_center_y()
        self.snake_list.append(snakebody)
        self.last_snake_list_body = snakebody
        self.snake_list_length += 1
            

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.ESCAPE:
            if self.total_time >= 1 + self.esc_timer:
                self.esc_timer = -1
            else:
                arcade.close_window()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


Snake = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
Snake.setup()
arcade.run()