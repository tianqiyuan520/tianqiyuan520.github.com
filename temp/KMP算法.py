###KMP算法

class kmp:
    '''KMP算法'''
    def cal_next(self,Str1:str)->str:
        '''求数组的next数组值,递推'''
        index = 0
        next = [0]
        i = 1
        Str1 = Str1 if isinstance(Str1,str) else str(Str1)
        while i < len(Str1):
            if Str1[index] == Str1[i]:
                index += 1
                i += 1
                next.append(index)
            else:
                if index == 0:
                    next.append(index)
                    i+=1
                else:
                    index -= 1
        self.next = next
        return next
    next = []
    def search(self,list1:str,list2:str):
        next = self.next
        i = 0 #主串指针
        j = 0 #子串指针
        #list1为主串
        while i < len(list1):
            if list2[j] == list1[i]:
                i += 1
                j += 1
            elif j > 0:
                j = next[j-1]
            else:
                i += 1
            if j == len(list2):
                return i-j

    def __init__(self, list: str,list2: str):
        self.list = list
        self.list2 = list2
        self.cal_next(list2)
    def __call__(self):
        print(a.list,a.next)
test1='abababcaa'
test2='bcaa'
a = kmp(test1,test2)
print(a.search(a.list,a.list2))
a()
input()