def main():
    numYearBase10 = 2019
    numYearBase8 = 0o3743
    numYearBase16 = 0x7E3

    print("Year by base 10 : %d, by base 8 : %d, by base 16 : %d" % (numYearBase10, numYearBase8, numYearBase16))

    numComplex1 = complex(3, 4)
    numComplex2 = 4+3j

    print("Complex value : ", numComplex1)
    print("Absolute value : ", abs(numComplex2))
    print("Real value : ", numComplex2.real)
    print("image value : ", numComplex2.imag)

    strDeptName = "Computer Software Engineering"
    strUnitName = "S"
    print("Department : ", strDeptName)
    print("Full name of dept : ", strUnitName + ", " + strDeptName)

main()