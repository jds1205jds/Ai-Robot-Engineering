//Q1) (수식문제) 당신의 나이를 출력하세요.
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <time.h>

int main() {
    int birth_year;
    int current_year = 2025;
    printf("태어난 년도를 입력해주세요: ");
    scanf("%d", &birth_year);
    printf("당신의 나이는 %d세 입니다\n", current_year - birth_year + 1);
    return 0;
}
