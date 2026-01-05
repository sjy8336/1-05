# help(list)
""" 
# 자료구조 : list, tuple, dict, set
list : 순서를 기억. 인덱스로 관리. 데이터 변경 가능(mutable)
tuple : 데이터 변경 불가능(immutable)
dict : 인덱스로 관리하는 것이 아니라 key값과 value 값을 매핑하여 관리
        key 값은 중복되어선 안된다
set : 데이터 중복을 허용하지 않음

[1] list
- 인덱스로 관리
- 순서 있음
- 데이터 중복 허용
- 저장되는 요소들이 타입이 같을 필요는 없음
"""
list1 = []  # 빈 리스트
list2 = [1, 2, 3, 4, 5]     # 정수 리스트
list3 = ['hello', 'hi', '안녕']     # 문자 리스트
list4 = [1, 'bye', 3.14, True]  # 혼합 리스트
# 리스트의 크기 확인 : len()함수
print((list1), len(list1))
print((list2), len(list2))
print((list3), len(list3))
print((list4), len(list4))

print(type(list4))  # <class 'list'>

print('list4[0]=', list4[0])    # 1
print('lsit4[3]=', list4[3])    # True
# print('lsit4[4]=', list4[4])    # IndexError: list index out of range

print('-'*30)
# for 변수 in 리스트:
#   실행문
# 리스트에 저장된 요소들이 순차적으로 변수에 할당됨
# list4에 저장된 요소들을 반복문 이용해 모두 출력해보세요
for value in list4:
    print(value, end = ', ')
print()

lst1=[]
lst2=list()    # list() 함수 이용 빈 리스트 생성
lst3 = list((10, 20, 30))   # 튜플을 리스트로 생성

print(lst1)
print(lst2)
print(lst3) # [10, 20, 30]

# range()함수 이용해서 리스트 생성
lst4 = list(range(11, 21))
print(lst4) # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 문자열 리스트
lst5 = list('hello Python')
print(lst5) # ['h', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']

# [1] 1부터 30까지 정수 중 홀수 요소를 갖는 odd_list 라는 리스트를 생성하세요
#     for 루프 이용해 odd_list에 저장된 값을 모두 출력하세요

# [1]
""" odd_list = list(range(1, 31))
for value in odd_list:
    print(value, end = ', ')
print() """

odd_list = [i for i in range(1, 31, 2)]    # comprehension / range(시작, 끝, 증가치)
print(odd_list)

odd_list2 = []
for j in range(1, 31):
    if j % 2 == 1:
        odd_list2.append(j)  # odd_list2에 추가
print(odd_list2)

total = 0
for value in odd_list:
    print(value, end= ', ')
    total += value # 누적 합계
print()
print(f'1 ~ 30 사이 홀수들의 합계: {total}') # 225
print(sum(odd_list))  # 225

# [2] 'Korea', 'Japan', 'India', 'France'를 저장하는 nations라는 리스트 생성.
#     리스트의 크기 출려하고 for루프 이용해 모두 출력

nations = ['Korea', 'Japan', 'India', 'France']

for n in nations:
    print(n)
print('-------------------------')

# [3] nations 리스트에 저장된 첫 번째 요소값만 출력

print(nations[0])   # 양수 인덱스
print('-------------------------')

# [4] natins 리스테 저장된 마지막 요소값만 출력

print(nations[3])
print(nations[len(nations)-1])  # -1 +len(nations) : 마지막 요소의 인덱스
print('-------------------------')

# 음수 인덱스 : -1, -2
print(nations[-1])  # France
print(nations[-2])  # India
print(nations[-3])  # Japan

lst6 = [10, 20, 30, 'Hello', 'Python', False]
print('*'*30)
print(lst6)
# 리스트 slicing : 특정 범위 내 요소들을 추출할 때 슬라이스를 허용
# 리스트명[start : end : step] : 인덱스 start 부터 end-1 까지 추출
print(lst6[2 : 5])  # [30, 'Hello', 'Python']
print(lst6[3 : 6])  # ['Hello', 'Python', False]
print(lst6[3:])   # ['Hello', 'Python', False] 3에서 시작해서 끝까지 슬라이싱
print(lst6[0:3])  # [10, 20, 30]
print(lst6[:3])  # [10, 20, 30]
print(lst6[:])  
lstCopy = lst6[:]   # 복사본을 반환
print(f'lst6Copy: {lstCopy}')
print(f'lst6: {lst6}')
# lstCopy의 뒤에서 3번째 요소의 값을 "안녕" 으로 변경해보세요
lstCopy[-3] = "안녕"
print('----------------------------')
print(lstCopy)  # [10, 20, 30, '안녕', 'Python', False]
print(f'lst6: {lst6}')

jumin = '030412-1234567'
jumin_list = list(jumin)
print(jumin_list)   # ['0', '3', '0', '4', '1', '2', '-', '1', '2', '3', '4', '5', '6', '7'] 
# 문자열은 기본적으로 리스트임
# [1] jumin 에서 생년월일을 추출하여 출력하기 030412    03년 4월 12일생
""" print(f'{jumin[:6]}')
print(f'{jumin[:2]}년 {jumin[2:4]}월 {jumin[4:6]}일생') """
print('----------------------------')
birth = jumin[:6]
print(birth)
print('%s년 %s월 %s일생' %(jumin[:2], jumin[2:4], jumin[4:6]))
print('%s년 %s월 %s일생' %(jumin[:2], jumin[3], jumin[4:6]))
print('----------------------------')

# [2] 주민번호 뒷자리를 추출하여 출력하세요 1234567
print(jumin[7:])
print(f'주민번호 뒷자리={jumin[-7:]}')  # 주민번호 뒷자리=1234567
print('----------------------------')

# [3] 주민번호에서 짝수 위치 문자열 출력하세요
print(jumin)
# 리스트[start:end:step]
print(jumin[::2])  # 001-246

# [4] 주민번호에서 홀수 위치 문자열 출력하세요
print(jumin[1::2])

# [5] 주민번호를 역순으로 출력하세요
print(jumin[::-1])  # 7654321-214030

# jumin의 인덱스는 0 ~ 13
# print('jumin[20]=', jumin[20])  # IndexError: string index out of range

# slicing 사용 시 인덱스 초과해도 오류가 나지 않음
print('jumin[:20] : ', jumin[:20])  # jumin[:20] :  030412-1234567

# 음수 인덱스로 슬라이싱
nums = [10, 20, 30, 40, 50]
# 30, 40을 추출하되 음수 인덱스 이용하세요
print(nums[-3:-1])
print(nums[-3:])