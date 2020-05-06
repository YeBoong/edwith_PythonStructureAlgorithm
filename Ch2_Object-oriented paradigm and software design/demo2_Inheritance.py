# Inheritance (상속)
    # 부모 클래스(super class)의 속성과 기능을 자식 클래스(sub class)에 제공
    # 자식 클래스(sub class)는 상속 받은 속성과 기능 외에 자신만의 속성과 기능을 가질 수 있다.
    # 상속 받은 속성 및 기능의 값을 새롭게 초기화 하거나 덮어 쓸 수 있다.(Polymorphism : Overriding, Overloading)

    # Super Class
        # 부모 클래스
        # 개념적 관점에서 일반화
        # Sub Class 들이 공통적으로 가질 속성과 기능.
    # Sub Class
        # 자식 클래스
        # 개념적 관점에서 특별화, 전문화
        # Super Class로부터 받은 공통 된 속성 및 기능 외에 자기만의 속성 및 기능을 가짐.

    # ex)
        # Person(super class)
            # 속성 : NatlRegisterNum
            # 기능 : login()
        
            # Customer(sub class)
                # 속성 : NatlRegisterNum, ID, AccountNum
                # 기능 : login(), requestWithdrawal(), confirmSecurityCard()

            # Employee(sub class)
                # 속성 : NatlRegisterNum, EmplID, Clearance
                # 기능 : login(), overideTransaction(), searchCustomer()

class Father(object):
    strHometown = 'Jeju'
    def __init__(self):
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
    
class Child(Father, Mother):            # Father 클래스와 Mother 클래스 두 개를 다중 상속 받는다.
                                        # strHometown이나 생성자(__init__)같은 중복 상속 요소는 우선 상속받는(= 먼저 쓴) Father 클래스 쪽으로 상속 받는다.
                                        # 이 Child에 대한 객체를 생성할 경우, Mother 클래스의 생성자는 실행 되지 않고, 
                                        # me.strHometown을 출력할 경우에도, Father 클래스의 strHometown 값인 'Jeju'가 출력되는 것을 알 수 있다.
    strName = "Moon"
    def __init__(self):                 # 생성자는 우선 상속되는 Father 클래스의 생성자와 Child 클래스의 생성자 총 2개가 실행된다. 
        super(Child, self).__init__()
        print("Child is created")
    def doRunning(self):                # 부모 클래스인 Father 클래스의 doRunning 메소드를 Overwrite했다.
        print('Fast')

me = Child()
me.doFatherThing()
me.doMotherThing()
me.doRunning()
print(me.strHometown)
print(me.strName)