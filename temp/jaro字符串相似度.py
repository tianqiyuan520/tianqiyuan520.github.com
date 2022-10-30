##jaro字符串相似度
strA = 'faremviel'
strB = 'farmville'

def add(stringA:str,stringB:str) -> str:
    '''添加字符串长度'''
    while len(stringA) < len(stringB):
        stringA += ' '
    while len(stringA) > len(stringB):
        stringB += ' '
    return stringA,stringB

def cal(stringA:str,stringB:str) -> int:
    '''计算字符可位移的个数(<=可位移)'''
    return int((len(stringB)/2 -1) if len(stringA) < len(stringB) else ( (len(stringA)/2 -1) if len(stringA) > len(stringB) else (len(stringA)/2 -1) ))

def main(stringA:str,stringB:str,c:int) -> str:
    '''循环判断'''
    s1 = add(stringA,stringB) 
    s2 = s1[1] 
    s1 = s1[0] 
    m = 0#匹配的字符个数
    t=0#换位数
    index = []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            index.append([s1[i],i])
            m+=1
        else:
            if i>=c:
                #判断位移
                for j in range(-c+1,c+1):
                    if i+j>=0 and i+j<=len(s2)-1 and s1[i] == s2[i+j]:
                        index.append([s1[i],i+j])
                        m+=1
                        break
    ##确认位移
    for i in range(len(index)):
        if i-1>=0 and index[i-1][1] > index[i][1]:
            t+=2
    ###算法
    print(m,c,t,'\n',index)
    print(( m*10000/len(s1) + m*10000/len(s2) + (m-int(t/2))*10000/m )/30000)

c = cal(strA,strB)
main(strA,strB,c)
input()