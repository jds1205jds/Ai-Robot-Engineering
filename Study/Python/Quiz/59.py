# 리스트에서 중복된 값들을 모두 찾아 리스트로 반환하는 함수
# 동일 숫자가 2번 이상 등장하는 항목만 추려내야 한다.
# 중복된 값이 여러 번 있어도 한 번만 결과에 포함한다.

numbers = [1, 2, 3, 2, 4, 5, 3, 3, 6]

def find_duplicates(numbers):
    new_list = []
    for i in numbers:
        if numbers.count(i) > 1 and i not in new_list:
            new_list.append(i)

    return new_list

print(find_duplicates(numbers))
