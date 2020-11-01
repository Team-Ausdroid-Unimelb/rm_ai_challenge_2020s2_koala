class LabelledImage():
    def __init__(self, ID=None, filename=None, speed=0, armours=[]):
        self.ID = ID
        self.filename = filename
        self.speed = speed
        self.armours = armours       

class Armour():
    def __init__(self, robot=str(), pose=str(), location=[0,0,0,0], confidence=0):
        self.robot = robot              # red 1, red 2, blue 1 or blue 2.
        self.pose = pose                # front, side or back.
        self.location = location        # [x, y, weight, height]
        self.confidence = confidence    # 0 to 1