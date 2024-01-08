import arcade

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
SCALE: float = 1.0
SCREEN_TITLE: str = "snake"
MOVEMENT_SPEED: int = 16
STARTING_DIRECTION: str = "south"

SNAKEBODY_PATH = "Snake2/snake_body.png"
SNAKEHEAD_PATH = "Snake2/snake_body2.png"

"""----------------------------------------------------------------"""

class SnakeBody(arcade.Sprite):
    def __init__(self, filename: str, bodybefore, scale: float = 1.0):
        super().__init__(filename, scale) 
        self.bodybefore = bodybefore
        self.center_x_before = self.center_x
        self.center_y_before = self.center_y
    def move(self):
        self.center_x_before = None
        self.center_y_before = None
        self.bodybefore.center_x_before = self.center_x
        self.bodybefore.center_y_before = self.center_y

class SnakeHead(arcade.Sprite):
    def __init__(self, filename: str, scale: float = 1.0, direction: str = "south"): 
        super().__init__(filename, scale) 
        self.direction = direction

    def move(self):
            if self.direction == "south":
                self.center_y -= MOVEMENT_SPEED #runter bewegen
            elif self.direction == "north":
                self.center_y += MOVEMENT_SPEED #hoch bewegen
            elif self.direction == "west":
                self.center_x -= MOVEMENT_SPEED #links bewegen
            elif self.direction == "east":
                self.center_x += MOVEMENT_SPEED #rechts bewegen

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

    def setup(self):
        self.time = 0
        self.total_time = 0
        self.esc_timer = -1

        self.snake_list = arcade.SpriteList()
        self.snakehead = SnakeHead(SNAKEHEAD_PATH, SCALE, STARTING_DIRECTION)
        self.snakehead.center_x = SCREEN_WIDTH / 2
        self.snakehead.center_y = SCREEN_HEIGHT / 2
        self.snake_list.append(self.snakehead)

        self.snakebody_1 = SnakeBody(SNAKEBODY_PATH, self.snakehead, 1.0)
        self.snakebody_1.center_x = SCREEN_WIDTH / 2 
        self.snakebody_1.center_y = SCREEN_HEIGHT / 2 + 16*1
        self.snake_list.append(self.snakebody_1)

        self.snakebody_2 = SnakeBody(SNAKEBODY_PATH, self.snakebody_1, 1.0)
        self.snakebody_2.center_x = SCREEN_WIDTH / 2
        self.snakebody_2.center_y = SCREEN_HEIGHT / 2 + 16*2
        self.snake_list.append(self.snakebody_2)
        
        

    def on_draw(self):
        self.clear()
        self.snake_list.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        self.snake_list.update()

        self.time += delta_time
        self.total_time += delta_time

        if self.time >= 0.5:
            self.snakehead.move()
            self.snakebody_1.move()
            self.snakebody_2.move()
            self.time = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ESCAPE:
            self.esc_timer = self.total_time

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