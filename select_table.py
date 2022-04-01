from tkinter import*
#初始化Tk()
import DP
from scatter import scatter
from search import sqlite_read


def select_table():
    tk = Tk()
    tk.geometry('500x400')
    tk.title('Python GUI Learning')
    v = IntVar()
    #列表中存储的是元素是元组
    language=sqlite_read()
    #定义单选按钮的响应函数
    def callRB():
        for i in range(4):
            if (v.get()==i):
                root1 = Tk()
                Label(root1,text='你的选择是'+language[i]+'!', command=scatter(language[i]),fg='red',width=20, height=6).pack()
                # Button(root1,text='确定',width=3,height=1,command=root1.destroy).pack(side='bottom')
    Label(tk,text='选择数据').pack(anchor=W)
    #for循环创建单选框
    for num in range(len(language)):
        Radiobutton(tk, text=language[num], value=num, command=callRB, variable=v).pack(anchor=W)
    #进入消息循环
    tk.mainloop()
select_table()