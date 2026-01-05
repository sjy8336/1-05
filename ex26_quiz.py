# [문제 1]
work = ['Cleaning', 'Shopping', 'Study', 'Walking', 'Testing']
print(work)
""" print('오늘 할 일:', work[:])
print('마무리한 일:', work[0])
for i in work:
    work.pop(0)
    print('남은 일', work[:])
    print('마무리한 일:', work[0]) """
print('오늘 할 일:', work)
""" for w in work:
    print('마무리 한 일:', work[0])
    work.pop(0)
    # work.remove(w)  # 삭제 처리
    if len(work) > 0:
        print('남은 일:', work)
print('할 일 끝~~~~') """
for _ in range(len(work)):  #range(len(work)) => 5번 확실하게 돌라는 뜻
    print('마무리 한 일', work[0])
    work.pop(0)
    if (len(work) > 0):
        print('남은 일:', work)
print('할 일 끝!!!')

print('*'*30)
# [문제 2]
title = ['국어', '영어', '수학', '물리', '화학', '한국사']
score = [55, 35, 40, 70, 65, 30]
# tip) enumerate() 함수 활용
"""  
enumerate(iterable, start=0)
- iterable : 리스트/튜플/문자열 등 반복 가능한 객체
- start : 인덱스를 시작할 번호(기본값:0)
enumerate()는 "index + 값" 을 한 번에 받고자 할 때 사용.
"""
nums = [10, 20, 30]
# for in 루프 이용 => 값만 출력
for n in nums:
    print(n)

for idx, value in enumerate(nums):
    print(f'{idx} : {value}')
""" 
for ind, sub in enumerate(title):
    for inde, sco in enumerate(score):
        print(f'{sub}: {sco}점')
print('----Test 결과-----------------------')
print(f'합계 점수: {sum(score)}점')
print(f'평균 점수: {sum(score) / 6:.1f}점')
print(f'40점 미만 과목수: {score}점') """

total = sum(score)  #합계 점수
avg = total / len(score)    #mean()
# 과락한 과목수
cnt = 0
fail = []   # 과락한 과목 저장할 리스트
for i, jumsu in enumerate(score):
    print(f'{title[i]} : {jumsu}')
    if jumsu < 40:
        cnt = cnt + 1
        fail.append(title[i])   # 과락 과목 추가
result = '성공 - Pass 축하합니다 합격입니다!'
if cnt > 0 or avg < 60:
    result = '실패 - fail 불합격입니다 ㅠㅠ'
print('----성적 결과-----------------------')
print(f'합계 점수: {total}점')
print(f'평균 점수: {avg:.1f}점')
print(f'40점 미만 과목수: {cnt}, 과목명: {fail}')
print(result)

print('*'*30)