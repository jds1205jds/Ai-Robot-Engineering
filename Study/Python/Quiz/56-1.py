# Q56) 사칙연산 계산 if, elif, else
# 문자열로 주어진 연산자 "+", "-", "*", "/" 와 두 정수를 입력받아 올바른 연산 결과를 출력하라.
# switch case문 사용금지, if-else문으로 해결할것

calculator = input("연산자 입력 : ")
a = int(input("첫 번째 숫자 입력 : "))
b = int(input("두 번째 숫자 입력 : "))

if calculator == "+" :
    print(a + b)
elif calculator == "-" :
    print(a - b)
elif calculator == "*" :
    print(a * b)
elif calculator == "/" :
    print(a / b)
else :
    print("잘못된 연산자입니다.")
