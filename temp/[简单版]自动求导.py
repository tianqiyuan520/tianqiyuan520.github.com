class Derivative:
    def __init__(self,content) -> None:
        self.content = content
    def translate(self,data:list) -> list:
        '''数组化简'''
        pass
        # new_data = []
        # def a(j:list,deep):
        #     while isinstance(j,list):
        #         deep += 1
        #         j = j[0]
        #     return j,deep
        # def b(j:list,deep):
        #     if deep >= 1:
        #         deep -= 1
        #     j = data[0]
        #     for i in range(deep): j = j[0]
        #     if len(j) > 1:
        #         cc = a(j,deep)
        #         j=cc[0]
        #         deep=cc[1]
        # while data:
        #     j = data[0]
        #     deep = 0
        #     cc = a(j,deep)
        #     j=cc[0]
        #     deep=cc[1]
        #     b(j,deep)
        #     data.pop(0)

        # for i in range(len(data)):
            # print('第',i,'部分 ',data[i])
            # j = data[i]
            # time = -1
            # while isinstance(j,list):
            #     time += 1
            #     j = j[0]
            # time2 = time
            # while time2 >0:
            #     time2 -=1
            #     new_data.append("(")
            # if isinstance(data[i],list) and len(data[i]) > 1:
            #     new_data.append(data[i])
            # time2 = time
            # while time2 >0:
            #     time2 -=1
            #     new_data.append("(")
        
        print('新\n',str(data).replace('[[','(').replace(']]',')'))
    def s_num(self):
        '''分离数字,数字合并'''
        is_num = 0
        num = ''
        content_list = []
        for i in range(len(self.content_l)):
            try:
                int(self.content_l[i])
                is_num=1
            except:
                is_num=0
            if is_num == 1:
                num += self.content_l[i]
            else:
                if num != '':
                    content_list.append([int(num)])
                content_list.append([self.content_l[i]])
                num = ''
            if i == len(self.content_l)-1:
                if num != '':
                    content_list.append([int(num)])
        self.content_l = content_list

    def s_1(self,data:list):
        '''分离括号外的 +-'''
        ##括号外部，以加减法分为一组一组
        is_e = 0
        content_list = [[]]
        for i in data:
            if i[0] == '(':
                is_e += 1
            elif i[0] == ')':
                is_e -= 1
            if is_e == 0:
                if i[0] != '-' and i[0] != '+':
                    content_list[-1].append([i[0]])
                else:
                    content_list.append([i[0]])
                    content_list.append([])
            else:
                content_list[-1].append([i[0]])
        # print(content_list)
        return content_list
    def s_p(self,data:list,mode=0):
        '''分离括号外的 连接符号 mode是否查^'''
        ##括号外部，以加减法分为一组一组
        ##如果左右边有括号，则去括号 (去除后符号对等)
        if data[0] == ['('] and data[-1] == [')']:
            data.pop(-1)
            data.pop(0)
            num = []
            ##进栈，出栈
            for i in data:
                if i[0] == '(':
                    num.append(1)
                elif len(num) >= 1 and i[0] == ')':
                    num.pop(-1)
            print(num)
            if len(num) != 0:
                data.append([')'])
                data.insert(0,['('])
        #
        is_e = 0
        per = []
        content_list = [[]]
        for i in data:
            if i[0] == '(':
                is_e += 1
            elif i[0] == ')':
                is_e -= 1
            if is_e == 0:
                if mode ==1 :
                    if (i[0] != '-' and i[0] != '+' and i[0] != '*' and i[0] != '/' and i[0] != '^'):
                            content_list[-1].append([i[0]])
                    else:
                        per.append(i[0])
                        content_list.append([i[0]])
                        content_list.append([])
                else:
                    if (i[0] != '-' and i[0] != '+' and i[0] != '*' and i[0] != '/'):
                            content_list[-1].append([i[0]])
                    else:
                        per.append(i[0])
                        content_list.append([i[0]])
                        content_list.append([])
            else:
                content_list[-1].append([i[0]])
        return content_list,per
    def be_simple(self,data:list):
        '''化简'''
        content_list = []
        i = 0
        while i < len(data):
            if isinstance(data[i][0],int):
                if i >= 1 and i<=len(data)-4 and data[i-1][0] != '-'and data[i-1][0] != '/'and data[i-1][0] != '^' and isinstance(data[i+2][0],int) and data[i+3][0] != '^':
                    if data[i+1][0] == '+':
                        content_list.append([data[i][0]+data[i+2][0]])
                        i+=2
                    elif data[i+1][0] == '-':
                        content_list.append([data[i][0]-data[i+2][0]])
                        i+=2
                    elif data[i+1][0] == '^':
                        content_list.append([data[i][0]**(data[i+2][0])])
                        i+=2
                    elif data[i+1][0] == '*':
                        content_list.append([data[i][0]*(data[i+2][0])])
                        i+=2
                    elif data[i+1][0] == '/':
                        content_list.append([data[i][0]/(data[i+2][0])])
                        i+=2
                elif i == 0 and i<=len(data)-3 and isinstance(data[i+2][0],int):
                    if i+3 == len(data):
                        if data[i+1][0] == '+':
                            content_list.append([data[i][0]+data[i+2][0]])
                            i+=2
                        elif data[i+1][0] == '-':
                            content_list.append([data[i][0]-data[i+2][0]])
                            i+=2
                        elif data[i+1][0] == '^':
                            content_list.append([data[i][0]**(data[i+2][0])])
                            i+=2
                        elif data[i+1][0] == '*':
                            content_list.append([data[i][0]*(data[i+2][0])])
                            i+=2
                        elif data[i+1][0] == '/':
                            content_list.append([data[i][0]/(data[i+2][0])])
                            i+=2
                    elif i<=len(data)-4 and data[i+3][0] != '^':
                        if data[i+1][0] == '+':
                            content_list.append([data[i][0]+data[i+2][0]])
                            i+=2
                        elif data[i+1][0] == '-':
                            content_list.append([data[i][0]-data[i+2][0]])
                            i+=2
                        elif data[i+1][0] == '^':
                            content_list.append([data[i][0]**(data[i+2][0])])
                            i+=2
                        elif data[i+1][0] == '*':
                            content_list.append([data[i][0]*(data[i+2][0])])
                            i+=2
                        elif data[i+1][0] == '/':
                            content_list.append([data[i][0]/(data[i+2][0])])
                            i+=2
                elif i<=len(data)-3 and isinstance(data[i+2][0],int) == False:
                    content_list.append([data[i][0]])
                elif (i >= 1 and i<=len(data)-4 and data[i-1][0] != '-'and data[i-1][0] != '/'and data[i-1][0] != '^')==False:
                    content_list.append([data[i][0]])
            else:
                content_list.append([data[i][0]])
            i+=1
        return(content_list)
    def der(self,data:list):
        '''对给定的参数求导'''
        ...
    def main(self):
        '''主程序'''
        self.content_l = list(self.content)
        self.s_num()
        print('初步解析:',self.content_l)
        # print('初步解析:',self.be_simple(self.content_l))
        ##定义循环的 类似 树结构   [[ [数据] , [指针],[指针对应的数据是否求导(0,1),1,0,01,1,1...] ],[],...]
        self.main_tree = []
        ##分离
        data = self.s_1(self.content_l)
        # for i in range(len(data)):
        #     if data[i][-2]:
        #         ...
        # if data[-2] == '^':
            # ...
        is_dir = []
        for i in range(len(data)):
            # print('第',i,'部分: ',data[i],'分离',self.s_p(data[i])[0],'连接的符号: ',self.s_p(data[i])[1])
            if (data[i]) == ['-'] or (data[i]) == ['+']:
                is_dir.append(0)
            else:
                is_dir.append(1)
        print(is_dir)
        self.main_tree.append([data,[0],is_dir])
        time = 0
        self.is_return= 0
        self.end = False
        while time < 100 and (self.end==False):
            print('\n\n\n========================第',time,'次========================\n\n')
            self.get_der()
            time+=1
        if self.end:
            self.translate(self.main_tree[0][0])
    def get_der(self):
        index = self.main_tree[-1][1][0] #指针的数据
        # 指针+1 (index迭代)
        if index < len(self.main_tree[-1][0])-1:
            self.main_tree[-1][1][0] = index+1
        data = self.main_tree[-1][0] ##该数据
        is_der = self.main_tree[-1][2][index] ##判断对应指针的数据 是否需要求导
        # print('参数:  \n',data,'\n')
        print(index,self.is_return)
        #判断 指针是否越界:
        if index == len(data)-1:
            self.is_return += 1
        if index == len(data)-1 and self.is_return >= 3:
            print('终\n')
            if len(self.main_tree) == 1:
                print('求导结束')
                self.end = True
            else:
                past_index = self.main_tree[-2][1][0]
                if past_index != len(self.main_tree[-2][0])-1:
                    past_index -= 1
                self.is_return = 0
                print('上一个的数据\n',self.main_tree[-2][0][past_index])
                print('当前的数据\n',data)
                #结果赋值
                self.main_tree[-2][0][past_index] = data
                self.main_tree[-2][2][past_index] = 0
                print('更新的数据\n',self.main_tree[-2][0][past_index])
                self.main_tree.pop(-1)
        else:
            if is_der == 1:
                data_new = self.s_p(data[index])[0] ## 对应指针的数据 分离后的数据
                per = self.s_p(data[index])[1] ## 对应指针的数据 分离后的数据 连接符号
                print('符号:\n',per)
                if len(per) == 0:
                    #无连接符号
                    data_new = self.s_p(data[index],1)[0]
                    per = self.s_p(data[index],1)[1]
                    if len(per) == 0:
                        if data_new[0][0][0]:
                            ##判断是 数字或 未知数
                            print(data_new[0][0][0])
                            if isinstance(data_new[0][0][0],int):
                                data[index] = [[0]]
                            else:
                                data[index] = [[1]]
                            self.main_tree[-1][2][index] = 0
                    
                #有符号
                if per == ['*']:
                    ## (u*v)' = u'*v + u*v'
                    #求左边的导数
                    self.main_tree.append([[data_new[0],['*'],data_new[2],['+'],data_new[0],['*'],data_new[2]],[0],[1,0,0,0,0,0,1]])
                elif per == ['^']:
                    ## [f(x)^n]' = (n-1)*f(x)^(n-1)*f'(x)
                    self.main_tree.append([[data_new[2],['*'],data_new[0],['^'],['('],data_new[2],['-'],[1],[')'],['*'],data_new[0]],[10],[0,0,0,0,0,0,0,0,0,0,1]])
                elif per == ['/']:
                    ## (u/v)' =  (u'*v - u*v') / (v^2)
                    self.main_tree.append([[['('],data_new[0],['*'],data_new[2],['-'],data_new[0],['*'],data_new[2],[')'],['/'],['('],data_new[2],['^'],[[2]],[')']],[0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]])
                elif per == ['+']:
                    self.main_tree.append([[data_new[0],['+'],data_new[2]],[0],[1,0,1]])
                elif per == ['-']:
                    self.main_tree.append([[data_new[0],['-'],data_new[2]],[0],[1,0,1]])
        if self.end == False:
            print('当前传入的数据:\n','指针:',index,'\n是否要导',self.main_tree[-1][2],'\n当前数据:\n',data[index],'\n源数据\n',data,'\n')
            print('\n','当前树结构',self.main_tree)
