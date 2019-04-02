from tkinter import *
from tkinter import font
from PIL import ImageTk,Image

import xlrd

menu_card = xlrd.open_workbook('D:\python\project one\item_details.xlsx')
flag=0
page= menu_card.sheet_by_index(0)

item_names=[]

for i in range(1,page.nrows):
    item_names.append(page.cell_value(i,1))

app=Tk()
app.minsize(1200,720)

app.configure(bg='lightgrey')
def_font=font.Font(family='georgia',size=13)

def cancel(Event=None):
    global entry2,entry1,c1,list_box,qty
    list_box.delete(0,END)
    entry1.focus_set()
    search_name.set('')
    qty.set('')
    c1.delete('all')

def remove():
    global  bill_list,bill,entry1,bill_sno,total_amount
    
    if len(bill)==0:
        return
    i=bill_list.curselection()[0]
    bill_list.delete(0)
    bill_sno=bill_sno-1
    total_amount-=bill[i][3]
    add_amount(0)
    bill.pop(i)

    for j in range(i,len(bill)):
        bill[i][0]=bill[i][0]-1
    bill_list.delete(0,END)
    bill_list.insert(END,*bill)
    entry1.focus_set()

def clear():
    global bill,bill_sno,bill_list,paid,c2,entry2,entry1,c2,c3

    paid.set('')
    qty.set('')
    c1.delete('all')
    c2.delete('all')
    c3.delete('all')
    entry1.focus_set()
    bill=[]
    bill_sno=0
    bill_list.delete(0,END)

def hover(Event):
    global clear_btn,search_btn,remove_btn,add_btn,cancel_btn,bill_btn,stack_btn
    h=Event.widget.cget('text')
    if h=='Clear':
        clear_btn['bg']='#939393'
        clear_btn['relief']='sunken'
    elif h=='Remove':
        remove_btn['bg']='#939393'
        remove_btn['relief']='sunken'
    elif h=='Cancel':
        cancel_btn['bg']='#939393'
        cancel_btn['relief']='sunken'
    elif h=='Search':
        search_btn['bg']='#939393'
        search_btn['relief']='sunken'
    elif h=='Add':
        add_btn['bg']='#939393'
        add_btn['relief']='sunken'
    elif h=='Print':
        print_btn['bg']='#939393'
        print_btn['relief']='sunken'
    elif h=='Bill':
        bill_btn['bg']='#7f95d8'
        bill_btn['relief']='sunken'
    elif h=='Stack':
        stack_btn['bg']='#7f95d8'
        stack_btn['relief']='sunken'

def cancel_hover(Event):
    global clear_btn,search_btn,remove_btn,add_btn,cancel_btn,bill_btn,stack_btn
    h=Event.widget.cget('text')
    if h=='Clear':
        clear_btn['bg']='#7f95d8'
        clear_btn['relief']='flat'
    elif h=='Remove':
        remove_btn['bg']='#7f95d8'
        remove_btn['relief']='flat'
    elif h=='Cancel':
        cancel_btn['bg']='#7f95d8'
        cancel_btn['relief']='flat'
    elif h=='Add':
        add_btn['bg']='#7f95d8'
        add_btn['relief']='flat'
    elif h=='Search':
        search_btn['bg']='#7f95d8'
        search_btn['relief']='flat'
    elif h=='Print':
        print_btn['bg']='#7f95d8'
        print_btn['relief']='flat'
    elif h=='Search':
        search_btn['bg']='#7f95d8'
        search_btn['relief']='flat'
    elif h=='Print':
        print_btn['bg']='#7f95d8'
        print_btn['relief']='flat'
    elif h=='Bill':
        bill_btn['bg']='#939393'
        bill_btn['relief']='flat'
    elif h=='Stack':
        stack_btn['bg']='#939393'
        stack_btn['relief']='flat'

def search(s):
    global item_names
    temp=[]
    for i in range(len(item_names)):
        if s in item_names[i]:
            temp.append(item_names[i])
    return (temp)

def add_amount(val):
    global c2,total_amount
    total_amount+=val
    c2.delete('all')
    c2.create_text(33,12,text='Rs,'+str(total_amount))

def create_bill(i_name,q):
    global item_names,bill,bill_sno,bill_list,out
    s1=''

    for i in range(len(item_names)):
        if item_names[i]==item_name:
            bill_sno+=1
            bill.append([bill_sno,item_name,q,q*page.cell_value(i+1,3)])
            s1=(str(bill_sno)+'.').rjust(4)
            s2=item_name.rjust(10)
            s4=str(q).rjust(3)
            s3=str(q*page.cell_value(i+1,3)).rjust(8)
            s1=s1+s2+s4+s3
            bill_list.insert(END,s1)
            bill_list.see(bill_sno)
            add_amount(q*page.cell_value(i+1,3))
            out+=s1+'\n'
            break


