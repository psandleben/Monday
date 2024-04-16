import arcade

"""----------------------------------------------------------------"""

class GUI(arcade.Window):
    def __init__(self, breite, höhe):
        super().__init__(breite, höhe, "Tic Tac Toe", False, True)
        self.field_coordinates = None
        self.field_status = None
        self.total_time = None
        self.mouse_release_timer = None
        self.circle_radius = None
        self.line_width = None

    def setup(self):
        #self.field_coordinates = [[[0,600],[200, 400]], [[200,600],[400, 400]], [[400,600],[600, 400]], [[0,400],[200, 200]], [[200,400],[400, 200]], [[400,400],[600, 200]], [[0,200],[200, 0]], [[200,200],[400, 0]], [[400,200],[600, 0]]]
        self.field_coordinates = [[[0,self.height],[self.width/3, self.height/3*2]], [[self.width/3,self.height],[self.width/3*2, self.height/3*2]], [[self.width/3*2,self.height],[self.width, self.height/3*2]], [[0,self.height/3*2],[self.width/3, self.height/3]], [[self.width/3,self.height/3*2],[self.width/3*2, self.height/3]], [[self.width/3*2,self.height/3*2],[self.width, self.height/3]], [[0,self.height/3],[self.width/3, 0]], [[self.width/3,self.height/3],[self.width/3*2, 0]], [[self.width/3*2,self.height/3],[self.width, 0]]]
        self.field_status = [0, 0, 0, 0, 0, 0, 0, 0, 0] #0 = None | -1 = o | 1 = x
        self.total_time = 0
        self.mouse_release_timer = -1
        if self.height <= self.width:
            self.circle_radius = self.height / 8
        else: self.circle_radius = self.width / 8
        self.line_width = self.circle_radius/7.5

    def on_draw(self):
        self.clear()
        
        self.draw_outlines()
        self.draw_infill()

    def on_update(self, delta_time):
        self.total_time += delta_time
        
        if self.mouse_release_timer != -1:
            self.mouse_release_timer += delta_time


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.mouse_release_timer = self.total_time

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.total_time >= 1.5 + self.mouse_release_timer:
                self.mouse_release_timer = -1
        else:
            if button == arcade.MOUSE_BUTTON_LEFT:
                for i in range(len(self.field_coordinates)):
                    if x >= self.field_coordinates[i][0][0] and y <= self.field_coordinates[i][0][1] and x <= self.field_coordinates[i][1][0] and y >= self.field_coordinates[i][1][1]:
                        self.field_status[i] = -1
                        break
            elif button == arcade.MOUSE_BUTTON_RIGHT:
                for i in range(len(self.field_coordinates)):
                    if x >= self.field_coordinates[i][0][0] and y <= self.field_coordinates[i][0][1] and x <= self.field_coordinates[i][1][0] and y >= self.field_coordinates[i][1][1]:
                        self.field_status[i] = 1
                        break
                
        #print(str(self.field_status))
        #print(str(x), " ", str(y))

    def draw_outlines(self):
        arcade.draw_line(0, self.height / 3, self.width, self.height / 3, arcade.color.WHITE, self.line_width)
        arcade.draw_line(0, self.height / 3*2, self.width, self.height / 3*2, arcade.color.WHITE, self.line_width)
        arcade.draw_line(self.width / 3, 0, self.width / 3, self.height, arcade.color.WHITE, self.line_width)
        arcade.draw_line(self.width / 3 * 2, 0, self.width / 3 * 2, self.height, arcade.color.WHITE, self.line_width)
    
    def draw_infill(self):
        for i in range(len(self.field_status)):
            if self.field_status[i] == -1:
                x = (self.field_coordinates[i][1][0] - self.width/6)
                y = (self.field_coordinates[i][0][1] - self.height/6)
                arcade.draw_circle_outline(x, y, self.circle_radius, arcade.color.WHITE,self.line_width)
                
                #print("x: ", x, "y: ", y)
                #print(str(self.field_status))
                #print(i)

            elif self.field_status[i] == 1:
                x = (self.field_coordinates[i][1][0] - self.width/6)
                y = (self.field_coordinates[i][0][1] - self.height/6)
                arcade.draw_line(x-self.circle_radius, y+self.circle_radius, x+self.circle_radius, y-self.circle_radius, arcade.color.WHITE, self.line_width)
                arcade.draw_line(x+self.circle_radius, y+self.circle_radius, x-self.circle_radius, y-self.circle_radius, arcade.color.WHITE, self.line_width)
        
    def on_resize(self, width: float, height: float):
        super().on_resize(width, height)
        self.field_coordinates = [[[0,self.height],[self.width/3, self.height/3*2]], [[self.width/3,self.height],[self.width/3*2, self.height/3*2]], [[self.width/3*2,self.height],[self.width, self.height/3*2]], [[0,self.height/3*2],[self.width/3, self.height/3]], [[self.width/3,self.height/3*2],[self.width/3*2, self.height/3]], [[self.width/3*2,self.height/3*2],[self.width, self.height/3]], [[0,self.height/3],[self.width/3, 0]], [[self.width/3,self.height/3],[self.width/3*2, 0]], [[self.width/3*2,self.height/3],[self.width, 0]]]
        if self.height <= self.width:
            self.circle_radius = self.height / 8
        else: self.circle_radius = self.width / 8
        self.line_width = self.circle_radius/7.5

"""----------------------------------------------------------------"""     
    
game = GUI(500,500)
game.setup()
arcade.run()