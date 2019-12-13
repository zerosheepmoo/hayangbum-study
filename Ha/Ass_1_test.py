from Ass_1 import helloWorld, retMan, add, rev, toP, oddOrEven, compute, jinsu
# 채점 파일입니다.

C_WHITE = "\033[37m"
C_RED = "\033[31m"
C_BLUE = "\033[34m"

def main():
    res = 120.0
    # helloWorld()
    if helloWorld() != "Hello World":
        res -= 1
        print(C_RED + "helloWorld() 오답!")
    
    # retMan
    if retMan('T') != True:
        res -= 3
        print(C_RED + "retMan('T') 오답!")
    if retMan('S') != "This is string":
        res -= 3
        print(C_RED + "retMan('S') 오답!")
    if retMan('N') != 42:
        res -= 3
        print(C_RED + "retMan('N') 오답!")
    if retMan('set') != {4, 5, 6}:
        res -= 3
        print(C_RED + "retMan('set') 오답!")
    if retMan('dic') != {'name': 'python', 'emo': 'happy'}:
        res -= 3
        print(C_RED + "retMan('dic') 오답!")
    if retMan('li') != [1, 2, 3]:
        res -= 3
        print(C_RED + "retMan('li') 오답!")
    if retMan('tup') != (3, 2, 1):
        res -= 3
        print(C_RED + "retMan('tup') 오답!")
    
    # SC
    if add('he', 'llo') != 'HELLO' or add('Cok', 'e') != 'COKE' or add('Happy set', 'World') != 'HAPPY SETWORLD':
        res -= 4.1
        print(C_RED + "add(s1, s2) 오답!")
    if rev('oLLeh') != 'hello' or rev('ekOC') != 'coke' or rev('dlrowtes yppah') != 'happy setworld':
        res -= 4.1
        print(C_RED + "rev(s1, s2) 오답!")
    if toP('oLLeh') != '%%%%%' or toP('ekOC') != '%%%%' or toP('dlrowtes yppah') != '%%%%%%%%%%%%%%':
        res -= 4.1
        print(C_RED + "toP(s1, s2) 오답!")

    # 정수계산기 - 홀짝
    if oddOrEven(4)!='even' or oddOrEven(331)!= 'odd' or oddOrEven(-39)!= 'odd':
        res -= 7.7
        print(C_RED + "oddOrEven(n) 오답!")
    
    # 정수계산기 - compute
    if compute(4, 5, '+') !=9 or compute(-3, 4, '+') !=1:
        res -=3
        print(C_RED + "compute(a, b, '+') 오답!")
    if compute(4, 5, '-') !=-1 or compute(-3, 4, '-') !=-7:
        res -=3
        print(C_RED + "compute(a, b, '-') 오답!")
    if compute(4, 5, '/') !=0.8 or compute(4, 4, '/') !=1:
        res -=3
        print(C_RED + "compute(a, b, '/') 오답!")
    if compute(4, 5, '*') !=20 or compute(4, 0, '*') !=0:
        res -=3
        print(C_RED + "compute(a, b, '*') 오답!")
    if compute(2, 4, 'power')!= 16:
        res -=3
        print(C_RED + "compute(a, b, 'power') 오답!")
    if compute(4, 5, 'mod') !=4 or compute(4, -3, 'mod') !=-2:
        res -=3
        print(C_RED + "compute(a, b, 'mod') 오답!")
    
    # 정수계산기 - 진수
    if jinsu(13, 2) != '1101' or jinsu(13, 8) != '15' or jinsu(13, 16) != 'D':
        res -=30
        print(C_RED + "jinsu 1차 목표 실패!")
    if jinsu(23, 3) != '212' or jinsu(43, 11) != '3A' or jinsu(50, 7) != '101':
        res -=30
        print(C_RED + "jinsu 2차 목표 실패!")
    res = round(res, 2)
    res = str(res)
    print(C_BLUE + ("총점: " + res))

print()
main()
print(C_WHITE)