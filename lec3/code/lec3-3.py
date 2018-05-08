# 파이썬의 코드 구분은 "들여쓰기"로 수행된다.
# 함수, 조건, 반복 구조 등 내포가 필요한 구문은 콜론(:)으로 구분한다.

age = input("나이를 입력하세요. : ")
if int(age) >= 20:
    print("Party Tonight")
else:
    print("Study Tonight")

# 삼항연산자
# format : 참명령문 if 조건 else 거짓명령문
print("Party Tonight" if int(age) >= 20 else "Study Tonight")
