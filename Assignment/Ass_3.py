import time

#pylint: disable=unused-variable


# 3-1 함수들
# 다음의 함수들을 만드시오
# 수동 채점 합니다

# 3-1-0 예제
# factorial(n)
# 함수를 반복하여 콜하는 일 없이 만들기

def factorial(n):
    if n == 0:
        return 1

    res = 1
    for i in range(1, n+1):
        res *= i
    return res

# 3-1-1
# 피보나치 수열을 리턴하는 함수 만들기, 반복 X
# fibo(n), n은 번째항
# ex) fibo(4) => [1, 1, 2, 3, 5]
# ex2) fibo(0) => [1]


def fibo(n):
    pass

# 3-1-2
# 회문 검사하기, 반복 X
# palin(str)
# ex) palin('helleh') => True
# ex2) palin('ef') => False
# ex3) palin('') => False


def palin(n):
    pass    # 지우고 수정하세요.

# 3-1-3
# 이진탐색, 있으면 index, 없으면 -1 출력
# bina(lst, tar)
# ex) bina([1,2,4,5], 4) => 2
# ex2) bina([1,3,5,6], 4) => -1


def bina(lst, tar):
    pass

# ---------------------------------

# 3-2 리커시브 함수들
# 다음의 함수들을 만드시오

# 3-2-0 예제
# factorial(n)
# 함수를 반복하여 콜하기


def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n-1)

# 3-2-1
# 피보나치 수열 리턴, 반복 O
# 3-1-1과 동일한 결과값


def fibo_rec(n):
    pass    # 지우고 수정하세요.

# 3-2-2
# 회문, 반복 O, 3-1-2와 동일한 결과값


def palin_rec(str):
    pass    # 지우고 수정하세요.

# 3-2-3
# 이진탐색, 반복 O, 3-1-3 과 동일한 결과값


def bina_rec(lst, tar):
    pass    # 지우고 수정하세요.

# -------------------------

# 3-3 함수들 어펜드

# 3-3-1 마법의 소라고동
# 조건 `in` 키워드를 사용할 것
# thing 가능 목록 = ['피자', '햄버거', '사과', '벌레']
# act 가능 목록 = ['먹어', '친구를 줘']
# thing 이 '벌레'거나 act가 '친구를 줘'면 print('안돼.')와 함께 False를 return
# 만약 thing이 '벌레' 면서 act가 '친구를 줘'면 print('돼.') 와 함께 True
# 나머지 True와 print('그래.')


def sora(thing, act):
    print('소라고동 님, ' + thing + '을 ' + act + '도 될까요?')
    time.sleep(1)

    # 이 아래부터 지우고 다시 쓰시오.
    if thing == "벌레" and act == "친구를 줘":
        print("돼.")
    elif thing == "":
        print('그래.')
        return True
    else:
        print("안돼.")
        return False

# 3-3-2 안녕하세요, 올리브양입니다.

# 예시의 형태를 만족하는 함수를 구현하시오.

# 형태: oliveYang(kind, *arguemnts, **keywords)
# ex) oliveYang('피자', '꽥', '꽥꽥꽥', shopkeeper="Yang", client="Jun")
# => --혹시, 피자 있나요?
# => --죄송합니다. 재고가 다 나갔네요.
# => 꽥
# => 꽥꽥꽥
# => shopkeeper: Yang
# => client: June

# 다른 비슷한 형식 함수 ex) 치즈샵 예시

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# 실행
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# 결과값
# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch

# -------구현하기--------
def oliveYang(kind, *arguments, **keywords):
    return -1 # 지우고 작성.
# ---------------------

# 3-3-3 람다

# n에 대하여 x 만큼 감소하는 함수를 리턴하는 함수를 람다식으로 만들어보자.
# decre_creator(n)
# 조건 lambda 사용 

# 비슷한 예시)

def incre_creator(n):
    return lambda x: x + n

func = incre_creator(42)
func(0) # 42 반환
func(1) # 43 반환

def decre_creator(n):
    return lambda x: -1