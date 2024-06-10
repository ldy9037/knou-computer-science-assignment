# 입력값 유효성 검증을 위해 함수 생성
def validate(operand: int) -> None:
    if operand <= 0: # 입력값이 0이거나 0보다 작으면 
        raise ValueError("반지름 및 높이는 양수만 지정 가능합니다.") # ValueError로 예외 발생
    
#반지름 사용자 입력
rad = int(input("반지름을 입력하세요:")) #높이 사용자 입력
validate(rad)             
    
hei = int(input("높이를 입력하세요:")) #부피&겉넓이 계산
validate(hei)
                          
vol = 1/3 * 3.14 * rad ** 2 * hei
suf = 3.14 * rad ** 2 + 3.14 * rad * hei 
print("원뿔의 부피는" ,vol, "입니다.") 
print("원뿔의 겉넓이는" ,suf, "입니다")