print('start...')
main = Derivative("(233*x)^2-x-4+3*x-(x^5-(6*x))/(3*x)")
# main = Derivative("(233*x)^2")
main.main()




## 根据深度遍历

result = []
result2 = []
deeps = []
deep = 0
def printList(list1,deep):
    for elements in list1:
        if isinstance(elements,list):
            printList(elements,deep+1) #递归调用函数本身进行深层次的遍历
        else :
            # print(elements)
            deeps.append(deep)
            result.append(elements)


list1 = main.main_tree[0][0]

printList(list1,0)


def a():
    '''根据深度,转括号'''
    deep = 0
    for i in range(0,len(result)):
        # print('当前指针:',i,'当前深度',deeps[i],'上一个深度:',deep,'数据:',result[i])
        if i >= 0:
            if deeps[i] < deep:
                for j in range(deep-deeps[i]):
                    result2.append(')')
                deep = deeps[i] 
            if deeps[i] > deep:
                for j in range(deeps[i]-deep):
                    result2.append('(')
                deep = deeps[i] 
        result2.append(result[i])
        if i == len(result)-1:
            #末尾
            if deep > 0:
                for j in range(deep):
                    result2.append(')')

def b():
    '''去除无意义括号'''
    for i in range(len(result)):
        if i >= 1 and i <= len(result) -2 and result[i] != '(' and result[i] != ')' and result[i-1] == '(' and result[i+1] == ')':
            result.pop(i-1)
            result.pop(i)
        if i >= 1 and i <= len(result) -2 and result[i] == '(' and result[i+1] == ')':
            result.pop(i+1)
            result.pop(i)

def c():
    '''转字符串'''
    string = ''
    for i in result:
        string += str(i)
    return string


a()
print('深度：',deeps)
print('数据1:\n',result,'\n数据2:\n',result2)
result = result2
b()
print('new: ',c())
