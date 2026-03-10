# 5. [종합 응용: 로그인 시스템]
# 문제: users = {"admin": "1234", "user1": "pwpw"}라는 딕셔너리가 있습니다.
# while문을 사용하여 아이디와 비밀번호를 입력받습니다.
# 딕셔너리에 있는 아이디와 비밀번호가 일치하면 "환영합니다"를 출력하고 break로 종료합니다. 
# 일치하지 않으면 "다시 입력하세요"를 출력하고 계속 반복합니다.

users = {"admin": "1234", "user1": "pwpw"}

while True :
    id = input("아이디를 입력하세요: ")
    pw = input("비밀번호를 입력하세요: ")
    
    id = "id"
    if id in users and users[id] == pw :  # 오답부분 - users에 id가 있는지 확인하고, 해당 id라는 key의 value가 pw와 일치하는지 확인해야됨
        print("환영합니다")
        break
    else :
        print("다시 입력하세요")
