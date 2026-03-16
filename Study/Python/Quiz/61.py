# 문제 1: 가상 학생 성적 CSV 파일 생성하기
# 조건
# students.csv 파일을 생성한다.
# 학생 수는 1000명으로 한다.
# id (1~1000 번호)
# name (랜덤 한글 3글자 조합)
# math 점수 (0~100 랜덤)
# english 점수 (40~100 랜덤)
# CSV 형식으로 저장한다. (콤마 구분)
# ex)
# id,name,math,english
# 1,박민수,87,74
# 2,김하준,45,93

import random

n1 = list("김이박최정강조윤장임한오서신")
n2 = list("재석영수민지현우철훈수진미규")

with open("students.csv", "w") as file:
    for i in range(30):
        id = i+1
        name = random.choice(n1) + random.choice(n2) + random.choice(n2)
        math = random.randrange(0,100)
        eng = random.randrange(0,100)
        file.write("{}. {}/{}/{}\n".format(id, name, math, eng))
