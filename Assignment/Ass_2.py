# 2-1
# 비밀번호 검사기. 20 점
# 다음의 조건들에 해당하는 비밀번호면 True, 아니면 False를 반환한다.
# 1. 최소 열 글자 이상
# 2. 대문자, 소문자, 숫자를 최소 하나 씩은 포함.
def secretCheck(secret):
    return -1 # 지우고 재작성하시오.

# 2-2
# Sort and Binary Search

# insertion Sort를 사용하여 list를 정렬 후, 특정 값을 Binary Search 하여,
# 존재하면 그 값의 index를, 아니라면 -1을 반환하는 함수를 완성하라.

# 정렬된 list와 정렬 중 pull이 몇번 이루어졌는지를 count에 할당하여,
# 둘을 아래에 제시된 딕셔너리 형태로 반환하라.
# 40점

# ex) a = [3,2,1]
# 1을 3 왼쪽으로 넣기 위해 2를 a[2]에 할당하고, 3을 a[1]에 할당한다. 2번. 삽입되는 친구는 pull 횟수에 고려하지 않는다.
# [1, 3, 2] 상태에서 3은 1보다 작으므로 pull이 일어나지 않는다. 0번.
# 2는 3 보다 작으므로 3을 a[2]에 할당한다. 1번.
# 총 4번의 pull 횟수가 있게 된다.

def insSort(inputList):
    resList = []
    count = 0
    # ...
    # 이곳에 알고리즘이 들어갑니다.
    # ...
    resObj = {
        "li": resList,
        "count": count
    }
    return resObj

# target과 동일한 값이 inputList에 존재하면 해당 index를, 아니라면 -1을 idx에 할당하고
# 총 몇번 탐색을 하게 되는지를 count에 할당하여 아래에 제시된 리스트 형태로 반환하라.
# 40점

def binSearch(inputList, target):
    targetedList = inputList
    idx = -1
    count = -1
    # ...
    # 이곳에 알고리즘이 들어갑니다.
    # ...
    resList = [idx, count]  # 지우고 재작성하시오.
    return resList

# 2-3 별별별
# 주어진 값에 따라 별을 프린트하는 함수를 완성하시오.
# type 순서대로 10점, 20점, 30점, 40점

# line은 별이 print 되는 줄의 수이다.
# type은 별이 print 되는 규칙의 종류이다.

# type이 'reg' 일 경우 line * line 만큼의 별을 반환한다.
# ex) starOutput(4, 'reg') 인 경우

# ****
# ****
# ****
# ****

# type이 'jump' 일 경우, 'reg'의 경우에서 좌우 별사이 띄어쓰기를 한다.
# ex) starOutput(3, 'jump') 인 경우

# * * *
# * * *
# * * *

# type이 'pyramid' 일 경우, 줄에 있는 별이 하나씩 늘어간다.
# line이 음수인 경우는 'pyramid'일 경우를 상하로 뒤집는다.

# ex) starOutput(3, 'pyramid')

# *
# **
# ***

# ex2) starOutput(-3, 'pyramid')

# ***
# **
# *

# type이 'dia'인 경우 다음과 같은 결과를 반환한다.
# 공백과 * 하나의 칸 너비는 같다고 가정한다.
# ex) starOutput(5, 'dia')
# 첫번째 줄은 '공백' '공백' '별' '공백' '공백'이 출력된 결과다.

#   *
#  *** 
# *****
#  ***
#   *

# ex2) starOutput(4, 'dia')

#  *
# ***
# ***
#  *

# ex3) starOutput(-5, 'dia')

# ** **
# *   *
#      
# *   *
# ** **


def starOutput(line, type):
    return ''

# -------------------------

# 실행시켜보고 싶다면 아래에 각주를 없앨것

# # 정렬

# def sortAndFind():
#     li = [3, 4, 1, 6, 2, 5, 7]
#     sed = insSort(li)
#     res = binSearch(res["li"])
#     print()
#     print(sed)
#     print(res)
#     print()


# # 별 프린트 

# def starPrint():
#     print(starOutput(5, 'reg'))
#     print()
#     print(starOutput(5, 'jump'))
#     print()
#     print(starOutput(5, 'pyramid'))
#     print()
#     print(starOutput(7, 'dia'))
#     print()

# sortAndFind()
# starPrint()