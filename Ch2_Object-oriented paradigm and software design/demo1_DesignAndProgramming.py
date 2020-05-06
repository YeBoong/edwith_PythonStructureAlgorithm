# 좋은 소프트웨어의 기준
    #   정확성
    #   :   client의 목적에 부합해야한다.
    #   :   error 없이 정확한 결과를 도출해야한다.

    #   기반의 탄탄함.
    #   :   client의 과중한 입력,
    #       예상하지 못한 입력, 
    #       예상하지 못한 습관,
    #       유연하게 대응할 수 있어야한다.

    #   유연성
    #   :   이후의 소프트웨어 수정 및 업데이트 같은 유지 보수 확장성이 좋아야한다.

    #   사용성과 재사용성
    #   :   처음 사용자도 쓰기 쉽도록 인터페이스, UI 등을 잘 디자인 해야한다.
    #   :   다양한 환경에서 지원
    #   :   소프트웨어의 주 기능 이외에도 
    #       다양한 목적으로도 어느정도 쓸 수 있도록 추가 기능을 제공해야한다.

    #   효율성
    #   :   빠른 실행속도
    #   :   작은 용량
    #   :   쉽게 구현해놔야한다.


# 객체 지향
    # 현실 세계의 요소들을 얼마나 추상화(Abstract)를 잘 하느냐가 관건.
        # ex)   :   은행 시스템
            # 고객
                # : 속성 - ID, Name, AccountNum 등
                # : 기능 - 로그인(), 인출 요청(), 보안카드 확인() 등 
            # 거래
                # : 속성 - amount, releaseATMID(거래가 발생한 ATM의 ID 정보)
                # : 기능 - releaseMoney()
            # 뱅킹(예금, 이체)
                # : 속성 - amountInAccount(계좌 잔고 정보)
                # : 기능 - reduceMoney(), sendNotice()

    # 클래스 VS 객체
        # 클래스
            # 하나의 틀, 설계도. 정의 부분.
            # 실행 전 구현만 해놓은 것.
            # 개념화 시킨 것.
        # 객체
            # 실행의 결과물.
            # 클래스를 실체화 시킨 것.

    # 접근제한자 : public(+), private(-), protected(#) 등이 있지만, 파이썬은 지원하지 않는다.
    #              파이썬은 '__'를 이용하여 접근을 권장하지 않는다는 표시를 하는 방법이 있다.
    # 캡슐화 : 클래스 내부가 가려져 있고, 외부에서는 메소드를 통해서 접근 가능하도록 하는 구조.
    # 상속


# UML : 소프트웨어 설계 표준 모델
# UML notation : Class and Instance
    # Abstrct class - Person
    # class - Customer
    # Named Istance - Park::Customer  (객체 이름 :: 클래스 이름)
    # Unnamed Istance - :Customer

    # Park::Customer
        # -ID : String, 접근제한자 : private / 속성 이름 : ID / 데이터 타입 : String
        # #AccountNum : Integer, 접근제한자 : protected / 속성 이름 : AccountNum / 데이터 타입 : Integer
        # +Name : String = Hey, 접근제한자 : public / 속성 이름 : Name / 데이터 타입 : String / Default 값 : Hey

        # +login() : void, 메소드 이름 : login / 접근제한자 : public / 반환 타입 : void
        # +requestWithdrawal() : Boolean, 메소드 이름 : requestWithdrawal / 접근제한자 : public / 반환 타입 : boolean
        # +confirmSecurityCard() : Boolean, 메소드 이름 : confirmSecurityCard / 접근제한자 : public / 반환 타입 : boolean


# 캡슐화 : 클래스 내부가 가려져 있고, 
#          외부에서는 메소드를 통해서 접근 가능하도록 하는 구조.
    # 개체(Object) : Data + Behavior
        # Data : 속성(Attribute, field, variable)
        # Behavior : 기능(Function, Method)

    # 캡슐화를 구현하려면 접근제한자가 필요.
        # public, private, protected 등
    
    # 파이썬은 사실 공식적으로는 접근제한자 기능을 제공하지 않는다.
    