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
    file = open("./ha/weaponsInput.txt", 'r', encoding='UTF-8')
    return file

# saveList(): 무기 목록을 커스텀한 네임을 가진 txt 로 출력. .py경로에 export

def saveList():
    global data
    name = input("파일의 이름을 입력해주세요, con이라고 입력 시 저장하지 않고 콘솔창에만 프린트합니다: ")
    if name == 'con':
        for idx in range(0, len(data)):
            for Didx in range(1, 6):
                print("|",end='')
                print(data[idx][Didx],end='')
            print("|")
    else:
        newFile = open("./Ha/{0}.txt".format(name), "w", encoding='UTF-8')
        newFile.write("# 샵으로 시작하면 주석처리됩니다.\n# |무기종류|무기이름|상품코드|가격|비고|\n# 무기 코드는 최소 15글자 (종류최소2글자, 식별번호 최소 13자)를 준수해야 합니다.\n# 무기 코드에는 특수문자, 공백, 대문자를 쓸 수 없습니다.")
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

def searchID_sim(id):
    global data
    lst=[]
    for idx in range(0, len(data)):
        if id in data[idx][3]:
            lst.append(idx)
    
    return lst

def searchID(id):
    global data
    return bina_rec_help(data, id, 0, len(data)-1)

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
def sort_by_G():
    global data
    newData=data
    for i in range(len(newData), -1, -1):
        max = 0 # 가장 큰 원소의 인덱스
        for j in range(0, i):
            if newData[j][4] > newData[max][4]:
                max = j
        newData[max], newData[j] = newData[j], newData[max] # 자리 바꿈

    return newData

def searchG(more, less, equal):
    global data
    lst=[]
    for idx in range(0, len(data)):
        data[idx][4]=data[idx][4].replace(',','')
        data[idx][4]=data[idx][4].replace('G','')
        data[idx][4]=data[idx][4].replace(' ','')
    lst = sort_by_G()

    if more:
        for idx in range(len(lst)-1, -1, -1):
            if lst[idx][4]<more:
                del lst[idx]
    if less:
        for idx in range(len(lst)-1, -1, -1):
            if lst[idx][4]>less:
                del lst[idx]
    if equal:
        for idx in range(len(lst)-1, -1, -1):
            if lst[idx][4]!=equal:
                del lst[idx]

    return lst

# editG(id: string, G: number): id와 상품코드랑 일치하는 무기 가격 수정 
def convertor(gold):
    gold = list(gold)
    for idx in range(-1, -1*(len(gold))-1, -1):
        if idx%(4)==0 :
            gold.insert(idx+1, ',')
    
    result=''
    for idx in range(0, len(gold)):
        result+=str(gold[idx])

    result+=" G"
    return result


def editG(id, gold):
    global data
    tar = searchID(id)
    ans = input('원래 가격이 {0}인 {1}를 {2}로 바꾸려는 게 맞나요? y를 입력하시면 진행합니다.'.format(data[tar][4], data[tar][2], convertor(gold)+" G"))
    if ans == 'y':
        data[tar][4] = convertor(gold)
    else:
        print('작업을 취소하였습니다.')

# weaponAdd(type: string, name: string, id: number, G: number, etc?: string ): 지금 편집하고 있는 리스트에 대해 추가 (etc는 optional)
def weaponAdd(type, name, id, G, etc):
    global data
    data.insert(len(data), ['', type, name, id, convertor(G), etc, ''])
    print("추가된 무기의 정보는 다음과 같습니다:")
    print("무기종류: ",data[len(data)-1][1])
    print("무기이름: ",data[len(data)-1][2])
    print("무기코드: ",data[len(data)-1][3])
    print("무기가격: ",data[len(data)-1][4])
    print("세부사항: ",data[len(data)-1][5])
    input("\n계속하려면 엔터 키를 눌러주세요(홈화면으로 나가집니다)")

# weaponDelete(id: number): 해당하는 id를 가진 무기를 리스트에서 삭제
def weaponDelete(id):
    global data
    tar=searchID(id)

    print("\n","="*10)
    print("무기종류: ",data[tar][1])
    print("무기이름: ",data[tar][2])
    print("무기코드: ",data[tar][3])
    print("무기가격: ",data[tar][4])
    print("세부사항: ",data[tar][5])

    ans = input("삭제하고자 하는 무기가 다음의 것이 맞나요? 맞다면 y를 입력해주세요.")

    if ans=='y':
        del data[tar]
        print("성공적으로 삭제되었습니다.")
    else:
        print("삭제가 취소되었습니다")

# weaponsDelete(name: string): 해당하는 name을 가진 무기들을 리스트에서 삭제
def weaponsDelete(name):
    global data
    cnt=0

    for idx in range(len(data)-1, -1, -1):
        if data[idx][2]==name:
            del data[idx]
            cnt+=1

    print("총", str(cnt)+"건의","'"+name+"'이름을 가진 모든 무기들을 삭제했습니다.")        

