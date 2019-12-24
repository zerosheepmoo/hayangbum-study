# The last Assignment

# 이 과제 이후로는 더 이상 이런 식의 과제는 존재하지 않습니다.
# 이전까지 배웠던 내용으로 무기관리 프로그램을 만들것입니다.
# 다음의 기능을 포함한 프로그램을 만드시오.

import time
import getpass

C_WHITE = "\033[37m"
C_RED = "\033[31m"
C_BLUE = "\033[34m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"

# uploadList(): 무기 목록인 weaponsInput.txt 편집모드로 읽기

def uploadList():
    file = open("ha/weaponsInput.txt", 'r', encoding='UTF8')
    return file

# saveList(): 무기 목록을 커스텀한 네임을 가진 txt 로 출력. .py경로에 export

def saveList(data):
    name = input("파일의 이름을 입력해주세요, con이라고 입력 시 저장하지 않고 콘솔창에만 프린트합니다: ")
    if name == 'con':
        for idx in range(0, len(data)):
            for Didx in range(1, 6):
                print("|",end='')
                print(data[idx][Didx],end='')
            print("|")
    else:
        newFile = open("{0}.txt".format(name), "w")
        for idx in range(0, len(data)):
            for Didx in range(1, 6):
                newFile.write("|")
                newFile.write(data[idx][Didx])
            newFile.write("|\n")

# 무기목록 입/출력 예시
# |무기종류|무기이름|상품코드|가격|비고|
# |검|숏소드|ssd2019121400031|3,400 G||
# ....

# 편집

# searchID(id: string): 무기(id를 포함하는 상품코드를 갖고 있는 무기의 리스트 출력) 검색

def searchID(data, id):
    i=0
    j=len(data)-1
    return bina_rec_help(data, id, i, j)

def bina_rec_help(lst, tar, i, j):
    if i<j:
        mid=(i+j)//2
        if lst[mid][3]==tar:
            return mid
        elif mid==i or mid==j:
            if lst[i][3]==tar:
                return i
            elif lst[j][3]==tar:
                return j
            else:
                return -1
        else:
            if lst[mid][3]>tar:
                return bina_rec_help(lst, tar, i, mid-1)
            else:
                return bina_rec_help(lst, tar, mid+1, j)
    elif i==j and lst[i][3]==tar:
        return i
    else:
        return -1


# searchG(more: number || false, less: number || false, equal: int || false: 가격(이상, 이하, 같을 때), false 일땐, 해당 필터링 X
# editG(id: string, G: number): id와 상품코드랑 일치하는 무기 가격 수정 
# weaponAdd(type: string, name: string, id: number, G: number, etc?: string ): 지금 편집하고 있는 리스트에 대해 추가 (etc는 optional)
# weaponDelete(id: number): 해당하는 id를 가진 무기를 리스트에서 삭제
# weaponsDelete(name: string): 해당하는 name을 가진 무기들을 리스트에서 삭제

# 위의 기능을 포함한 프로그램을 자유롭게 구현하시오.
# □  ■

def sortData(data):
    newData=[]
    for idx in range(0, len(data)):
        newData.append(data[idx].split('|'))

    for i in range(len(newData), 0, -1):
        max = 0 # 가장 큰 원소의 인덱스
        for j in range(0, i):
            if newData[j][3] > newData[max][3]:
                max = j
        newData[max], newData[j] = newData[j], newData[max] # 자리 바꿈

    return newData

def manangeWeapon():
    print(("□ "*50+'\n')*3)
    print("Accessing...")
    for i in range(0, 3):
        time.sleep(1)
        print("□ "*50)
    time.sleep(1)
    print(C_BLUE+"USER: "+getpass.getuser())
    time.sleep(1)
    print("QUALIFIDING BY FBI SECURED NETWORK...")
    time.sleep(1.5)
    print(C_GREEN+"A C C E S S    G R A N T E D")
    print(C_WHITE)
    time.sleep(1)

    com_dic={'0':'exit','L':'Load the list from Secured storage. 1~6 commands need to pre-run this', '1':'print(save) the list', '2i':'searching_by ID', '2g':'searching_by Gold', '3':'edit Gold info', '4':'Add a new weapon', '5':'Delete a weapon', '6':'Delete some weapons(by ID)'}
    com_key=list(com_dic.keys())
    com_des=list(com_dic.values())
    while True:
        print("")
        print("===== WELCOME TO WEAPONS CONTROL SYSTEM =====")
        print("you can use the following commands.")
        print("----------------------")
        print("command_number : command_descriptions")
        
        i=0
        while i < len(com_dic):
            print(com_key[i],":", com_des[i])
            i+=1

        print("----------------------")
        print("")
        sel = input("숫자를 입력하세요: ")

        if sel =="":
            continue
        elif sel =="0":
            print("Good bye, commander")
            break
        elif sel =="L":
            file = uploadList()
            data = file.readlines()

            #print(data)#raw-data 확인용
            for idx in range(len(data)-1, -1, -1):
                if data[idx][0]=='#':
                    del data[idx]
            #print(data)#주석삭제 확인용
            
            #print(data)#raw-data 확인용
            data = sortData(data)
            #print(data)#sorted-data 확인용

            input("무기리스트가 성공적으로 로드되었습니다. 아무 키나 눌러 계속하세요")
        elif sel =="1":
            saveList(data)
        elif sel == '2i':
            print("--------SEARCHING by ID")
            id = input("\n원하는 무기의 ID를 입력해주세요: ")
            result = searchID(data, id)
            
            if result==-1:
                input("원하는 무기를 찾을 수 없습니다. 다시 시도해주세요.")
            else:
                print("요청하신 무기 정보는 다음과 같습니다:")
                print("무기종류: ",data[result][1])
                print("무기이름: ",data[result][2])
                print("무기코드: ",data[result][3])
                print("무기가격: ",data[result][4])
                print("세부사항: ",data[result][5])
                input("\n계속하려면 아무 키나 눌러주세요(홈화면으로 나가집니다)")
        else:
            input("\nerror: 예약된 명령어가 아닙니다. 아무 키나 누른 후 다시 시도해주세요")

manangeWeapon()

##중간기록용
##L 명령어를 통해 웨폰리스트 데이터 입력, 주석 삭제, 정렬 완료 시
##[[무기1],[무기2]]식의 이중리스트 형태가 됨.
##각각의 [무기] 리스트들은 ['','종류','이름','코드','가격','비고','']꼴임. 각각 양 끝에 공백이 있음에 유의