from os import system
import tkinter as tk
from easygui import indexbox as ibox
win=tk.Tk()
bg=tk.PhotoImage(file='bg.png')
usrCount=0
win.title('PY12306')
win.resizable(0, 0)
usrEnt=None
pwdEnt=None
fromEnt=None
toEnt=None
dateEnt=None
nameEnt=None
textvariablelist=[]
def editUsrCfg():
    global usrEnt,pwdEnt,fromEnt,toEnt,dateEnt,nameEnt
    for i in range(7):
        textvariablelist.append(tk.StringVar())
    cfgWin=tk.Toplevel(master=win)
    usrEnt=tk.Entry(cfgWin,textvariable=textvariablelist[0])
    usrEnt.pack()
    #usrEntList.append(usrEnt)
    pwdEnt=tk.Entry(cfgWin,textvariable=textvariablelist[1])
    pwdEnt.pack()
    #pwdEntList.append(pwdEnt)
    fromEnt=tk.Entry(cfgWin,textvariable=textvariablelist[2])
    fromEnt.pack()
    #fromEntList.append(fromEnt)
    toEnt=tk.Entry(cfgWin,textvariable=textvariablelist[3])
    toEnt.pack()
    #toEntList.append(toEnt)
    dateEnt=tk.Entry(cfgWin,textvariable=textvariablelist[4])
    dateEnt.pack()
    #dateEntList.append(dateEnt)
    nameEnt=tk.Entry(cfgWin,textvariable=textvariablelist[5])
    nameEnt.pack()
    #nameEntList.append(nameEnt)
    cfgBtn=tk.Button(cfgWin,text='确认',command=saveCfg).pack()
    textvariablelist[0].set('账号')
    textvariablelist[1].set('密码')
    textvariablelist[2].set('出发站')
    textvariablelist[3].set('目的站')
    textvariablelist[4].set('日期')
    textvariablelist[5].set('姓名')
    cfgWin.mainloop()
def saveCfg():
    global usrCount
    #for i in range(len(usrEntList)):
        with open('usr/usr'+str(usrCount)+'.cfg','w')as IO:
            IO.write(usrEnt.get()+','+pwdEnt.get()+','+fromEnt.get()+','+toEnt.get()+','+dateEnt.get()+','+nameEnt.get())
        #usrCount+=1
def launch():
    system('py12306-master/py12306.py')
tk.Label(win,image=bg).pack()
tk.Button(win,text='更改用户配置',command=editUsrCfg).place(x=0,y=0)
tk.Button(win,text='开始抢票',command=launch).place(800,400)
tk.mainloop()