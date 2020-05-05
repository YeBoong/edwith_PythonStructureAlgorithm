# 클래스 정의 파일과 
# 실행 파일 따로 만들기
# 2. import 및 실행 파일

from demo19_ModuleAndImport_1 import MyHome

homeAtBusan = MyHome("Busan S") # 생성자 실행
homeAtBusan.printStatus()
# Garbage Collector에 의한 소멸자 자동 실행.

