# 리스트 요소 정렬하기 : 리스트의 sort()함수 활용
#                     sorted() 내장함수
score = [65, 68, 82, 43, 76, 100]
print(score)    # [65, 68, 82, 43, 76, 100]
score.sort()    # 오름차순 정렬, 원본이 정렬된다
print(score)    # [43, 65, 68, 76, 82, 100]

score.sort(reverse = True)  # 내림차순
print(score)    # [100, 82, 76, 68, 65, 43]
print('*** sorded() 사용 시 *******************')
nums = [6, 3, 2, 7, 1, 0]
print(nums) # [6, 3, 2, 7, 1, 0]
# sort() : 원본이 정렬됨
# sorted() : 정렬하되 원본 리스트를 변경하지 않는다
order_nums = sorted(nums)
print(f'order_nums: {order_nums}')  # order_nums: [0, 1, 2, 3, 6, 7]
print(f'nums: {nums}')  # nums: [6, 3, 2, 7, 1, 0]

# 중첩 리스트: 리스트 안에 또 다른 리스트가 들어있는 구조
nested = [[1, 2], [3, 4], [5, 6]]   # 3행 2열의 2차원 리스트
# 2차원 리스트
print(nested)
# 중첩 리스트 + enumerate()활용해 출력해보자
for row_idx, row in enumerate(nested):
    # print(f'row[{row_idx}]: {row}')  #row: 1차원 리스트 => vector
    for col_idx, col in enumerate(row):
        print(col, end = ' ')
    print()

matrix = [
    [3, 4, 5],
    [1, 2, 3],
    [7, 8, 9]
]
# 3행, 3열
# [1] 각 행의 합을 구해 출력하세요
# 0 번째 행의 합 = 12
# 1 번째 행의 합 = 6
# 2 번째 행의 합 = 24