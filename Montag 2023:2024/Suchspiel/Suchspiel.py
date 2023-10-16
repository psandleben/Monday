import arcade
import random

#asprite für grafiken
#pip3 install arcade

class Suchspiel(arcade.Window):
    
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


