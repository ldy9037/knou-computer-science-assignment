# 두 값을 매개변수로 받아 큰 값을 반환하는 함수
def get_bigger_num(a: int, b: int) -> int:
    return a if a >= b else b # a가 b보다 같거나 크면 a를 반한하고 b가 a보다 크면 b를 반환

# 배개변수로 받은 숫자가 짝수인지 홀수인지 체크하는 함수
def check_type(number: int) -> str:
    return "짝수" if number % 2 == 0 else "홀수" # 숫자를 2로 나눴을 때 나머지가 0이면 "짝수" 반환, 나머지가 있으면 "홀수" 반환

a, b = map(int, input("두 숫자를 공백으로 구분해서 입력해주세요.").split()) # 두 숫자를 입력
bigger_num = get_bigger_num(a, b) # 두 숫자 중 큰 숫자를 확인
print("큰 값은 %d이며 %s입니다."%(bigger_num, check_type(bigger_num))) # 큰 숫자와 홀수/짝수 여부를 출력