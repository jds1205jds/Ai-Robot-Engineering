# numbers 내부에 들어 있는 숫자가 몇 번 등작하는지 출력하는 코드를 작성하세요.
numbers=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter={}

numbers.sort() # 정렬

for number in numbers:
    if number in counter:
        counter[number]+=1
    else:
        counter[number]=1

print(counter)
