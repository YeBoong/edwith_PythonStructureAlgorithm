# 클래스와 객체

class MyHome:
    colorRoof = 'Red'       
    stateDoor = 'Closed'
    # 두 개의 속성(변수)
    def paintRoof(self, color):
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'Open'
    def closeDoor(self):
        self.stateDoor = 'Close'
    def printStatus(self):
        print("Roof color is : ", self.colorRoof, ", and door is ", self.stateDoor)
    # 4개의 기능(함수)

home1 = MyHome()    # 객체 생성
home2 = MyHome()    # 객체 생성

home2.openDoor()
home1.paintRoof('Blue')
home1.printStatus()
home2.printStatus()

