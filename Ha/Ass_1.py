def helloWorld():
    return "Hello World"

def retMan(command):
    com = ["T", "S", "N", "set", "dic", "li", "tup"]
    ans = [True, "This is string", 42, {4,5,6},{'name': 'python', 'emo': 'happy'}, [1,2,3], (3,2,1)]
    i=0
    while i < 7:
        if com[i]==command:
            return ans[i]
        else:
            i+=1

def add(s1, s2):
    return (s1+s2).upper()

def rev(s):
    return s[::-1].lower()

def toP(s):
    return "%"*len(s)

def oddOrEven(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

def compute(a, b, sig):
    if sig=="+":
        return a+b
    elif sig=="-":
        return a-b
    elif sig=="*":
        return a*b
    elif sig=="/":
        return a/b
    elif sig=="power":
        return a**b
    elif sig=="mod":
        return a%b

def jinsu(n, base):
    j_array=""
    while n>=base:
        if(n%base==10):
           j_array+='A'
        elif(n%base==11):
            j_array+='B'
        elif(n%base==12):
            j_array+='C'
        elif(n%base==13):
            j_array+='D'
        elif(n%base==14):
            j_array+='E'
        elif(n%base==15):
            j_array+='F'
        else:
            j_array+=str(n%base)
        n=n//base
    if n>=10:
        if(n%base==10):
           j_array+='A'
        elif(n%base==11):
            j_array+='B'
        elif(n%base==12):
            j_array+='C'
        elif(n%base==13):
            j_array+='D'
        elif(n%base==14):
            j_array+='E'
        elif(n%base==15):
            j_array+='F'
    else:
        j_array+=str(n)

    return j_array[::-1]