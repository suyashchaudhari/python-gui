from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("425x970")
root.title("Calculator")
def click(event):
    global scvalue
    text=event.widget.cget("text")

    if text== "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except:
                tmsg.showinfo("error", "ERROR....")
                scvalue.set("ERROR")
                screen.update()

        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
        pass
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
scvalue =StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(fill=X,padx=10,pady=10,ipadx=8)
f = Frame(root,bg="grey")
b=Button(f,text="9",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="7",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(fill=X)

f = Frame(root,bg="grey")
b=Button(f,text="6",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="4",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(fill=X)


f = Frame(root,bg="grey")
b=Button(f,text="3",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="1",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(fill=X)


f = Frame(root,bg="grey")
b=Button(f,text="00",padx=25,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="0",padx=25,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="C",padx=25,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(fill=X)


f = Frame(root,bg="grey")
b=Button(f,text="+",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=28,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(fill=X)


f = Frame(root,bg="grey")
b=Button(f,text="/",padx=27,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=27,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=27,pady=15,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(fill=X)
root.mainloop()
