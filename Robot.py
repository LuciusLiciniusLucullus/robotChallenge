
# coding: utf-8

# In[75]:


rotations = {
    "NORTH": [{"LEFT": "WEST"}, {"RIGHT": "EAST"}],
    "WEST": [{"LEFT": "SOUTH"}, {"RIGHT": "NORTH"}],
    "EAST": [{"LEFT": "NORTH"}, {"RIGHT": "SOUTH"}],
    "SOUTH": [{"LEFT": "EAST"}, {"RIGHT": "WEST"}]
}

def checkOutbound(num):
    if num < 0 or num > 5:
        return True
    else:
        return False
    
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.face = "NORTH"
        
    def place(self, x, y, face):
        self.x = x
        self.y = y
        self.face = face
        
    def move(self):
        if self.face == "NORTH":
            if not checkOutbound(self.y + 1):
                self.y += 1
        elif self.face == "WEST":
            if not checkOutbound(self.x - 1):
                self.x -= 1
        elif self.face == "EAST":
            if not checkOutbound(self.x + 1):
                self.x += 1
        else:
            if not checkOutbound(self.y - 1):
                self.y -= 1
            
    def redirection(self, direction):
        if direction == "LEFT":
            self.face = rotations[self.face][0]["LEFT"]
        else:
            self.face = rotations[self.face][1]["RIGHT"]
        
    def report(self):
        print(str(self.x) + ", " + str(self.y) + ", " + self.face)
      
#init robot
newRobot = Robot()

def control(input):
    command = input.split(" ")
    userChoice = command[0]
    if userChoice.upper() == "PLACE":
        x,y,face = command[1].split(",")
        newRobot.place(int(x),int(y),face)
    elif userChoice.upper() == "REPORT":
        newRobot.report()
    elif userChoice.upper() == "MOVE":
        newRobot.move()
    elif userChoice.upper() == "LEFT" or userChoice == "RIGHT":
        newRobot.redirection(userChoice)
        
#tests       
control("PLACE 1,2,EAST")
control("MOVE")
control("MOVE")
control("LEFT")
control("MOVE")
control("REPORT")

        
        

