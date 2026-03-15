try :
  file = open("info.txt", "w")
  예외.발생()

except : 
  print("오류 발생")

finally :
  file.close()
  print("file.colsed : ", file.closed)

# 출력 
# 오류발생
# file.closed : True
