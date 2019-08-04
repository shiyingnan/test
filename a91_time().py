# -*- coding: utf-8 -*-
# 时间函数
import time

x=time.strftime("%Y-%m-%d %H:%M:%S")

print(x)
time.sleep(1)
print(x)
y=time.strftime("%Y-%m-%d %H:%M:%S")
print("y:",y)

a=time.ctime(time.time())
print(a)
time.sleep(2)
print(time.ctime(time.time()))
c=time.asctime(time.localtime(time.time()))
print("c:",c)
d=time.asctime(time.gmtime(time.time()))  #格林威治时间
print(d)

#计算消耗时间
start=time.time()
time.sleep(2)
end=time.time()
xtime=end-start
print("消耗时间:%.2f秒"%xtime)

start2 = time.clock()
print(start2)
for j in range(2000):
    print(j)
end2 = time.clock()
xx=end2-start2
print('different is %6.3f' %xx)



# wb=load_workbook(r"C:\Users\SYN\Desktop\SynPython\file.xlsx")
# ws=wb['syntest']
# elist=[]
#
# for i in ws['A2':'C18']:
#     elist.append(i)
#
# syndict=defaultdict(list)
# for c in elist:
#     syndict[c[0].value].append(c[1].value)
#     syndict[c[0].value].append(c[2].value)
# syndict=dict(syndict)
# print(syndict)
#
# ws2=wb['result']
# slist=[]
# for cc in ws2['A']:
#     if cc.value in syndict:
#         slist.append(syndict[cc.value][1])
# print(len(slist))


