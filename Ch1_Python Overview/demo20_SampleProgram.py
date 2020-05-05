# 고객 처리 프로그램

class CashierLine :             # 클래스 정의
    lstLine = []
    def addCustomer(self, strName):
        self.lstLine.append(strName)
    def processCustomer(self):
        strReturnName = self.lstLine[0]
        self.lstLine.remove(strReturnName)
        return strReturnName
    def printStatus(self):
        strReturn = ""
        for i in range(len(self.lstLine)):
            strReturn += self.lstLine[i] + " "
        return strReturn

binLoop = True
line = CashierLine()            # 객체 생성
while binLoop:
    strName = input("Enter customer name : ")
    if strName == ".":
        break
    elif strName == "->":
        print("Processed : ", line.processCustomer())
        print("Line : ", line.printStatus())
    else:
        line.addCustomer(strName)
        print("Line : ", line.printStatus())
print("Number of remaining customers : ", len(line.lstLine))

