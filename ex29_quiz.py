"""  
[1] member 리스트를 이름 가나다 순으로 정렬해 출력하세요
[2] member 회원 중 '신석하' 회원을 탈퇴시키세요
[3] 신입 회원 '도지원'을 추가하세요
[4] 정우람 회원을 정가람으로 변경하세요
[5] 이름 내림차순으로 정렬해 다시 출력하세요
"""
member = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석하', '강민규', '전민수', '박찬호', '이승엽']

# [1]
a = sorted(member)
print(a)

# [2]
a.remove('신석하')
print(a)

# [3]
a.append('도지원')
print(a)

# [4]
a[-3] = '정가람'
print(a)

# [5]
b = sorted(a, reverse=True)
print(b)

# 문제 2
# 1 ~ 45 사이의 임의의 정수 6개를 비복원 추출하여 리스트와 튜플에 저장하는 프로그램을 작성하시오.
import random
# 비복원 추출: 중복되는 값 없이 추출. random.sample() => 비복원 추출함. 이거 사용하지 말고 해보기

# [문제 2]
x = (0,)
for ran in range(6):
    r = random.randint(1, 46)
    if r != ran:
    print(x, type(x))
