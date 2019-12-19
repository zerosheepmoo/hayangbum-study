from Ass_3 import fibo, fibo_rec, palin, palin_rec, bina, bina_rec, oliveYang, sora, decre_creator

#pylint: disable=unused-variable
# 채점 파일입니다.

C_WHITE = "\033[37m"
C_RED = "\033[31m"
C_BLUE = "\033[34m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"

passed = 0
failed = 9

print(C_YELLOW+"간이 테스트입니다. 통과했어도 instruction에 따르지 못했으면 점수는 상이할 수 있습니다.")

# 3-1
if fibo(0) != [1] or fibo(1) != [1, 1] or fibo(7) != [1,1,2,3,5,8,13,21]:
    print(C_RED+"fibo() 실패!")
else:
    print(C_GREEN+"fibo() 통과!")
    passed+=1
    failed-=1

if palin('ef') != False or palin('helleh') != True or palin('') != False:
    print(C_RED+"palin() 실패!")
else:
    print(C_GREEN+"palin() 통과!")
    passed+=1
    failed-=1

if bina([1,2,3,5,6], 3) == 2 and bina([1,3,5,6,7], 4) == -1:
    print(C_GREEN+"bina() 통과!")
    passed+=1
    failed-=1
else:
    print(C_RED + "bina() 실패!")

# 3-2
if fibo_rec(0) != [1] or fibo_rec(1) != [1, 1] or fibo_rec(7) != [1,1,2,3,5,8,13,21]:
    print(C_RED+"fibo_rec() 실패!")
else:
    print(C_GREEN+"fibo_rec() 통과!")
    passed+=1
    failed-=1

if palin_rec('ef') != False or palin_rec('helleh') != True or palin_rec('') != False:
    print(C_RED+"palin_rec() 실패!")
else:
    print(C_GREEN+"palin_rec() 통과!")
    passed+=1
    failed-=1

if bina_rec([1,2,3,5,6], 3) == 2 and bina_rec([1,3,5,6,7], 4) == -1:
    print(C_GREEN+"bina_rec() 통과!")
    passed+=1
    failed-=1
else:
    print(C_RED + "bina_rec() 실패!"+C_WHITE)

# 3-3

if sora('피자', '먹어') != True or sora('피자', '친구를 줘') != False or sora('벌레', '친구를 줘') != True:
    print(C_RED + "sora() 실패!")
else:
    print(C_GREEN+"sora() 통과!")
    passed+=1
    failed-=1

if oliveYang('pizza', 'heelo', fa='e') != -1:
    print(C_BLUE+"oliveYang() 채점 불가")
    failed-=1
else:
    print(C_RED + "oliveYang() 미구현!")

f = decre_creator(42)
if f(1) == 41:
    print(C_GREEN+"decre_creator() 통과!")
    passed+=1
    failed-=1
else:
    print(C_RED + "decre_creator() 실패!")

print()
print(C_GREEN+"통과: "+ str(passed))
print(C_RED+"실패: "+ str(failed))
print(C_WHITE)

