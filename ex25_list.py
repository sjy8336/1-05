# list의 주요 함수(메서드)
# [1] 추가 : append()
# [2] 삭제 : 아래 참고
"""  
    pop() : 맨 뒤의 요소부터 제거
    pop(위치) : 특정 인덱스 위치의 요소를 제거
    remove(값) : 특정 값을 제거. 해당 값이 여러 개 있다면 인덱스가 가장 낮은 요소 1개만 삭제
    del 리스트명[인덱스] : 특정 위치의 요소를 제거
    clear() : 리스트의 모든 요소를 제거
"""
lst = [1, 2, 3, 'Good~', 'Nice!!', False, True]
print(lst, len(lst))
# 'Excellent'를 추가 후 lst를 출력
lst.append('Excellent')
print(lst)  # [1, 2, 3, 'Good~', 'Nice!!', False, True, 'Excellent']
lst.insert(3, 'Exvellent!!')    # 특정 인덱스 위치에 삽입
print(lst)
print('-----------------------------------')

# 맨뒤의 Excellent를 삭제하세요
lst.pop()
print(lst)  # [1, 2, 3, 'Exvellent!!', 'Good~', 'Nice!!', False, True]
# 맨앞의 1을 삭제하세요
lst.pop(0)
print(lst)  # [2, 3, 'Exvellent!!', 'Good~', 'Nice!!', False, True]
# False값을 제거하세요
lst.pop(-2)
print(lst)  # [2, 3, 'Exvellent!!', 'Good~', 'Nice!!', True]
# 값으로 제거
lst.remove('Exvellent!!')
print(lst)  # [2, 3, 'Good~', 'Nice!!', True]

del lst[2]
print(lst)  # [2, 3, 'Nice!!', True]
# lst에 저장된 요소 모두 지우세요
lst.clear()
print(lst)
# 수정 처리
for i in range(1, 5):
    lst.append("Hi "+str(i))
print(lst)  # ['Hi1', 'Hi2', 'Hi3', 'Hi4']
# 'Hi 3'을 'Hello 3'으로 수정하세요
lst[2] = "Hello 3"
print(lst)  # ['Hi1', 'Hi2', 'Hello 3', 'Hi4']

idx = lst.index('Hello 3')
print(idx)  # 2 / Hello 3이란 문자열이 위치한 곳의 인덱스 번호를 반환함. 찾는 값이 없으면 오류.
# 'Hi 2'를 'Python 2'로 수정하기
lst[lst.index('Hi 2')] = 'Python 2'
print(lst)  # ['Hi 1', 'Python 2', 'Hello 3', 'Hi 4']

arr = [1, 2, 3, 4]
copy = arr
# arr이 가리키는 리스트의 주소값을 copy에게 할당하는 것
# arr과 copy는 서로 같은 주소값을 갖는다
print(id(copy)) # 1932771223040
print(id(arr))  # 1932771223040
print('-----------------------------------')
# 슬라이싱 이용해서 사본 copy2를 만드세요
copy2 = arr[:]  # 같은 객체를 참조하는 것이 아닌 복사본 객체를 새로 copy2에 할당
print(id(arr))  # 1932771223040
print(id(copy2))  #1932770833472
print(f'copy = {copy}')
print(f'copy2 = {copy2}')
print('-----------------------------------')

# copy의 마지막 요소값을 40으로 수정하세요
copy[-1] = 40
print(f'copy = {copy}') # copy = [1, 2, 3, 40]
print(f'arr = {arr}')  # [1, 2, 3, 40]

# copy2의 위치 2인 곳의 값을 30으로 수정
copy2[2] = 30
print(f'copy2 = {copy2}')   # copy2 = [1, 2, 30, 4]
print(f'arr = {arr}')   # arr = [1, 2, 3, 40]