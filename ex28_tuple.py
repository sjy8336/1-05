# tuple
# - 순차적 데이터를 관리하는 자료형
# => 리스트와 동일하지만, 변경 불가능한 특성을 갖는다 (immutable)
# - 생성은 가능/수정, 삭제, 추가는 불가능
# - 리스트에 비해 처리 속도가 빠르다
t1 = () # [] => 리스트, () => 튜플
t2 = (1, 2, 3, 4)   # 정수 튜플
t3 = ('A', 'B', 'C', 'D')   # 문자 튜플
t4 = (120, 'Banana', 85.1, True)    # 혼합 튜플

print(t1, type(t1)) # () <class 'tuple'>
print(t2)
print(t3)
print(t4)
# 100요소를 갖는 t5 튜플 생성하세요
t5 = (100)  # 이건 튜플이 아니라 정수값
print(t5)
print(type(t5)) # <class 'int'>

t6 = (100,) # 1개의 요소를 갖는 튜플을 만들려면 반드시 쉼표를 사용해야 한다
print(t6)   # (100,)
print(type(t6))  # <class 'tuple'>

# 튜플 조회
print(t4[0], t4[2]) # 120 85.1
# 튜플 수정
# t4[0] = 'Hello'     # TypeError: 'tuple' object does not support item assignment
# t6.append(200)  # AttributeError: 'tuple' object has no attribute 'append'
# 추가 수정 삭제 불가능
t7 = 10, 20, 30     # 튜플 packing
print(t7, type(t7))  # (10, 20, 30) <class 'tuple'>
# packing: 하나의 변수에 여러 값을 할당
# unpacking: 패킹된 변수에서 여러 값을 꺼내는 것
x, y, z = t7    # 언패킹
print(x)    # 10
print(y, z) # 20 30

# 리스트 unpacking
lst = ['a', 'b', 'c', 'd']
x, y, *others = lst
print(x)    # a
print(y)    # b
print(others)   # ['c', 'd']

"""  
(1919, 3, 1) 튜플을 생성하시오
그런뒤 unpacking 을 통해 year, month, day 변수에 할당 후 아래와 같이 출력하시오
1919년 3월 1일은 삼일절 입니다
"""
# 내가 한거
Day1 = (1919, 3, 1)
year, month, day = Day1
print(f'{year}년 {month}월 {day}일은 삼일절 입니다')

theDay = 1919, 3, 1
print(theDay)   # (1919, 3, 1)
year, month, day = theDay
print(f'{year}년 {month}월 {day}일은 삼일절 입니다')

# list 2개를 만들고 하나로 합치기
lst1 = [1, 2, 3]
lst2 = [10, 20]
print(lst1)
print(lst2)
print(lst1 + lst2)  # [1, 2, 3, 10, 20]

print(lst1)
print(lst2)

lst1.extend(lst2)
print(lst1)  # [1, 2, 3, 10, 20]

# 튜플 합치기 : + 만 지원된다.
t1 = 100, 200
t2 = 'a', 'b', 'c'
t3 = t1 + t2
print(t3)   # (100, 200, 'a', 'b', 'c')
# t1.extend(t2) : 지원되지 X
# 튜플
# (1) + : tuple 요소들을 연결해서 하나로 합침
# (2) * : tuple 의 반복 연산 수행
t4 = t1 * 3
print(t4)   # (100, 200, 100, 200, 100, 200)
# 튜플 : 불변성. 조회용
# - 튜플 요소를 변경해야 한다면?
#   => list로 변환 후 => list 요소값을 변경한 후 => 다시 tuple로 변환한다
# tuple => list 로 변환: list(대상튜플)
# list => tuple로 변환: tuple(대상리스트)
print(t2)   # ('a', 'b', 'c') => 'c'를 대문자 'C'로 변경하세요

# 내가한거
""" tl2 = list(t2)
tl2[2] = 'C'
tt2 = tuple(tl2)
print(tt2) """

l2 = list(t2)
print(l2, type(l2))  # ['a', 'b', 'c'] <class 'list'>
l2[-1] = 'C'
print(l2)
t3 = tuple(l2)
print(t3)   # ('a', 'b', 'C')

# 튜플의 메소드
# (1) count(x) : 튜플 내에 x가 몇개 있는지 반환
# (2) index(x) : 튜플 내에 x가 몇번째 인덱스 위치에 있는지 반환
t = (10, 20, 30, 90, 80, 20, 40, 20, 10)
# t에 10과 20이 몇개 있는지 각각 출력해보기
cnt1 = t.count(10)
cnt2 = t.count(20)
print(f'10의 개수: {cnt1}, 20의 개수: {cnt2}')  # 10의 개수: 2, 20의 개수: 3
idx = t.index(80)
print(f'80이 저장된 위(index): {idx}')  # 80이 저장된 위(index): 4

# sorted()함수 이용해서 t를 오름차순 정렬
# 내림차순 정렬도 해보기
print(t)    # (10, 20, 30, 90, 80, 20, 40, 20, 10)
asc_t = tuple(sorted(t))    # tuple 없이 그냥하면 리스트로 나옴 [10, 10, 20, 20, 20, 30, 40, 80, 90]
print(asc_t)    

desc_t = sorted(t, reverse = True)
print(desc_t)   # [90, 80, 40, 30, 20, 20, 20, 10, 10]
# 함수에서 여러 값을 반환하는 경우 => tuple

import math
def area_circle(radius):
    result = math.pi * radius ** 2
    result2 = 2 * math.pi * radius  # 원의 둘레
    return result, result2

# 반지름이 30인 원의 면적, 둘레 출력하세요
u = area_circle(3)
print(u, type(u))
a, b = area_circle(10)  # unpacking
print(f'반지름 10인 원의 면적: {a:.2f}, 원의 둘레: {b:.2f}')

# [문제1] 수학시험
# ([문제, 정답, 배점])
test = (['3+9=?', 12, 3], ['24/4=?', 6, 2], ['99-35=?', 64, 5], ['1-(10+4)=?', -13, 10], ['2의 5제곱은?', 32, 20])
# 반복문 돌면서 test에 저장된 문제를 풀어봅시다
# <1> 문제출력
# <2> 사용자가 정답을 입력합니다 input()함수 활용
# <3> 사용자가 입력한 값이 정답ㄱ과 일치라는지 체크해서 일치하면 해당 점수 배점하세요
# 출력 예시
"""  
정답 개수: 3개
오답 개수: 2개
Total Score: 23점
"""

""" print(test)
for tst in test:
    num = 0
    ans = 0
    no = 0
    print(tst[num])
    z = int(input('정답: '))
    if tst[1] == z:
        # tt = sum(tst[2])
        ans += 1
    else: 
        no += 1
    num += 1
s = f'''
정답 개수: {ans}개
오답 개수: {no}개
'''
print(s) """

trueCnt = 0
falseCnt = 0
jumsu = []
for quiz in test:
    print(quiz[0])
    dap = int(input('답을 입력하세요 >>'))
    if dap == quiz[1]:
        trueCnt += 1
        jumsu.append(quiz[2])   # 맞춘 경우 배점을 jumsu에 저장
    else:
        falseCnt += 1
print(f'''
-------------------------
정답 개수: {trueCnt} 개
오답 개수: {falseCnt} 개
Total Score: {sum(jumsu)} 점
-------------------------
''')