class HelloWorld:               # 클래스 정의
    def __init__(self):             # 생성자
        print("Hello World")
    def __del__(self):              # 소멸자
        print("Good bye")
    def performAverage(self, num1, num2):
        average = (num1 + num2) / 2.0
        print("The average of the scores is : ", average)

def main():
    world = HelloWorld()
    score1, score2 = input("Enter two scores separated by a comma : ").split(",")
    world.performAverage(int(score1), int(score2))

main()