def get_quantity(Event=None):
    global entry2,item_name,entry1,search_name,qty

    q=int(qty.get())
    if q==0:
        return
    create_bill(item_name,q)
    search_name.set('')
    entry1.focus_set()

def print_item(i_name):
    global c1,entry2,qty

    qty.set('')
    c1.delete('all')
    c1.create_text(33,12,text='> '+i_name)
    entry2.focus_set()
    entry2.bind('<Return>',get_quantity)

def get_item(Event=None):
    global list_box,entry2,item_name
    
    item_name=list_box.get(list_box.curselection())[3:]
    print_item(item_name)

def search_item(Event=None):
    global list_box,entry2,x1,list_box

    list_box.delete(0,END)
    x1.destroy()

    s_key=str(search_name.get()).upper()
    if s_key=='':
        return

    searched_items=search(s_key)

    for i in searched_items:
        list_box.insert(END,' > '+i)
  #  if len(searched_items)==0:
  #      Label(app,text='*** No Such Item ***',font=('times new roman',11),bg='#D4FFF7').place(relx=0.11,rely=0.45,relwidth=0.8)
    
    list_box.focus_set()
    list_box.bind('<Return>',get_item)
    return

def get_balance(Event=None):
    global c3,entry3,paid,total_amount

    balance=paid.get()-total_amount
    c3.create_text(33,12,text='Rs,'+str(balance))



def get_money():
    global bill,bill_sno,bill_list,list_box,out,paid,total_amount,c3,entry3,total_amount
    
    out+=('Total Amount : '+str(total_amount)).rjust(25)
    entry3.focus_set()
    paid.set('')
    entry3.bind('<Return>',get_balance)

    list_box.delete(0,END)
    print(bill)
    print(out)
    bill=[]
    bill_sno=0
    out=''

def billing():
    global flag1,flag2,logo,l1,l2,bill_btn,stack_btn,f0,f1,search_name,f5,lb1,lb2,lb4,lb3,lb5,lb6,lb7,entry1,entry2,entry3,c1,c2,c3,x1,list_box,bill_list,qty,clear_btn,remove_btn,cancel_btn,add_btn,search_btn,print_btn,paid

    if flag1==True:
        flag1=False
        flag2=True
    else:
        return

    f0=Frame(app,bg='lightgrey')
    f0.place(x=90,y=83,relheight=1,relwidth=1)
    logo=Label(f0,image=pic,bg='lightgrey')
    logo.place(x=-100,y=-100,relwidth=1,relheight=1)
    f1=Frame(f0,bg='lightgrey')
    f1.place(x=75,y=60,relheight=0.65,relwidth=0.28)
    
    lb1=Label(f1,text='Product Name',font=def_font,bg='lightgrey')
    lb1.place(x=0,y=0)
    entry1=Entry(f1,font=('times new roman',13),relief=FLAT,textvariable=search_name,width=20)
    entry1.place(x=2,y=25,relwidth=0.7)
    search_btn=Button(f1,text='Search',command=search_item,relief=FLAT,font=('times new roman',11),bd=0,bg='#7f95d8',width=8)
    search_btn.place(y=25,relx=0.76)

    list_box=Listbox(f1,selectmode=EXTENDED,font=def_font,relief=FLAT)
    list_box.config(activestyle='none')
    x1=Label(list_box,text='*** Enter the Item Name Above ***',font=('times new roman',11),bg='white')
    x1.place(relx=0.11,rely=0.45,relwidth=0.8)
    list_box.config(activestyle='none',selectbackground='grey',bd=0)
    list_box.place(x=0,y=80,relwidth=1,relheight=0.6)
    entry1.bind('<Return>',search_item)
    entry1.focus_set()

    lb2=Label(f1,text='Selected Product',font=def_font,bg='lightgrey')
    lb2.place(x=0,rely=0.8)
    c1=Canvas(f1,height=20)
    c1.place(x=2,rely=0.85,relwidth=0.7)
    lb3=Label(f1,text='Count',font=def_font,bg='lightgrey')
    lb3.place(relx=0.8,rely=0.8)
    entry2=Entry(f1,font=('times new roman',13),relief=FLAT,textvariable=qty,width=20)
    entry2.place(relx=0.8,rely=0.85,relwidth=0.2)
    
    f3=Frame(f1,bg='lightgrey')
    add_btn=Button(f3,text='Add',font=('times new roman',11),command=get_quantity,width=8,bd=0,relief=FLAT,bg='#7f95d8')
    add_btn.pack(side=LEFT,padx=2)
    cancel_btn=Button(f3,text='Cancel',font=('times new roman',11),command=cancel,bd=0,width=8,relief=FLAT,bg='#7f95d8')
    cancel_btn.pack(pady=3,side=RIGHT)
    f3.pack(side=BOTTOM,anchor=SE)

    
    f2=Frame(f0,bg='lightgrey')
    f2.place(relx=0.62,rely=0.08,relheight=0.63,relwidth=0.25)

    lb3=Label(f2,text='Bill',font=def_font,bg='#9fabcf')
    lb3.place(relx=0,y=45,relwidth=1)
    bill_list=Listbox(f2,relief=FLAT,selectmode=EXTENDED,font=def_font)
    bill_list.config(activestyle='none',selectbackground='grey',bd=0)
    bill_list.place(x=0,y=70,relwidth=1,relheight=0.75)
    
    f4=Frame(f2,bg='lightgrey')
    print_btn=Button(f4,text="Print",font=('times new roman',11),command=get_money,width=8,bd=0,relief=FLAT,bg='#7f95d8')
    print_btn.pack(side=LEFT)
    remove_btn=Button(f4,text='Remove',font=('times new roman',11),command=remove,width=8,bd=0,relief=FLAT,bg='#7f95d8')
    remove_btn.pack(side=LEFT,padx=2)
    clear_btn=Button(f4,text='Clear',font=('times new roman',11),command=clear,width=8,bd=0,relief=FLAT,bg='#7f95d8')
    clear_btn.pack(side=RIGHT)
    f4.pack(side=BOTTOM,anchor=SE)
    
    f5=Frame(f0,bg='lightgrey')
    f5.place(relx=0.385,rely=0.75,relheight=0.1,relwidth=0.5)

    lb5=Label(f5,text='Amount',font=def_font,bg='lightgrey')
    lb5.place(relx=0,rely=0)
    c2=Canvas(f5,bd=0,height=20)
    c2.place(relx=0,rely=0.3,relwidth=0.32)

    lb6=Label(f5,text='Paid',font=def_font,bg='lightgrey')
    lb6.place(relx=0.33,rely=0)
    entry3=Entry(f5,font=('times new roman',13),relief=FLAT,textvariable=paid,width=20)
    entry3.place(relx=0.33,rely=0.3,relwidth=0.32)

    lb7=Label(f5,text='Balance',font=def_font,bg='lightgrey')
    lb7.place(relx=0.66,rely=0)
    c3=Canvas(f5,bd=0,height=20)
    c3.place(relx=0.66,rely=0.3,relwidth=0.34)

    remove_btn.bind('<Enter>',hover)
    remove_btn.bind('<Leave>',cancel_hover)
    cancel_btn.bind('<Enter>',hover)
    cancel_btn.bind('<Leave>',cancel_hover)
    clear_btn.bind('<Enter>',hover)
    clear_btn.bind('<Leave>',cancel_hover)
    add_btn.bind('<Enter>',hover)
    add_btn.bind('<Leave>',cancel_hover)
    search_btn.bind('<Enter>',hover)
    search_btn.bind('<Leave>',cancel_hover)
    print_btn.bind('<Enter>',hover)
    print_btn.bind('<Leave>',cancel_hover)


