from tkinter import*

# 初始化Tk()
import DP
from search import sqlite_read


# 动态规划算法
def dpAlgrithm(s):
    # r.destroy()
    print(s)
    DP.zhi(s)


def select_table():
    myWindow = Tk()
    myWindow.geometry('500x400')
    myWindow.title('选取文件')
    v = IntVar()
    # 列表中存储的是元素是元组
    language = sqlite_read()
    # print(language)


    # 定义单选按钮的响应函数
    def callRB():
        for i in range(len(language)):
            if (v.get()==i):
                root1 = Tk()
                Label(root1,text='你的选择是'+language[i]+'!',fg='red',width=20, height=6).pack()
                Button(root1,text='确定', width=3, height=1, command=dpAlgrithm(language[i])).pack(side='bottom')
    Label(myWindow,text='选择要操作的文件').pack(anchor=W)
    #for循环创建单选框
    for i in range(len(language)):
        Radiobutton(myWindow, text=language[i], value=i, command=callRB, variable=v).pack(anchor=W)
    # 进入消息循环
    myWindow.mainloop()