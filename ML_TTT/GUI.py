import arcade
import random

"""----------------------------------------------------------------"""

class GUI(arcade.Window):
    def __init__(self, breite, höhe):
        super().__init__(breite, höhe, "Tic Tac Toe", False, True)
        self.winner = None
        self.PC = None
        self.field_coordinates = None
        self.field_status = None
        self.total_time = None
        self.mouse_release_timer = None
        self.circle_radius = None
        self.line_width = None


    def setup(self):
        #self.field_coordinates = [[[0,600],[200, 400]], [[200,600],[400, 400]], [[400,600],[600, 400]], [[0,400],[200, 200]], [[200,400],[400, 200]], [[400,400],[600, 200]], [[0,200],[200, 0]], [[200,200],[400, 0]], [[400,200],[600, 0]]]
        self.winner = False
        self.PC = PlayerPC("easy", self.field_status)
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
        self.check_winner()
        
        if self.mouse_release_timer != -1:
            self.mouse_release_timer += delta_time

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.mouse_release_timer = self.total_time
 
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.winner == False:
            if self.total_time >= 1.5 + self.mouse_release_timer:
                    self.mouse_release_timer = -1
            else:
                
                if button == arcade.MOUSE_BUTTON_LEFT:
                    for i in range(len(self.field_coordinates)):
                        if x >= self.field_coordinates[i][0][0] and y <= self.field_coordinates[i][0][1] and x <= self.field_coordinates[i][1][0] and y >= self.field_coordinates[i][1][1] and self.field_status[i] == 0:
                            self.field_status[i] = 1
                            if 0 in self.field_status:
                                self.PC.makemove();
                            break
                
                
                
                
                
                """if button == arcade.MOUSE_BUTTON_RIGHT:
                    for i in range(len(self.field_coordinates)):
                        if x >= self.field_coordinates[i][0][0] and y <= self.field_coordinates[i][0][1] and x <= self.field_coordinates[i][1][0] and y >= self.field_coordinates[i][1][1] and self.field_status[i] == 0:
                            self.field_status[i] = -1
                            break"""    
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

    def check_winner(self):
        if self.field_status[0] == 1 and self.field_status[1] == 1 and self.field_status[2] == 1:
            self.winner = True
        elif self.field_status[3] == 1 and self.field_status[4] == 1 and self.field_status[5] == 1:
            self.winner = True
        elif self.field_status[6] == 1 and self.field_status[7] == 1 and self.field_status[8] == 1:
            self.winner = True
        
        elif self.field_status[0] == 1 and self.field_status[3] == 1 and self.field_status[6] == 1:
            self.winner = True
        elif self.field_status[1] == 1 and self.field_status[4] == 1 and self.field_status[7] == 1:
            self.winner = True      
        elif self.field_status[2] == 1 and self.field_status[5] == 1 and self.field_status[8] == 1:
            self.winner = True
        
        elif self.field_status[0] == 1 and self.field_status[4] == 1 and self.field_status[8] == 1:
            self.winner = True
        elif self.field_status[2] == 1 and self.field_status[4] == 1 and self.field_status[6] == 1:
            self.winner = True
        

        elif self.field_status[0] == -1 and self.field_status[1] == -1 and self.field_status[2] == -1:
            self.winner = True
        elif self.field_status[3] == -1 and self.field_status[4] == -1 and self.field_status[5] == -1:
            self.winner = True
        elif self.field_status[6] == -1 and self.field_status[7] == -1 and self.field_status[8] == -1:
            self.winner = True
        
        elif self.field_status[0] == -1 and self.field_status[3] == -1 and self.field_status[6] == -1:
            self.winner = True
        elif self.field_status[1] == -1 and self.field_status[4] == -1 and self.field_status[7] == -1:
            self.winner = True      
        elif self.field_status[2] == -1 and self.field_status[5] == -1 and self.field_status[8] == -1:
            self.winner = True
        
        elif self.field_status[0] == -1 and self.field_status[4] == -1 and self.field_status[8] == -1:
            self.winner = True
        elif self.field_status[2] == -1 and self.field_status[4] == -1 and self.field_status[6] == -1:
            self.winner = True
        
        #print(self.field_status)
        

"""----------------------------------------------------------------"""     

class PlayerPC():
    def __init__(self, strength, field_status):
        self.strength = strength
        self.field_status = field_status

    def impossible(self):
        pass

    def easy(self):
        liste = []
        for i in range(self.field_status):
            if self.field_status[i] == 0:
                liste.add(i)

        self.field_status = liste
        
        self.field_status[random.choice(liste)] = -1

    def makemove(self):
        if self.strength == "easy":
            self.easy()

    

"""----------------------------------------------------------------"""
game = GUI(500,500)
game.setup()
arcade.run()