# 1-1 반환하기

# 다음의 함수들을 완성하라. 

# 1-1-1 'Hello World' 리턴(return, 반환)하기. 1점
def helloWorld():
    return -1    # 지우고 재작성하시오.

# 1-1-2 커맨드 입력에 따른 결과값 반환하기. 21점
# T: True
# S: "This is string"
# N: 42
# set: {4, 5, 6}
# dic: {'name': 'python', 'emo': 'happy'}
# li: [1, 2, 3]
# tup: (3, 2, 1)
def retMan(command):
    return -1    # 지우고 재작성하시오.

# -------------------------------------

# 1-2 string convert 기능 만들기 각 4.1 점

# add(s1, s2): s1 과 s2 를 concat 후, 대문자로 바꿔서 반환한다. ex) add('he', 'llo') => 'HELLO'
def add(s1, s2):
    return -1    # 지우고 재작성하시오.

# rev(s): s를 뒤집은 후 소문자로 바꿔 반환한다. ex) rev('oLLeH') => 'hello'
def rev(s):
    return -1    # 지우고 재작성하시오.

# toP(s): s의 길이에 해당하는 만큼 %를 반환한다. ex) toP('hello') => '%%%%%'
def toP(s):
    return -1    # 지우고 재작성하시오.

# 1-3 정수 계산기 만들기

# 다음의 기능을 포함한 정수 계산기를 만들려한다.
# oddOrEven(n): n에 대하여 홀짝 판별
# compute(a, b, sig): a와 b를 sig 연산한다. ex) compute(1, 2, "-") => -1
# jinsu(n, base): 10진수 n을 base에 해당하는 진수로 표현하는 기능

def oddOrEven(n):
    # 1차 목표: 모든 정수에 대하여 홀짝 판별. 총 7.7 점
    # 홀일 때는 'odd', 짝일 때는 'even'을 출력

    return -1    # 지우고 재작성하시오.

def compute(a, b, sig):
    # 1차 목표: + - / * 연산처리. 총 12점 예) compute(1, 2, '+') => 3
    # 2차 목표: 제곱(power), 나머지(mod) 연산처리. 총 6점 예) compute(4, 2, 'power') => 16

    return -1    # 지우고 재작성하시오.

def jinsu(n, base):
    # 1차 목표: base 2, 8, 16 에 대하여 바꾼다. 30점
    # 2차 목표: 0 < base < 17 에 대하여 바꾼다. 30점
    # 11진수 이상일 때: 10: A, 11: B, 12: C, 13: D, 14: E, 15: F
    # return 값의 type은 string 이어야한다.

    return -1    # 지우고 재작성하시오.


# -------------------------------------
# 홀짝 헬프 함수
def ooeHelp():
    print("")
    print("-----oddOrEven-----")
    num = input("판별할 숫자를 입력하세요: ")
    num = int(num)
    print("결과: " + oddOrEven(num))

# 사칙연산 헬프함수
def computeHelp():
    print("")
    print("-----compute-----")
    a = input("첫번째 숫자 입력: ")
    b = input("두번째 숫자 입력: ")
    sig = input("기호 입력: ")
    compute(a, b, sig)

# 진수 헬프 함수
def jinsuHelp():
    print("")
    print("-----jinsu-----")
    num = input("변환시킬 숫자를 입력하세요: ")
    num = int(num)
    base = input("베이스를 입력하세요: ")
    base = int(base)
    print("결과: " + jinsu(num, base))

# 계산기
def calculator():
    while True:
        print("")
        print("---계산기 실행---")
        print("1: 진수, 2: 사칙연산, 0: 종료")
        print("--------------")
        print("")
        sel = input("숫자를 입력하세요: ")
        if sel == "1":
            jinsuHelp()
        elif sel == "2":
            computeHelp()
        elif sel == "3":
            ooeHelp()
        elif sel =="0":
            print("")
            print("계산기 종료.")
            break
        else:
            print("\nerror: 잘못된 입력")

# 다음의 주석을 해제하면 계산기 기능을 실행시킬 수 있다.
# calculator()
