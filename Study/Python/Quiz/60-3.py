# 문제 3: 학생 점수 중 60점 이상만 통과 처리 + 보정점수 계산
# 조건
# filter로 60점 이상(합격) 점수만 걸러라.
# map으로 걸러진 점수에 +5점 보정 점수를 적용하라.
# 보정된 점수 리스트를 출력하라.
# 예상 출력 형태: [83, 97, 66, 93, 78]

scores = [35, 78, 92, 55, 61, 47, 88, 73]
result1 = filter(lambda x:x>=60, scores)
result2 = map(lambda x:x+5, result1)
print(list(result2))
