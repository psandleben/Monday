import arcade

class GUI(arcade.Window):
    def __init__(self, breite, höhe):
        super().__init__(breite, höhe, "Tic Tac Toe")
        field = [[[0,600],[200, 400]], [[200,600],[400, 400]], [[400,600],[600, 400]], [[0,400],[200, 200]], [[200,400],[400, 200]], [[400,400],[600, 400]], [[0,200],[200, 0]], [[200,200],[400, 0]], [[400,200],[600, 0]]]

    def on_mouse_press(self):
        pass
    
    def on_draw(self):
        self.clear()
    
        arcade.draw_line(0, self.height / 3, self.width, self.height / 3, arcade.color.WHITE, 10)
        arcade.draw_line(0, self.height / 3*2, self.width, self.height / 3*2, arcade.color.WHITE, 10)

        arcade.draw_line(self.width / 3, 0, self.width / 3, self.height, arcade.color.WHITE, 10)
        arcade.draw_line(self.width / 3 * 2, 0, self.width / 3 * 2, self.height, arcade.color.WHITE, 10)

GUI(600,600)
arcade.run()