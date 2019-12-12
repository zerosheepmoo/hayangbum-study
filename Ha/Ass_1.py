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

# 다음의 기능을 포함한 정수 계산기를 만들려한다.
# oddOrEven(n): n에 대하여 홀짝 판별
# compute(a, b, sig): a와 b를 sig 연산한다. ex) compute(1, 2, "-") => -1
# jinsu(n, base): 10진수 n을 base에 해당하는 진수로 표현하는 기능

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
   jinsu_cal(j_array, n, base)
   return j_array[::-1]

def jinsu_cal(j_array, n, base):
    if n<base:
        j_array+="{0}".format(n)
    else:
        j_array+=hex(n%base)[2:]
        jinsu_cal(j_array, n//base, base)