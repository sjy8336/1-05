# [1] mm 단위 값을 매개변수로 받으면
#   cm와 m, inch 로 변환하여 list에 담아 반환하는 함수 구성 후 호출
# 함수명: convertUnit1(mm)
# mm 인치 변환 => 0.03937

# [1] - 내가 한거
""" def convertUnit1(mm):
    cm = mm * 10
    inch = mm * 0.03937
    lst = [mm, cm, inch]
    print(lst)
convertUnit1(10)
print('--------------------------') """

# [2] [1]번 반환값을 tuple로 반환하는 함수도 구성하세요
# 함수명: convertUnit2(mm)

# [2]
def convertUnit2(mm):
    result = convertUnit1(mm)   # [1]번 함수 재사용
    return result


# [3] 상품명, 정가, 할인율을 매개변수로 받아
#   해당 상품의 정보를 아래와 같이 출력하는 함수를 구성하세요
# 함수명: discount(pname, price, rate)
# 상품명: 배추
# 정  가: 5000원
# 할인율: 20%
# 할인가: 4000원

# [3]
def discount(pname, price, rate):
    s = f'''
    상품명: {pname}
    정  가: {price:,}원
    할인률: {rate * 100:.0f}%
    할인가: {price - price * rate:,}원
    '''
    print(s)
p = discount('배추', 5000, 0.2)
print('--------------------------')

# [4] 더하기 수행하는 함수 add(a, b)
# 빼기 수행하는 함수 minus(a, b)
# 곱하기 수행하는 함수 multiply(a, b)
# 나누기 수행하는 함수 divide(a, b)
# 위 4개의 함수를 구성하세요
# 그런뒤 calculate()함수를 구성하고
# 정수1, 정수2, 연산자(+, -, *, /) 3개 값을 사용자로부터
# 입력받은 뒤 연산자에 따라 다르게 연산하는 함수를 호출하여
# 수식과 함께 출력하세요

# [4]
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate():
    x = int(input('정수 1을 입력해주세요 >>>'))
    y = int(input('정수 2를 입력해주세요 >>>'))
    z = (input('연산자를 입력해주세요 >>>'))
    if z == '+':
        plus = add(x, y)
        print(f'{x}+{y}={plus}')
    elif z == '-':
        min = minus(x, y)
        print(f'{x}-{y}={min}')
    elif z == '*':
        mult = multiply(x, y)
        print(f'{x}*{y}={mult}')
    elif z == '/' :
        divi = divide(x, y)
        print(f'{x}/{y}={divi:.2f}')
    else:
        print('잘못 입력된 연산자입니다.')
calculate()
