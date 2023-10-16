import arcade, random

SCREEN_WIDTH = 560
SCREEN_HEIGHT = 440
SCREEN_TITLE = "Starting Template"

MOVEMENT_SPEED = 16

SNAKE_BODY_PATH = "Snake/snake_body.png"

"""class Snake(arcade.Sprite):
     Player Class 

    def update(self):
         Move the player 
        # Move player.
        # Remove these lines if physics engine is moving player.
        # self.center_x += self.change_x
        # self.center_y += self.change_y

        
        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1"""

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.snake_list = None

        self.time = 0
        self.total_time = 0

        self.direction = 0


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.snake_list = arcade.SpriteList()

        self.body_1 = arcade.Sprite(SNAKE_BODY_PATH) 
        self.body_1.center_x = SCREEN_WIDTH / 2
        self.body_1.center_y = SCREEN_HEIGHT / 2
        self.snake_list.append(self.body_1)

        self.total_time = 0

        self.direction = 0


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        self.snake_list.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.snake_list.update()

        self.time += delta_time
        self.total_time += delta_time

        if self.time >= 0.25 and self.time <= 0.3:
            if self.direction == 0:
                self.body_1.center_y += MOVEMENT_SPEED
            if self.direction == 2:
                self.body_1.center_y += -MOVEMENT_SPEED
            if self.direction == 1:
                self.body_1.center_x += MOVEMENT_SPEED
            if self.direction == 3:
                self.body_1.center_x += -MOVEMENT_SPEED

            self.time = 1
        
        if self.time >= 1.25:
            self.time = 0

        


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        if key == arcade.key.A:
            self.direction += 1
            if self.direction == 4:
                self.direction = 0
        elif key == arcade.key.D:
            self.direction -= 1
            if self.direction == -1:
                self.direction = 3

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        
        if key == arcade.key.A or key == arcade.key.DOWN:
            self.body_1.change_y = 0
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.body_1.change_y = 0

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


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()


"""class Suchspiel(arcade.Window):
    
    pop_sound = arcade.load_sound("sound/pop_1.wav")

    def __init__(self, breite, höhe, titel, fullscreen = False):
        super().__init__(breite, höhe, titel, True, True)

        arcade.set_background_color(arcade.color.WOOD_BROWN)

        self.gegenstand_liste = arcade.SpriteList()

        for i in range(5000):
            crate_1 = arcade.Sprite("grafik/crate.png") 
            crate_1.center_x = random.randrange(self.width)
            crate_1.center_y = random.randrange(self.height)
            self.gegenstand_liste.append(crate_1)

            crate_2 = arcade.Sprite("grafik/crate.png") 
            crate_2.center_x = random.randrange(self.width)
            crate_2.center_y = random.randrange(self.height)
            self.gegenstand_liste.append(crate_2)

            crate_3 = arcade.Sprite("grafik/crate.png") 
            crate_3.center_x = random.randrange(self.width)
            crate_3.center_y = random.randrange(self.height)
            self.gegenstand_liste.append(crate_3)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.close_window()
    
    def on_mouse_press(self,x,y, button, modifiers):
        hit_box_mouse = arcade.Sprite()
        hit_box_mouse.center_x = x
        hit_box_mouse.center_y = y
        hit_box_mouse.set_hit_box([(100,100), (-100,100), (100, -100), (-100, -100)])

        hitliste = arcade.check_for_collision_with_list(hit_box_mouse, self.gegenstand_liste)
        for gegenstand in hitliste:
            arcade.play_sound(self.pop_sound)
            gegenstand.center_x = random.randrange(700)
            gegenstand.center_y = random.randrange(500)


    def on_draw(self):
        self.clear()
        self.gegenstand_liste.draw()

sp = Suchspiel(800, 600, "Find the Items")

arcade.run()


"""