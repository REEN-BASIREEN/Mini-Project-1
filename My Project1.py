from tkinter import *
from tkinter import ttk,messagebox


GUI = Tk() #Tk() คือหน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึก')
GUI.geometry('700x750+500+50')

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_t1 = PhotoImage(file = 't1_expense.png')


Tab.add(T1,text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound ='top')


F1=Frame(T1)
F1.place(x=100,y=50)

def meat():
	v_price.set(300)
    
	

def bone():
	v_price.set(100)
  

def paw():
	v_price.set(60)
	
def offal():
	v_price.set(80)
	
def Save(even=None):
   
    price=v_price.get()
    quantity=v_quantity.get()

    
    if price == '' : 
        messagebox.showerror('Error','กรุณากรอกราคา')   
        return
    elif quantity == '' : 
        messagebox.showerror('Error','กรุณากรอกจำนวน')   
        return
    

    try:
        total=int(price)*int(quantity)
        
        # print('รายการ:{} ราคาชิ้นละ:{} บาท'.format(v_price,price))
        # print('จำนวน:{} ชิ้น ค่าใช้จ่ายทั้งหมด:{} บาท'.format(quantity,total))
        # text = 'รายการ:{} ราคาชิ้นละ:{} บาท\n'.format(v_price,price)
        text =  'ค่าใช้จ่ายทั้งหมด:{} บาท'.format(total)
        v_result.set(text)
        
        v_price.set('')
        v_quantity.set('')
       

      
    except:
        print('ERROR')
        messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่')
        
       
        v_price.set('')
        v_quantity.set('')
       

GUI.bind('<Return>',Save)

FONT1 = ('Arial Rounded MT Bold',18)


ttk.Button(F1,text='ปลากระพง',command=meat).pack(ipadx=20,ipady=10)
ttk.Button(F1,text='ปลานิล',command=bone).pack(ipadx=20,ipady=10)
ttk.Button(F1,text='ปลาช่อน',command=paw).pack(ipadx=20,ipady=10)
ttk.Button(F1,text='ปลาดุก',command=offal).pack(ipadx=20,ipady=10)


L=ttk.Label(F1,text='ราคา',font=FONT1).pack()
v_price=StringVar()

E2=ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack(pady=10)

L=ttk.Label(F1,text='จำนวน',font=FONT1).pack()
v_quantity=StringVar()

E3=ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack(pady=10)


B1=ttk.Button(F1,text='คำนวน',compound='left',command=Save)
B1.pack(ipadx=50,ipady=20)

v_result = StringVar()
v_result.set('------รวมเป็นเงิน-----')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='red')
result.pack(pady=20)



GUI.mainloop()