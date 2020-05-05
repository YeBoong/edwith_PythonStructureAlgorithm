# 생성자와 소멸자

from time import ctime

class MyHome :              # 클래스 정의
    colorRoof = 'red'
    stateDoor = 'Closed'
    # 두 개의 속성
    def paintRoof(self, color):
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'Open'
    def closeDoor(self):
        self.stateDoor = 'Close'
    def printStatus(self):
        print("Roof color is ", self.colorRoof, ', and Door is ', self.stateDoor)
    def __init__(self,strAddress):              # 생성자
        print("Built on ", strAddress)
        print("Built at ", ctime())
    def __del__(self):                          # 소멸자
        print("Destroyed at ", ctime())
    # 6개의 기능

homeAtBusan = MyHome('Busan S')     # 생성자 실행
homeAtBusan.printStatus
del homeAtBusan         # 소멸자 실행
                        # del 같은 제거 함수를 따로 사용하지 않아도
                        # 더 이상 사용하지 않는 객체 or 변수들은 garbage collector에 의해서
                        # 자동으로 메모리에서 삭제되고, 소멸자도 자동으로 실행된다.