# 위의 기능을 포함한 프로그램을 자유롭게 구현하시오.
# □  ■

def sortData(sig):
    global data
    newData=[]

    if sig=='1':
        for idx in range(0, len(data)):
            newData.append(data[idx].split('|'))
    else:
        newData=data

    for i in range(len(newData), 0, -1):
        max = 0 # 가장 큰 원소의 인덱스
        for j in range(0, i):
            if newData[j][3] > newData[max][3]:
                max = j
        newData[max], newData[j] = newData[j], newData[max] # 자리 바꿈

    data=newData

def manangeWeapon():
    global data
    print(("□ "*50+'\n')*3)
    print("Accessing...")
    time.sleep(1)
    print("\r"+"□ "*50, end='')
    time.sleep(1)
    print("\r"+"■ "*20+"□ "*30, end='')
    time.sleep(1)
    print("\r"+"■ "*50)
    time.sleep(1)
    print(C_BLUE+"USER: "+getpass.getuser())
    time.sleep(1)
    print("QUALIFIDING BY FBI SECURED NETWORK...")
    time.sleep(1.5)
    print(C_GREEN+"A C C E S S    G R A N T E D")
    print(C_WHITE)
    time.sleep(1)

    com_dic={'0':'exit','L':'Load the list from Secured storage. 1~6 commands need to pre-run this', '1':'print(save) the list', '2i':'searching_by ID', '2g':'searching_by Gold', '3':'edit Gold info', '4':'Add a new weapon', '5':'Delete a weapon(by ID)', '6':'Delete some weapons(by name)'}
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
            sortData('1')
            #print(data)#sorted-data 확인용

            input("무기리스트가 성공적으로 로드되었습니다. 엔터 키를 눌러 계속하세요")
        elif sel =="1":
            saveList()
        elif sel == '2i':
            sortData('')
            print("--------SEARCHING by ID")
            print("\n원하는 무기의 ID를 입력해주세요. -all을 입력하시면 모든 무기의 리스트를 출력합니다")
            print("-f를 입력하시면 무기 탐색 프로세스를 종료하고 홈으로 돌아갑니다.")
            id = input("\nID: ")
            if id=='-all':
                print("모든 무기 리스트를 출력합니다. 한 번에 5개씩 출력됩니다.")
                for idx in range(0, len(data), 5):
                    if(idx+4<len(data)):
                        for Didx in range(idx, idx+5):
                            print(str(Didx+1)+". ["+ str(data[Didx][1])+ "] ["+ str(data[Didx][2])+ "] ["+ str(data[Didx][3])+"]")
                    else:
                        for Didx in range(idx, len(data)):
                            print(str(Didx+1)+". ["+ str(data[Didx][1])+ "] ["+ str(data[Didx][2])+ "] ["+ str(data[Didx][3])+"]")
                input("출력이 끝났습니다. 엔터를 눌러 홈으로 돌아가십시오.")
            elif id=='-f':
                print("홈으로 돌아갑니다.")
                continue
            elif len(id)<13:
                print("입력하신 코드를 포함하는 자료를 모두 찾습니다. 시간이 조금 걸릴 수 있습니다.")
                lst = searchID_sim(id)
                for idx in range(0,len(lst)):
                    print(idx+1,". name: ",data[lst[idx]][2]," code: ",data[lst[idx]][3])
                input("세부정보를 확인하고 싶으시다면, 위 결과를 이용해 2i 서치를 돌려주세요.")
            else:
                result = searchID(id)
                
                if result==-1:
                    input("원하는 무기를 찾을 수 없습니다. 다시 시도해주세요.")
                else:
                    print("\n","-"*50)
                    print("요청하신 무기 정보는 다음과 같습니다:")
                    print("무기종류: ",data[result][1])
                    print("무기이름: ",data[result][2])
                    print("무기코드: ",data[result][3])
                    print("무기가격: ",data[result][4])
                    print("세부사항: ",data[result][5])
                    input("\n계속하려면 엔터 키를 눌러주세요(홈화면으로 나가집니다)")
        elif sel == '2g':
            print("--------SEARCHING by Gold")
            more = input("하한가를 입력해주세요. -f 입력시 하한가는 0G 입니다.")
            if more=='-f':
                more=False
            less = input("상한가를 입력해주세요. -f 입력시 상한가는 미정입니다.")
            if less=='-f':
                less=False
            equal = input("특정가를 입력해주세요. -f 입력시 특정가는 미정입니다.")
            if equal=='-f':
                equal=False

            lst = searchG(more, less, equal)

            print("해당하는 가격대의 무기 정보입니다.")
            for idx in range(0, len(lst)):
                print(idx+1,". name: ",lst[idx][2]," code: ",lst[idx][3])
            input("세부정보를 확인하고 싶으시다면, 위 결과를 이용해 2i 서치를 돌려주세요.")
        elif sel == '3':
            sortData('')
            print("--------EDITING Gold info")
            
            id = input("가격 정보를 수정하고자 하는 상품의 ID를 입력해주세요 : ")
            gold = input("수정하고자 하는 가격을 입력해주세요 : ")
            editG(id, gold)

            input("\n가격 수정이 완료되었습니다. \n계속하시려면 엔터 키를 눌러주세요(홈화면으로 나가집니다)")
        elif sel=='4':
            print("--------ADDING a new Weapon")

            type = input("추가하고자 하는 무기의 종류는 무엇인가요? ex)돌격소총, 샷건, 단검, 논문 ...\n")
            name = input("추가하고자 하는 무기의 이름은 무엇인가요? ex)L85A2, BOSG.12.2, 마체테...\n")
            print(C_BLUE+"\n식별코드는 보통 종류-추가년월일-식별번호 로 이루어집니다. ex)ar2017021400001")
            print(C_WHITE,end='')
            upper = True
            space=True
            spcial = True
            leng=True
            while upper==True or space==True or spcial==True or leng==True:
                upper=False
                space=False
                spcial=False
                leng=False
                id = input("추가하고자 하는 무기의 식별코드(ID)는 무엇인가요? \n")
                if len(id)<15:
                    print(C_RED+"식별코드는 최소 15자(종류 최소 2자+번호 최소 13자)여야 합니다. 다시 시도해주세요.")
                    print(C_WHITE)
                    leng=True
                    continue
                else:
                    for idx in range(0, len(id)):
                        if id[idx].isupper():
                            print(C_RED+"코드 사용의 혼선을 막기 위해 대문자의 사용은 금지되었습니다. 다시 시도해주세요.")
                            print(C_WHITE)
                            upper=True
                            continue
                        elif id[idx].isspace():
                            print(C_RED+"식별 코드에는 공백을 쓸 수 없습니다. 다시 시도해주세요")
                            print(C_WHITE)
                            space=True
                            continue
                        elif ord(id[idx])>=33 and ord(id[idx])<=47:
                            print(C_RED+"식별 코드에는 특수문자를 쓸 수 없습니다. 다시 시도해주세요")
                            print(C_WHITE)
                            spcial=True
                            continue

            gold = input("추가하고자 하는 무기의 가격은 얼마인가요? ,와 G는 생략하고 말해주세요. ex)130000\n")
            print("마지막 단계입니다. 추가하고자 하는 무기에 기록해놓고 싶은 기타사항이 있나요?")
            etc = input("ex)SAS, 5.56x45mm\n")

            weaponAdd(type, name, id, gold, etc)
        elif sel=='5':
            sortData('')
            print("--------DELETING a new Weapon")
            
            print("\n 삭제하고자 하는 무기의 ID를 입력해주세요.")
            print(C_BLUE+"HELP: 2i 메뉴에서 -all 을 입력하시면 모든 무기의 리스트를 보여줍니다."+C_WHITE)
            print("-f를 입력하시면 무기 삭제 프로세스를 종료하고 홈으로 돌아갑니다.")
            
            while True:
                id=input("\nID: ")

                if id=='-f':
                    continue
                elif len(id)<15:
                    print(C_RED+"무기의 ID는 항상 15자 이상입니다. 다시 입력해주세요."+C_WHITE)
                    continue
                else:
                    tar = searchID(id)
                    if tar == -1:
                        print(C_RED+"해당 ID와 일치하는 무기가 존재하지 않습니다. 다시 시도해주세요."+C_WHITE)
                        continue
                    else:
                        weaponDelete(id)
                        break
        elif sel=='6':
            print("--------DELETING some Weapons")

            print("\n 삭제하고자 하는 무기들의 이름을 입력해주세요.")
            print(C_BLUE+"HELP: 2i 메뉴에서 -all 을 입력하시면 모든 무기의 리스트를 보여줍니다."+C_WHITE)
            print("-f를 입력하시면 무기 삭제 프로세스를 종료하고 홈으로 돌아갑니다.")
            name = input("이름: ")

            if name=='-f':
                continue
            else:
                weaponsDelete(name)
        else:
            input("\nerror: 예약된 명령어가 아닙니다. 아무 키나 누른 후 다시 시도해주세요")

data=[]
manangeWeapon()

##중간기록용
##L 명령어를 통해 웨폰리스트 데이터 입력, 주석 삭제, 정렬 완료 시
##[[무기1],[무기2]]식의 이중리스트 형태가 됨.
##각각의 [무기] 리스트들은 ['','종류','이름','코드','가격','비고','']꼴임. 각각 양 끝에 공백이 있음에 유의