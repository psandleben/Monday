import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Tower_Defence"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background_color = arcade.color.BATTLESHIP_GREY
    
        self.Towers = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        
        self.Towers = arcade.SpriteList()
    
        tower_1 = arcade.Sprite("Platformer/grafik/tower.png", 1)
    
        tower_1.center_x = SCREEN_WIDTH / 2
        tower_1.center_y = SCREEN_HEIGHT / 2
        self.Towers.append(tower_1)

    def on_mouse_press(self,x,y, button, modifiers):
        hit_box_mouse = arcade.Sprite()
        hit_box_mouse.center_x = x
        hit_box_mouse.center_y = y
        hit_box_mouse.set_hit_box([(100,100), (-100,100), (100, -100), (-100, -100)])

        hitliste = arcade.check_for_collision_with_list(hit_box_mouse, self.gegenstand_liste)
        for gegenstand in hitliste:
            gegenstand.

    def on_draw(self):
        """Render the screen."""

        self.clear()

        self.Towers.draw()
        # Code to draw the screen goes here

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.close_window()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()


