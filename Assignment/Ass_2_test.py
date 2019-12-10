from Ass_2 import secretCheck, insSort, binSearch, starOutput
import random
# 채점 파일입니다.

C_WHITE = "\033[37m"
C_RED = "\033[31m"
C_BLUE = "\033[34m"

res = 200

# secretCheck

def test_sec():
    if secretCheck('0Ab123456') == False:
        if secretCheck('0123456789') == False:
            if secretCheck('abcdefghI') == False:
                if secretCheck('Ab2Fd4HKo5l') == True:
                    if secretCheck('$!fkdksla134B') == False:
                        return True
    return False

if not test_sec():
    res -= 20
    print(C_RED + "secretCheck 실패!")

# insSort

def test_inss():
    for i in range (0, 5):
        l = random.sample(range(1,100), 10)
        if insSort(l)["li"] != sorted(l):
            return False
    l = [2, 3, 1]
    if insSort(l) != {"li": [1,2,3], "count":2}:
        return False
    return True

if not test_inss():
    res -= 40
    print(C_RED + "insSort 실패!")

# binSearch

def test_bin():
    if binSearch([1,2,3,5], 3)[0] != 2 or binSearch([1,2,3,5], 3)[1] > 3:
        return False
    return True

if not test_bin():
    res -= 40
    print(C_RED + "binSearch 실패!")

# starPrint

Ans_1 = "***\n***\n***"
Ans_2 = "* * *\n* * *\n* * *"
Ans_3 = "*\n**\n***\n****"
Ans_4 = "****\n***\n**\n*"
Ans_5 = "*\n*"
Ans_6 = " * \n***\n * "
Ans_7 = "* *\n   \n* *"

if starOutput(3, 'reg') != Ans_1:
    res -= 10
    print(C_RED + "starOutput reg 실패!")

if starOutput(3, 'jump') != Ans_2:
    res -= 20
    print(C_RED + "starOutput jump 실패!")

if starOutput(4, 'pyramid') != Ans_3 or starOutput(-4, 'pyramid') != Ans_4:
    res -= 30
    print(C_RED + "starOutput pyramid 실패!")

if starOutput(2, 'dia') != Ans_5 or starOutput(3, 'dia') != Ans_6 or starOutput(-3, 'dia') != Ans_7:
    res -= 40
    print(C_RED + "starOutput dia 실패!")

res = round(res, 2)
res = str(res)
print(C_BLUE + ("총점: " + res))
print()
print(C_WHITE)