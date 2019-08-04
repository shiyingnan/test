# -*- coding: utf-8 -*-
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
import json
import requests
import re

a="hellouioewrjklhedf12345-im0g--=====<im0glike、。/>love【下载地址-】b0rhelhbyb0r"

# patt=re.compile(r"h([\s\S]*)<img[\s\S]*?/>|【下载地址】")
patt=re.compile(r"h(.*?)l")
# imggroup=patt.search(a).group(2)
# print(imggroup)
d=patt.findall(a)    #不匹配返回[]空集
print(d)
t=re.sub(r"he9llo|im9g","---",a)   #不匹配不报错
print(t)
w=t.split("im02222g",1)      #不匹配不报错
print(w)

syn={}
syn.setdefault("nihao",[])
syn=syn["nihao"]+["po"]
print(syn)

# d={"a":3,"b":4}
# def test(**kv):
#     kv.update({"p":9})
#     print(kv)
#
# kv=d
# test(**kv)



# def post_image():
#     img = "2.jpg"  # 图片路径
#     files = {"pic_path": open(img, "rb")}  # files # 类似data数据
#     url = "http://pic.sogou.com/pic/upload_pic.jsp"  # post的url
#     html = requests.post(url, files=files).text  # requests 提交图片
#     get_content(html)  # 结果是url就是图片的url sougou 把本地图片上传到sougou服务器变成了他的图片 调用解析函数把url传入
#
#
# def get_content(keywords):
#     url = "http://pic.sogou.com/pic/ocr/ocrOnline.jsp?query=" + keywords  # keywords就是图片url此方式为get请求
#     ocrResult = requests.get(url).json()  # 直接转换为json格式
#     contents = ocrResult['result']  # 类似字典 把result的value值取出来 是一个list然后里面很多json就是识别的文字
#     for content in contents:  # 遍历所有结果
#         print(content['content'].strip())  # strip去除空格 他返回的结果自带一个换行
#
#
# post_image()



# dc=OrderedDict()
# syn=["nihao","hello","nihao","have","you","no","trouble","Yo","hello","world","nihao","hello","3"]
#
#
# synset=set(syn)
# for i in syn:
#     dc[i]=syn.count(i)
#
# j=json.dumps(dc)
# print(type(j),j)
# k=json.loads(j)
# for q in zip(k.values(),k.keys()):
#     print(q)
# print(dir(Counter))
# word_counts=Counter(syn)
# x=word_counts.most_common(3)
#
# print(x)
# y=sorted(word_counts)
# print(y)
# print(word_counts["hello"])

# d=defaultdict(list)
# d[4]=89
# d["n"]=["90"]
# d["3"]="po"
#
# print(dict(d))
# p="".join(d["n"])
# print(p)
#
#
# dt={}
# dt["p"]=90
# dt["n"]=["90"]
# print(dt)

# byamax=simplegui.load_image('http://img05.tooopen.com/images/20150820/tooopen_sy_139205349641.jpg')
#
# WIDTH=600
# HEIGHT=600+100
# IMAGE_SIZE=WIDTH/3
# all_coordinates=[[IMAGE_SIZE*0.5,IMAGE_SIZE*0.5],[IMAGE_SIZE*1.5,IMAGE_SIZE*0.5],
#                 [IMAGE_SIZE*2.5,IMAGE_SIZE*0.5],[IMAGE_SIZE*0.5,IMAGE_SIZE*1.5],
#                 [IMAGE_SIZE*1.5,IMAGE_SIZE*1.5],[IMAGE_SIZE*2.5,IMAGE_SIZE*1.5],
#                 [IMAGE_SIZE*0.5,IMAGE_SIZE*2.5],[IMAGE_SIZE*1.5,IMAGE_SIZE*2.5],None
#                  ]
#
# ROWS=3
# COLS=3
# steps=0
# board=[[None,None,None],[None,None,None],[None,None,None]]
#
# class Square():
#     def __init__(self,coordinage):
#         self.center=coordinage
#     def draw(self,canvas,board_pos):
#         canvas.draw_image(byamax,self.center,[IMAGE_SIZE,IMAGE_SIZE],
#                           [(board_pos[1]+0.5)*IMAGE_SIZE,(board_pos[0]+0.5)*IMAGE_SIZE],[IMAGE_SIZE,IMAGE_SIZE])
#
# def init_board():
#     random.shuffle(all_coordinates)
#     for i in range(ROWS):
#         for j in range(COLS):
#             idx=i*ROWS+j
#             square_center=all_coordinates[idx]
#             if square_center is None:
#                 board[i][j]=None
#             else:
#                 board[i][j]=Square(square_center)
#
# def play_game():
#     global steps
#     steps=0
#     init_board()
#
# def draw(canvas):
#     canvas.draw_image(byamax,[WIDTH/2,WIDTH/2],[WIDTH,WIDTH],[50,WIDTH+50],[98,98])
#     canvas.draw_text('步数:'+str(steps),[400,680],22,'White')
#     for i in range(ROWS):
#         for j in range(COLS):
#             if board[i][j] is not None:
#                 board[i][j].draw(canvas,[i,j])
# def mouseclick(pos):
#     global steps
#     r=int(pos[1]//IMAGE_SIZE)
#     c=int(pos[0]//IMAGE_SIZE)
#     if r < 3 and c<3:
#         if board[r][c] is None:
#             return
#         else:
#             current_square=board[r][c]
#             if r-1 >=0 and board[r-1][c] is None:
#                 board[r][c]=None
#                 board[r-1][c]=current_square
#                 steps+=1
#             elif c+1<=2 and board[r][c+1] is None:
#                 board[r][c]=None
#                 board[r][c+1]= current_square
#                 steps+=1
#             elif r+1<=2 and board[r+1][c] is None:
#                 board[r][c]= None
#                 board[r+1][c]=current_square
#                 steps+=1
#             elif c-1>=0 and board[r][c-1] is None:
#                 board[r][c]=None
#                 board[r][c-1]=current_square
#                 steps+=1
#
# frame=simplegui.create_frame('拼图',WIDTH,HEIGHT)
# frame.set_canvas_background("Black")
# frame.set_draw_handler(draw)
# frame.add_button("重新开始",play_game,60)
#
# frame.set_mouseclick_handler(mouseclick)
# play_game()
# frame.start()







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


