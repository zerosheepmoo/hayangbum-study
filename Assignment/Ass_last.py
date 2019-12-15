# The last Assignment

# 이 과제 이후로는 더 이상 이런 식의 과제는 존재하지 않습니다.
# 이전까지 배웠던 내용으로 무기관리 프로그램을 만들것입니다.
# 다음의 기능을 포함한 프로그램을 만드시오.



# uploadList(): 무기 목록인 weaponsInput.txt 편집모드로 읽기
# saveList(): 무기 목록을 커스텀한 네임을 가진 txt 로 출력. .py경로에 export

# 무기목록 입/출력 예시
# | 무기종류 | 무기이름 | 상품코드 | 가격 | 비고 |
# | 검 | 숏소드 | ssd2019121400031 | 3,400 G | |
# ....

# 편집

# searchID(id: string): 무기(id를 포함하는 상품코드를 갖고 있는 무기의 리스트 출력) 검색
# searchG(more: number | false, less: number | false, equal: int | false: 가격(이상, 이하, 같을 때), false 일땐, 해당 필터링 X
# editG(id: string, G: number): id와 상품코드랑 일치하는 무기 가격 수정 
# weaponAdd(type: string, name: string, id: number, G: number, etc?: string ): 지금 편집하고 있는 리스트에 대해 추가 (etc는 optional)
# weaponDelete(id: number): 해당하는 id를 가진 무기를 리스트에서 삭제
# weaponsDelete(name: string): 해당하는 name을 가진 무기들을 리스트에서 삭제

# 위의 기능을 포함한 프로그램을 자유롭게 구현하시오.

def manangeWeapon():
    while True:
        print("")
        print("---무기 관리 시스템---")
        print("0: 종료")
        print("--------------")
        print("")
        sel = input("숫자를 입력하세요: ")
        if sel =="":
            continue
        elif sel =="0":
            print("")
            print("무기 관리 시스템 종료.")
            break
        else:
            print("\nerror: 잘못된 입력")

manangeWeapon()