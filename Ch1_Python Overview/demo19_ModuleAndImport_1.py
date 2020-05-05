from time import ctime

# 클래스 정의 파일과 
# 실행 파일 따로 만들기
# 1. 클래스 정의 파일

class MyHome:           # 클래스 정의
    colorRoof = 'Red'
    stateDoor = 'closed'
    def paintRoof(self, color):
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'Open'
    def closeDoor(self):
        self.stateDoor = 'Closed'
    def printStatus(self):
        print("Roof color is ", self.colorRoof, ", and Door is", self.stateDoor)
    def __init__(self, strAddress):
        print("Built on ", strAddress)
        print("Built at ", ctime())
    def __del__(self):
        print("Destroyed at : ", ctime())
    
    