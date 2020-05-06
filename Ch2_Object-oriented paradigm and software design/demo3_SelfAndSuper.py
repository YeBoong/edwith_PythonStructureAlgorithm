# self : 객체 자기 자신을 가리킨다.
# super : 부모 클래스를 가리킨다.

class Father(object):
    strHometown = 'Jeju'
    def __init__(self, paramHome):
        self.strHometown = paramHome            # Father 클래스 자신의 속성인 strHometown의 값을 객체 생성 시 매개변수로 받을 paramHome의 값으로 OverWrite 한다. 
        print("Father is created")
    def doFatherThing(self):
        print("Father's action")
    def doRunning(self):
        print("Slow")

class Mother(object):
    strHometown = 'Seoul'
    def __init__(self):
        print("Mother is created")
    def doMotherThing(self):
        print("Mother's action")
    
class Child(Father, Mother):                
    strName = "Moon"
    def __init__(self, paramName, paramHome):   # 자기 자신인 Child 객체 생성 시에 매개변수로 paramName과 paramHome의 값을 받는다.
        super(Child, self).__init__(paramHome)  # 자기 자신인 Child 객체의 부모 클래스이면서 우선 상속 받는 Father 클래스의 생성자를 실행한다. 이때 매개변수로 paramHome 값을 전달한다.  
        self.strName = paramName                # 객체 자기 자신의 속성인 strName 값을 매개변수 paramName의 값으로 OverWrite한다.
        print("Child is created")
    def doRunning(self):                
        print('Fast')

me = Child("Sun", "Universe")                   # paramName = Sun, paramHome = Universe
me.doFatherThing()                              
me.doMotherThing()
me.doRunning()
print(me.strHometown)                           # 우선 상속 받은 Father 클래스의 속성인 strHometown 값을 받아온다.
                                                # 이 때, strHometown의 값은 위의 생성자 실행의 영향으로 매개변수로 받은 paramHome이 OverWrite 된 값으로 출력된다.
print(me.strName)                               # 객체 me의 생성자의 "self.strName = paramName"의 영향으로 매개변수 paramName의 값으로 출력된다.

