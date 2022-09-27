#1/13 = 0.076923076923076923076923076923077

# reslut = 1
# dev = int(input())
# r = 0
# def _dev(a,b,c):
#     aa = True
#     ccc = 0
#     for i in range(0,50):
#         if a < b:
#             if aa and i != 0:
#                 ccc += 1
#             a*=10
#             c*=10
#         elif a >= b:
#             aa = False

#             c += int(a / b)
#             a -= int(b*int(a/b))
#         if a == 0:
#             break
#     return "0."+"0"*ccc+str(c)
# d = (_dev(reslut,dev,r))
# # d = list(str(d))
# # d[0] = "0."
# print(d)
# print("true: ",(reslut/dev))
# print("end")
import copy

reslut = [1]
# dev = list(input())
dev = [1,3,9,4,2,9]
r = 1
# def _dev(a,b,c):

#     for i in range(0,20):
#         if check(a,b)==False:
#             a.append(0)
#             c*=10
#         elif check(a,b)==True:

#             #得乘法
#             # aaaaa = 1
#             # aaaaaaaa = []
#             # for i in range(1,10):
#             #     b_ = copy.deepcopy(b)
#             #     aaaaaaa = copy.deepcopy(mul(b_,[i]))
#             #     aaaaaaa_ = copy.deepcopy(add(aaaaaaa[1],aaaaaaa[0]))
                
#             #     if check(copy.deepcopy(a),copy.deepcopy(aaaaaaa_))==True:
#             #         aaaaa = copy.deepcopy(i)
#             #         aaaaaaaa = copy.deepcopy(aaaaaaa_)
#             #     else:
#             #         break
#             print(a)
#             xxx = _add(a)
#             xxx2 = _add(b)
#             xxc = (xxx - xxx2*int(xxx/xxx2) )
            
#             a = list(map(int,str(xxc)))
#             c += int(xxx/xxx2)
#             cc__ = []
#             # a = cc__
#             # print("0: ",a)
#             # a = remove(a,copy.deepcopy(aaaaaaaa))
#             # cc__ = copy.deepcopy(a)
#             # print("1: ",a,aaaaaaaa)

#             # a = remove_z(cc__)
#             # print("2: ",cc__)
#             print("3: ",a,b,c)
#         if a == [0]:
#             break
#     return c
def _dev(a:list,b:list,c):
    c2 = [1,0]
    a.append(0)
    for i in range(0,200):
        if _add(copy.deepcopy(a))<_add(copy.deepcopy(b)):
            a.append(0)
            c*=10
            c2.append(0)
        elif _add(copy.deepcopy(a))>=_add(copy.deepcopy(b)):

            #得乘法
            aaaaa = 1
            aaaaaaaa = []
            for i in range(1,10):
                b_ = copy.deepcopy(b)
                aaaaaaa = copy.deepcopy(mul(copy.deepcopy(b),[copy.deepcopy(i)]))
                aaaaaaa_ = copy.deepcopy(add(copy.deepcopy(aaaaaaa[0]),copy.deepcopy(aaaaaaa[1])))

                if _add(copy.deepcopy(a))>=_add(copy.deepcopy(aaaaaaa_)):
                    aaaaa = copy.deepcopy(i)
                    aaaaaaaa = copy.deepcopy(aaaaaaa_)
                else:
                    break
            # print(a)
            xxx = _add(a)
            xxx2 = _add(b)
            xxc = (xxx - xxx2*int(xxx/xxx2) )

            yb = copy.deepcopy(a)
            #余数
            print("!!:  ",a,aaaaaaaa)
            #余数
            c3 = remove_z(remove(yb,copy.deepcopy(aaaaaaaa)))

            # a = list(map(int,str(xxc)))
            a = c3
            c += int(xxx/xxx2)
            c2[-1] = aaaaa
            cc__ = []
            # a = cc__
            # print("0: ",a)

            
            # cc__ = copy.deepcopy(a)
            # print("1: ",a,aaaaaaaa)

            # a = remove_z(cc__)
            # print("2: ",cc__)
            print("3: ",a,b,c2,"余数",c3)
        if a == [0] or len(c2) >= 20:
            break
    return c2 ,c
def check(a:list,b:list):
    #判断大小[1,2] < [1,3]
    if len(a) < len(b):
        return False
    elif len(a) > len(b):
        return True
    else:
        c_a = ""
        for i in range(0,len(a)):
            c_a += str(a[i])
        c_b= ""
        for i in range(0,len(b)):
            c_b += str(b[i])
        if int(c_a) >= int(c_b):
            return True
        else:
            return False
    
def check_dev(a:list,b:list):
    #[1,0,0] / [2,0] = [5]
    pass
def mul(a:list,b:list):
#乘法
# [2,0] * [5] = [1,0,0]
    ccc = [0]
    for i in range(len(a) - 1, -1, -1):
        if a[i] * b[0] >= 10:
            ccc.insert(0,int(str(a[i] * b[0])[0]))
            a[i] = int(str(a[i] * b[0])[1])
            # if a[i] >= 10:
            #     c += int(str(a[i])[0])
            #     a[i] = int(str(a[i])[1])
        else:
            a[i] = a[i] * b[0]
            ccc.insert(0,0)
    return a,ccc
def add(a:list,x:list):
    #加法
    c_C = 0
    if len(x) < len(a):
        for i in range(0,len(a)-len(x)):
            x.insert(0,0)
    if len(x) > len(a):
        for i in range(0,len(x)-len(a)):
            a.insert(0,0)
    for i in range(len(a) - 1, -1, -1):
        a[i] += x[i]
        a[i] += c_C
        if a[i] >= 10:
            c_C = int(str(a[i])[0])
            a[i] = int(str(a[i])[1])
        else:
            c_C = 0
        if i == 0 and c_C != 0:
            a.insert(0,c_C)
    
    return a

def remove(a:list,yy:list):
    #减法
    c = 0
    if len(yy) < len(a):
        for i in range(0,len(a)-len(yy)):
            yy.insert(0,0)
    if len(yy) > len(a):
        for i in range(0,len(yy)-len(a)):
            a.insert(0,0)
    for i in range(len(a) - 1, -1, -1):
        a[i] -= c
        if a[i] < yy[i]:
            a[i] = 10+a[i]- yy[i] 
            c = 1
        else:
            c = 0
            a[i] -= yy[i]
    if a.count(0) == len(a):
        a = [0]
    return a
def remove_z(aa:list):

    add = aa
    while len(aa) >= 1 and aa[0] == 0 :
        del aa[0]
    
    return(aa)
def _add(a:list):
    cddd = ""
    for i in a:
        cddd += str(i)
    if cddd == '':
        cddd = '0'
    return int(cddd)
d = (_dev(reslut,dev,r))
c = int(d[1])#0.00007172100
c3 = float(1/_add(copy.deepcopy(dev)))#0.00007172100
d = d[0]

# print("dev: ",dev)
# d = list(str(d))
d[0] = "0."
# print(d)
# d = mul([1,7,5],[3])
# d = copy.deepcopy(add(d[0],d[1]))
# d = remove([4, 1, 0],[3,5,4])
# d = copy.deepcopy(add([4,8,0], [9,2,0]))

print("reslut/dev= ",[1],dev,d,c,c3)
# print("true: ",(reslut/dev))
print("end")
input()
