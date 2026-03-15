while True :
  try :
    print("try구문입니다")
    break
    print("try구문 뒤입니다")
  except :
    print("except구문입니다")
  else :
    print("else 구문입니다")
  finally :
    print("finally구문입니다")

  print("while문 마지막줄입니다")

print("종료")

# break도 마찬가지로 while문을 빠져나와도 fianlly구문은 무조건 출력
