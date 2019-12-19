def secretCheck(secret):
    NumCheck=False
    CapitalCheck=False
    SmallCheck=False
    SpecialChar=False
    index=0

    while index < len(secret) :
        if ord(secret[index])>=97 and ord(secret[index])<=122:
            SmallCheck=True
            index+=1
            continue
        elif ord(secret[index])>=65 and ord(secret[index])<=90:
            CapitalCheck=True
            index+=1
            continue
        elif ord(secret[index])>=48 and ord(secret[index])<=57:
            NumCheck=True
            index+=1
            continue
        elif ord(secret[index])>=33 and ord(secret[index])<=47:
            SpecialChar=True
            index+=1
            continue
    
    if SmallCheck==True and CapitalCheck == True and NumCheck == True and len(secret)>=10 and SpecialChar==False:
        return True
    else :
        return False

def insSort(inputList):
    resList = []
    count = 0

    index=1
    while index < len(inputList):
        tmp=inputList[index]
        pointer=index-1
        while tmp<inputList[pointer] and pointer>=0:
            inputList[pointer+1]=inputList[pointer]
            pointer-=1
            count+=1
        inputList[pointer+1]=tmp
        index+=1
    resList=inputList

    resObj = {
        "li": resList,
        "count": count
    }
    return resObj

def binSearch(inputList, target):
    idx = -1
    count = 0
    first=0
    last=len(inputList)-1

    while first != last :
        mid=(first+last)//2
        if inputList[mid]==target :
            idx = mid
            count+=1
            break
        elif inputList[mid] > target:
            last=mid-1
            count+=1
            continue
        else:
            first=mid+1
            count+=1
            continue

    resList = [idx, count]
    return resList

def starOutput(line, type):
    result=''
    if type == 'reg':
        line_ct=0
        for line_ct in range(0, line):
            for line_ct in range(0, line):
                result += "*"
            result += "\n"
        return result[0:(line+1)*(line)-1]
    elif type == 'jump':
        line_ct=0
        for line_ct in range(0, line):
            for line_ct in range(0, line-1):
                result += "* "
            result += "*\n"
        return result[0:(2*line)*(line)-1]
    elif type == 'pyramid':
        line_ct=0
        col_ct=0
        sum_line=0
        for i in range(2, line+2):
            sum_line+=i
        if(line>=0):
            for line_ct in range(1, line+1):
                for col_ct in range (0, line_ct):
                    result += "*"
                result += "\n"
            return result[0:sum_line-1]
        else:
            for line_ct in range(line*-1, 0, -1):
                for col_ct in range (0, line_ct):
                    result += "*"
                result += "\n"
            return result[0:sum_line-1]

    elif type == 'dia':
        line_ct=0
        col_ct=0
        if line%2 == 1:
            if(line>=0):
                for line_ct in range(0, line):
                    space_ct=abs((line-line_ct*2)//2)
                    for col_ct in range(0, space_ct):
                        result += " "
                    for col_ct in range(0, line-(space_ct*2)):
                        result += "*"
                    for col_ct in range(0, space_ct):
                        result += " "
                    result += "\n"
                return result[0:(line+1)*(line)-1]
            else :
                line=line*-1
                for line_ct in range(0, line):
                    space_ct=abs((line-line_ct*2)//2)
                    for col_ct in range(0, space_ct):
                        result += "*"
                    for col_ct in range(0, line-(space_ct*2)):
                        result += " "
                    for col_ct in range(0, space_ct):
                        result += "*"
                    result += "\n"
                return result[0:len(result)-1]
        else:
            if(line>0):
                line-=1
                for line_ct in range(0, line//2+1):
                    space_ct=abs((line-line_ct*2)//2)
                    for col_ct in range(0, space_ct):
                        result += " "
                    for col_ct in range(0, line-(space_ct*2)):
                        result += "*"
                    for col_ct in range(0, space_ct):
                        result += " "
                    result += "\n"
                for line_ct in range(line//2, -1, -1):
                    space_ct=abs((line-line_ct*2)//2)
                    for col_ct in range(0, space_ct):
                        result += " "
                    for col_ct in range(0, line-(space_ct*2)):
                        result += "*"
                    for col_ct in range(0, space_ct):
                        result += " "
                    result += "\n"
                return result[0:len(result)-1]
            elif line==0:
                return ""
            else:
                line=line*-1
                line-=1
                for line_ct in range(0, line//2+1):
                    space_ct=abs((line-line_ct*2)//2)
                    for col_ct in range(0, space_ct):
                        result += "*"
                    for col_ct in range(0, line-(space_ct*2)):
                        result += " "
                    for col_ct in range(0, space_ct):
                        result += "*"
                    result += "\n"
                for line_ct in range(line//2, -1, -1):
                    space_ct=abs((line-line_ct*2)//2)
                    for col_ct in range(0, space_ct):
                        result += "*"
                    for col_ct in range(0, line-(space_ct*2)):
                        result += " "
                    for col_ct in range(0, space_ct):
                        result += "*"
                    result += "\n"
                return result[0:len(result)-1]


#def starPrint():
#    print("it's testing time!\n")
#    for line in range(5, 8, 2):
#        print("Line: {0} \n".format(line))
#        print(starOutput(line, 'dia'))
#        print("■"*50)
#
#    print("How about negative number?\n")
#    for line in range(-7, -4, 2):
#        print("Line: {0} \n".format(line))
#        print(starOutput(line, 'dia'))
#        print("■"*50)
#
#    print("now even num!\n")
#    for line in range(4, 7, 2):
#        print("Line: {0} \n".format(line))
#        print(starOutput(line, 'dia'))
#        print("■"*50)
#
#    print("last test! even negative!\n")
#    for line in range(-6, -3, 2):
#        print("Line: {0} \n".format(line))
#        print(starOutput(line, 'dia'))
#        print("■"*50)
#starPrint()