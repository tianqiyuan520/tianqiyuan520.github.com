import math
##题一

class 题二():
    def __init__(self) -> None:
        self.time = 500
        self.num = 0
    def __call__(self,n):
        self.a(n)
    def a(self,n:int)->float:
        if self.time >= 0:
            self.time -=1
            self.num += 1
            return math.sqrt(1+self.num*(self.a(n)))
        else:
            return math.sqrt(n)

answer2 = 题二()
print(answer2.a(114514))

##题一 (调用以前写好的简陋版数组运算)
import 大数计算类_除法 as dcal
data_list = []
for i in range(2,10000):
    data = ((dcal._dev([1],dcal.transform(i**2),1)))[0]
    data[0] = '.'
    data.insert(0,0)
    print(i,data)
    data_list.append(data)

b = [1,'.',0]
for i in range(len(data_list)):
    b = dcal.add2(b,data_list[i])
result = ''
for i in b:
    result += str(i)
print(b)
print((math.pi**2)/6)

##运行结果
#9999 [0, '.', 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0]
#近似 [1, '.', 6, 4, 4, 8, 3, 4, 0, 6, 1, 8, 4, 8, 0, 5, 4, 7, 9, 0, 0]
#精准 1.6449340668482264