def stack():
    global f0,flag2,flag1

    if flag2==True:
        flag2=False
        flag1=True
    else:
        return
    f0.destroy()


img=Image.open("D:/python/project one/logo.png")
pic=ImageTk.PhotoImage(img)

logo=Label(app,image=pic,bg='lightgrey')
logo.place(x=-30,y=0,relwidth=1,relheight=1)
l2=Frame(app,bg='#4d4d4d',height=80)
l2.pack(side=TOP,fill='x')
l1=Frame(app,bg='#676767')
l1.pack(side=LEFT,fill='y')

f0=Frame(app)
f1=Frame(f0)
f2=Frame(f0)
f3=Frame(f1)
f4=Frame(f2)
f5=Frame(f0)

x1=Label(f1)
lb1=Label(f1)
lb2=Label(f1)
lb3=Label(f1)
lb4=Label(f1)
lb5=Label(f0)
lb6=Label(f0)
lb7=Label(f0)

c1=Canvas(f1)
c2=Canvas(f5)
c3=Canvas(f5)

entry1=Entry(f1)
entry2=Entry(f1)
entry3=Entry(f5)

bill_btn=Button(l1,text='Bill',relief=FLAT,command=billing,height=3,bd=0,width=8,font=def_font,bg='#939393')
bill_btn.pack(fill='x',pady=1)
bill_btn.bind('<Enter>',hover)
bill_btn.bind('<Leave>',cancel_hover)
stack_btn=Button(l1,text='Stack',relief=FLAT,command=stack,height=3,bd=0,font=def_font,bg='#939393')
stack_btn.pack(fill='x',pady=1)
stack_btn.bind('<Enter>',hover)
stack_btn.bind('<Leave>',cancel_hover)

list_box=Listbox(f1)
bill_list=Listbox(f2)
x1=Label(list_box)

back_btn=Button(app)
add_btn=Button(f3)
cancel_btn=Button(f3)
search_btn=Button(f1)
remove_btn=Button(f4)
clear_btn=Button(f4)
print_btn=Button(f4)

search_name=StringVar()
qty=IntVar()
bill=[]
bill_sno=0
out=''
total_amount=0
paid=IntVar()
flag1=True
flag2=True

app.mainloop()